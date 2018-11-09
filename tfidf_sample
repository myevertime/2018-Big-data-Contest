from konlpy.tag import Kkma
from konlpy.utils import pprint
kmr=Komoran()

import pandas as pd
import openpyxl
pure= pd.read_excel("아로나민골드pure.xlsx", header=None, parse_cols='B:C')

kkma_list_unique = []
kkma_list_all = []
cloudlst = []

for row in pure.iterrows():
    data=kmr.pos(row[1].to_string())
    i=0
    while True:
        if data[i][0]=='.com' or data[i][0]=='.me' or data[i][0]=='안녕하세요' or data[i][0]=='속눈썹':
            data[i]=(',', 'Punctuation')
        elif data[i][0]=='유산' and data[i+1][0]=='균':
            data[i]=('유산균', 'NNG')
            data[i+1]=(',', 'Punctuation')
#make exceptions
        elif data[i][0]=='루' and data[i+1][0]=='테이' and data[i+2][0]=='ㄴ':
            data[i]=('루테인', 'NNG')
            data[i+1]=(',', 'Punctuation')
            data[i+2]=(',', 'Punctuation')
        if i==len(data)-2:
            break
        else:
            i=i+1
            
    nvadj= [(word,part) for word,part in data if  part=='NNG' or part=='NNP' or part=='NP' or part=='VV' or part=='VA' or part=='VCP' or part=='VCN'or part=='MM'or part=='NF'or part=='NV' or part=='NNB']
    nvadj2= [word for word,part in data if  part=='NNG' or part=='NNP'or part=='VV' or part=='VA' or part=='MM'or part=='NF'or part=='NV' or part=='NNB']
    kkma_list_all.append(nvadj)
    kkma_list_unique.append(list(set(nvadj)))
    cloudlst.append(nvadj2)
