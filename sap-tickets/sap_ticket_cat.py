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
parser.add_argument('-f', action='store', dest='texts_file',
                    help='Predict labels for given texts in the file')                     
parser.add_argument('-k', action='store', dest='K Value',
                    help='Validate the model')                     

results = parser.parse_args()

if results.do_training :
    model = fasttext.train_supervised(input="sap_ticket.train", autotuneValidationFile='sap_ticket.test')    
    # model = fasttext.train_supervised(input="sap_ticket_cat.txt", ws=6, lr=0.8, epoch=100)
    model.save_model("model_sap_ticket.bin")
elif results.sentence != None :
    model = fasttext.load_model("model_sap_ticket.bin")
    print(model.predict(results.sentence, k=3))
    # print(model.get_word_vector('super'))
    # print(model.get_nearest_neighbors('good'))
elif results.validation != None:
    model = fasttext.load_model("model_sap_ticket.bin")
    print(model.test(results.validation))
elif results.texts_file != None:
    model = fasttext.load_model("model_sap_ticket.bin")
    with open(results.texts_file) as f:
        texts = f.read().splitlines()
    predict_result = model.predict(texts, k=3)
    output_file = results.texts_file + '_labels.csv'
    with open(output_file, 'w') as fw:
        i = 0
        for text in texts:
            fw.write('%s, %s\n' % (text, predict_result[0][i]))
            i+=1