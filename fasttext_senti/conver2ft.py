## This program converts the file provided by Jaime Tenorio Ballesteros <jaime.tenorio@softtek.com>
## It converts to file which is needed by FastText
import pandas as pd

df = pd.read_csv('etd_full.csv', lineterminator='\n')

# df1 = df.head()
f = open("etd_full_ft.txt","w+")
for index, line in df.iterrows():
    senti = line['VALUE']
    clean_text =  line['TEXT'].replace('\n',' ').replace('\r', ' ')
    if senti == -1:
        label = '__label__neg'
    elif senti == 1:
        label = '__label__pos'
    else : 
        label = '__label__neu'
    f.write("%s %s \r\n" % (label, clean_text ))
f.close()