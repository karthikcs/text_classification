import sys, random, fileinput 
import pandas as pd
import argparse

#Shuf.py should take two arg one is file name , number 
#Head of top n 
#bottom of n-top

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', default=False,
                    dest='file_name',
                    help='File Name')
parser.add_argument('-n', action='store', default=False,
                    dest='number',
                    help='Number of Rows')

args = parser.parse_args()

df = pd.read_csv(args.file_name, header=None)  
df.reset_index(inplace=True)
df = df.sample(frac=1) #To shuffle the data.
df_head = df.head(int(args.number))   
tail_num = df.shape[0] - int(args.number)
df_tail = df.tail(tail_num)
df_head.to_csv("ITIS_RCA.train",columns=[0], index=False, header=False)
df_tail.to_csv("ITIS_RCA.test",columns=[0], index=False, header=False)

