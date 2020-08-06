import fasttext
import re


model = fasttext.load_model("model_stkhelp_q3.bin")

# print(model.get_subword_id('meeting'))
# print(model.get_subwords('meeting'))

# print(len(model.get_input_matrix()))
# print(len(model.get_labels()))
words = model.get_words()
# print(len(model.get_words()))
# print(len(model.get_labels()))

labels = model.get_labels()
# for label in labels:
# print(model.test_label("stkhelp.test",k=3)['__label__it_request'])
words = model.get_words()
# word = words[2]
for word in words:
    print(word,model.predict(word,k=3))

# words_with_no = 0
# words_with_only_no = 0

# searchObj2 = re.search(r'(\s|^)\d+',  '12')
# if searchObj2:
#     print('Number found')
# else: 
#     print('No Number found')

# for word in words:
#     searchObj1 = re.search(r'\w*\d\w*',  word)
#     if searchObj1:
#         words_with_no += 1

#     searchObj2 = re.search(r'(\s|^)\d+',  word)
#     if searchObj2:
#         words_with_only_no += 1

# print(words_with_no, words_with_only_no)



