import argparse
import fasttext

parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true', default=False,
                    dest='do_training',
                    help='Train mode')
parser.add_argument('-p', action='store', dest='sentence',
                    help='Predict the class of a sentence') 
parser.add_argument('-v', action='store', dest='validation',
                    help='Validate the model') 
parser.add_argument('-k', action='store', dest='K Value',
                    help='Validate the model')                     

results = parser.parse_args()

if results.do_training :
    model = fasttext.train_supervised(input="ft2-etd-train.txt", autotuneValidationFile='ft2-etd-test.txt', autotuneDuration=1800)
    # model = fasttext.train_supervised(input="amazon.train")    
    model.save_model("model_etd_full.bin")
elif results.sentence != None :
    # model = fasttext.load_model("model_amazon_q.bin")
    model = fasttext.load_model("model_etd_full_q.bin")
    senti = model.predict(results.sentence)
    print(senti[0][0])
    # print(model.get_word_vector('super'))
    # print(model.get_nearest_neighbors('good'))
elif results.validation != None:
    # model = fasttext.load_model("model_amazon_q.bin")
    model = fasttext.load_model("model_etd_full.bin")
    print(model.test(results.validation))