
# coding: utf-8

# Tokenization

import pandas as pd
import konlpy
from konlpy.tag import Komoran
k = Komoran()


# # SheetKeywords
# - Human1 남성 여성
# ---------------------------
# 2030
# - Human2 남친 여친 남자친구 여자친구 연인
# 4050
# - Human3 남편 아내 신랑 마누라 와이프
# - Human7 노인 어머니 어머님 아버지 아버님
# ---------------------------
# - Human4 임산부 수유부
# - Human5 유아 아기 어린이 아이들 
# - Human6 청소년 수험생 고3 입시
# - Human8 직장인


data = pd.read_excel("비타민제 사용자별로 구별.xlsx", sheet_name = "Human8", names = [i for i in range(6)])

contents = data[[2]] #Contents
contents_list = list((contents[2].values))

# Removing Typo - "임팩타민" bc of noun extracting
def removing_typos(a,b,content):
    content[content.index(a):content.index(b)+1] = [''.join(content[content.index(a):content.index(b)+1])]
    return content

def removing_typo(content):
    if "아로" in content:
        content[content.index("아로")] = "아로나"
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "로나" in content:
        content[content.index("로나")] = "아로나"
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "아로" in content:
        content[content.index("아로")] = "아로나"
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "아로" in content:
        content[content.index("아로")] = "아로나"
        if "민" in content:
            content = removing_typos("아로나","민",content)

# Keywords based on TF IDF 
# ---------------------------
# - Human1
# words = ["환자", "약", "담", "독", "낭", "철"]
# ---------------------------
# - Human2
# words = ["효과", "구입", "합성", "건강", "어머니", "사진", "미네랄"]
# ---------------------------
# - Human3
# words = ["신랑", "몸", "선물", "요즘", "기능", "오늘"] ## 고침 ["신랑", "몸", "선물", "기능"]
# ---------------------------
# - Human4
# words = ["아이", "사용", "방법", "건강"]
# ---------------------------
# - Human5
# words = ["어린이", "키즈", "맛", "성장기"]
# ---------------------------
# - Human6
# words = ["철", "임산부", "효능", "어린이"] ##고침 ["철", "수능", "효능", "함량"]
# ---------------------------
# - Human7
# words = ["노인", "부모", "복용", "해소", "아버지"]
# ---------------------------
# - Human8
# words = ["활력", "잇", "남편", "남성", "직장인", "몸", "눈"]

def listmaker(content) :
    analyzing_list = []
    words =   ["활력", "잇", "남편", "남성", "직장인", "몸", "눈"] #Keywords based on TF-IDF
    for word in words :
        if word in str(content):
            content = k.nouns(str(content))
            removing_typo(content)
            analyzing_list = content
    return analyzing_list

lst2 = []
for content in contents_list:
    lst = listmaker(content)
    if lst != []:
        lst2.append(lst)
        
        
# Association Analysis
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(lst2).transform(lst2)
df = pd.DataFrame(te_ary, columns=te.columns_)

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support = 0.05, use_colnames=True)

from mlxtend.frequent_patterns import association_rules

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1, support_only=False)
rules['length'] = rules['antecedents'].apply(lambda x: len(x))
rules['length2'] = rules['consequents'].apply(lambda x: len(x))
rules = rules [ (rules['length'] == 1) & (rules['length2'] == 1) ]

import openpyxl
rules.to_excel("비타민제 소비자별 연관분석 결과/Vitamin Workers.xlsx")

