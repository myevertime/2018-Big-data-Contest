
# coding: utf-8

# # tokenizing&preprocessing

# In[6]:


from gensim.models import Word2Vec
from konlpy.tag import Komoran
from konlpy.utils import pprint
kmr=Komoran()
import pandas as pd


# In[7]:


import openpyxl
pure= pd.read_excel("아로나민골드pure.xlsx", header=None, parse_cols="B:C")
print(pure[0:5])


# In[8]:


kkma_list_unique = []
kkma_list_all = []
cloudlst = []

for row in pure.iterrows():
    data=kmr.pos(row[1].to_string())
    i=0
    while True:
        if data[i][0]=='.com' or data[i][0]=='.me' or data[i][0]=='안녕하세요' or data[i][0]=='속눈썹':
            data[i]=(',', 'Punctuation')
        elif data[i][0]=='양제':
            data[i]=('영양제', 'NNG')
        elif data[i][0]=='유산' and data[i+1][0]=='균':
            data[i]=('유산균', 'NNG')
            data[i+1]=(',', 'Punctuation')
        elif data[i][0]=='아이' and data[i+1][0]=='허브':
            data[i]=('아이허브', 'NNG')
            data[i+1]=(',', 'Punctuation')
        elif data[i][0]=='아로' and data[i+1][0]=='나' and data[i+2][0]=='민':
            data[i]=('아로나민', 'NNG')
            data[i+1]=(',', 'Punctuation')
            data[i+2]=(',', 'Punctuation')
        elif data[i][0]=='씨' and data[i+1][0]=='플러스':
            data[i]=('씨플러스','NNG')
            data[i+1]=(',', 'Punctuation')
        elif data[i][0]=='임' and data[i+1][0]=='팩' and data[i+2][0]=='타' and data[i+3][0]=='민':
            data[i]=('임팩타민', 'NNG')
            data[i+1]=(',', 'Punctuation')
            data[i+2]=(',', 'Punctuation')
            data[i+3]=(',', 'Punctuation')
        elif data[i][0]=='센트' and data[i+1][0]=='룸':
            data[i]=('센트룸', 'NNG')
            data[i+1]=(',', 'Punctuation')
        elif data[i][0]=='밀크' and data[i+1][0]=='씨' and data[i+2][0]=='슬':
            data[i]=('밀크씨슬', 'NNG')
            data[i+1]=(',', 'Punctuation')
            data[i+2]=(',', 'Punctuation')
        elif data[i][0]=='루' and data[i+1][0]=='테이' and data[i+2][0]=='ㄴ':
            data[i]=('루테인', 'NNG')
            data[i+1]=(',', 'Punctuation')
            data[i+2]=(',', 'Punctuation')
        elif data[i][0]=='여치':
            data[i]=('여친', 'NNG')
        elif data[i][0]=='남' and data[i+1][0]=='친':
            data[i]=('남친', 'NNG')
            data[i+1]=(',', 'Punctuation')
        elif data[i]==('낫', 'VA'):
            data[i]=('낫', 'NNG')
        if i==len(data)-2:
            break
        else:
            i=i+1
    #kmr품사태깅임
    nvadj= [(word,part) for word,part in data if part=='NNG' or part=='NNP'or part=='NNB' or part=='NP' or part=='VV' or part=='VA' or part=='VCP' or part=='VCN'or part=='MM'or part=='NF'or part=='NV']
    nvadj2= [word for word,part in data if part=='NNG' or part=='NNP'or part=='NNB' or part=='NP' or part=='VV' or part=='VA' or part=='MM'or part=='NF'or part=='NV']
    kkma_list_all.append(nvadj)
    kkma_list_unique.append(list(set(nvadj)))
    cloudlst.append(nvadj2)


# # word2vec similarity

# In[9]:


embedding_model = Word2Vec(cloudlst, size=30, window = 2, min_count=10, workers=4, iter=100, sg=1)


# In[10]:


embedding_model.similarity('골드','효과')


# In[11]:


vecresult=embedding_model.most_similar(positive=['효과'], topn=100)
vecresult


# In[12]:


vecframe=pd.DataFrame(vecresult, columns=['token', 'similarity'])
#vecframe.to_excel('골드_효과.xlsx')


# # visualizing to cluster map

# In[15]:


from sklearn.manifold import TSNE
import matplotlib as mpl
import matplotlib.pyplot as plt
import gensim 
import gensim.models as g


# In[ ]:


vocab = list(embedding_model.wv.vocab)
X = embedding_model[vocab]

print(len(X))
print(X[0][:10])
tsne = TSNE(n_components=2)

# 100개의 단어에 대해서만 시각화
X_tsne = tsne.fit_transform(X[:100,:])
plot_embedding(X_tsne)

