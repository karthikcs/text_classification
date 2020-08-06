import argparse
import fasttext
import os, re

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true', default=False,
                    dest='do_training',
                    help='Train mode')
parser.add_argument('-p', action='store', dest='sentence',
                    help='Predict the class of a sentence') 
parser.add_argument('-v', action='store', dest='validation',
                    help='Validate the model') 
parser.add_argument('-k', action='store', dest='k',
                    help='Validate the model')                     

results = parser.parse_args()

if results.do_training :
    
    ### Create next version model_name 
    files = os.listdir('.')
    model_pattern = re.compile(r'model_senti_v.\.bin')
    it = filter(lambda x: model_pattern.search(x), files)
    model_versions = list(it)
    model_versions.sort(reverse=True)
    version = str(int(model_versions[0][13]) + 1)
    model_name = 'model_senti_v'+version+'.bin'
    # print(model_name)

    ### Prepare training and testing files
    os.system('shuf sentiments.txt > senti.all')
    num_lines = sum(1 for line in open('senti.all'))
    n_train  = num_lines * 0.8
    n_test = num_lines - n_train
    os.system('head -n %d senti.all  > senti.train' % n_train)
    os.system('tail -n %d senti.all > senti.test' % n_test)


    ### train the model
    model = fasttext.train_supervised(input="senti.train", autotuneValidationFile='senti.test')    
    # model = fasttext.train_supervised(input="senti.train")    
    model.save_model(model_name)


elif results.sentence != None :
    model = fasttext.load_model("model_senti_v4.bin")
    print(model.predict(results.sentence, results.k))
elif results.validation != None:
    model = fasttext.load_model("model_senti_v4.bin")
    print(model.test(results.validation))