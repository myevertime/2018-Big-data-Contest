
# coding: utf-8

# ## Association Rules

# In[11]:


import pandas as pd
import konlpy
from konlpy.tag import Komoran
k = Komoran()


# # SheetKeywords
# 
# - Human1 남성 여성 
# 
# ---------------------------
# 
# 2030
# 
# - Human2 남친 여친 남자친구 여자친구 연인
# 
# 4050
# 
# - Human3 남편 아내 신랑 마누라 와이프
# - Human7 노인 어머니 어머님 아버지 아버님
# 
# ---------------------------
# 
# - Human4 임산부 수유부
# - Human5 유아 아기 어린이 아이들 
# - Human6 청소년 수험생 고3 입시
# - Human8 직장인

# In[214]:


data = pd.read_excel("비타민제 사용자별로 구별.xlsx", sheet_name = "Human8", names = [i for i in range(6)])


# In[215]:


contents = data[[2]] #Contents
contents_list = list((contents[2].values))


# In[216]:


def removing_typos(a,b,content):
    content[content.index(a):content.index(b)+1] = [''.join(content[content.index(a):content.index(b)+1])]
    return content


# In[217]:


## Removing Typo - "임팩타민" bc of noun extracting
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
    if "로나" in content:
        content[content.index("로나")] = "아로나"
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "아리나" in content:
        if "민" in content:
            content = removing_typos("아리나","민",content)
    if "아로" in content:
        content[content.index("아로")] = "아로나"
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "아로나" in content:
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "아로나" in content:
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "씨" in content:
        if "플러스" in content:
            content = removing_typos("씨","플러스",content)
    if "씨" in content:
        if "플러스" in content:
            content = removing_typos("씨","플러스",content)
    if "회" in content:
        if "복제" in content:
            content = removing_typos("회","복제",content)
    if "액" in content:
        if "넘" in content:
            content = removing_typos("액","넘",content)
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
    if "로나" in content:
        content[content.index("로나")] = "아로나"
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "씨" in content:
        if "플러스" in content:
            content = removing_typos("씨","플러스",content)
    if "씨" in content:
        if "플러스" in content:
            content = removing_typos("씨","플러스",content)
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
    if "로나" in content:
        content[content.index("로나")] = "아로나"
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "씨" in content:
        if "플러스" in content:
            content = removing_typos("씨","플러스",content)
    if "씨" in content:
        if "플러스" in content:
            content = removing_typos("씨","플러스",content)
    if "아로나" in content:
        content[content.index("아로나")] = "아로나민"
    if "플러스" in content:
        content[content.index("플러스")] = "씨플러스"
    if "민씨" in content:
        content.remove("민씨")
    if "것" in content:
        content.remove("것")
    if "아로" in content:
        content[content.index("아로")] = "아로나"
        if "민" in content:
            content = removing_typos("아로나","민",content)
    if "임" in content:
        if "민" in content:
            content = removing_typos("임","민",content)
    if "임" in content:
        if "민" in content:
            content = removing_typos("임","민",content)
    if "임" in content:
        if "민" in content:
            content = removing_typos("임","민",content)
    if "임" in content:
        if "민" in content:
            content = removing_typos("임","민",content)
    if "메" in content:
        if "가트" in content:
            content = removing_typos("메", "가트", content)
    if "영" in content:
        if "양제" in content:
            content = removing_typos("영", "양제", content)
    if "유산" in content:
        if "균" in content:
            content = removing_typos("유산", "균", content)
    if "항산" in content:
        if "화제" in content:
            content = removing_typos("항산","화제",content)
    if "양제" in content:
        content[content.index("양제")] = "영양제"
    if "루" in content:
        if "테이" in content:
            content[content.index("테이")] = "테인"
            content = removing_typos("루","테인",content)
    if "스마트" in content:
        if "브레인" in content:
            content = removing_typos("스마트","브레인",content)
    if ".com" in content:
        content.remove(".com")
    if "것" in content:
        content.remove("것")
    if "수" in content:
        content.remove("수")
    if "등" in content:
        content.remove("등")
    if "때" in content:
        content.remove("때")
    if ".com" in content:
        content.remove(".com")
    if "거" in content:
        content.remove("거")
    if "속눈썹" in content:
        content.remove("속눈썹")
    if "속눈썹" in content:
        content.remove("속눈썹")
    if "속눈썹" in content:
        content.remove("속눈썹")
    if "속눈썹" in content:
        content.remove("속눈썹")
    if "제로" in content:
        content.remove("제로")
    if "씨" in content:
        content.remove("씨")
    if "제로" in content:
        content.remove("제로")
    if "씨" in content:
        content.remove("씨")
    if "제가" in content:
        content.remove("제가")
    if "제가" in content:
        content.remove("제가")
    if "제라" in content:
        content.remove("제라")
    if "제나" in content:
        content.remove("제나")
    if "제의" in content:
        content.remove("제의")
    if "비타민제" in content:
        content.remove("비타민제")
    if "비타민제" in content:
        content.remove("비타민제")
    if "비타민" in content:
        content.remove("비타민")
    if "비타민" in content:
        content.remove("비타민")
    if "오늘" in content:
        content.remove("오늘")
    if "요즘" in content:
        content.remove("요즘")
    if "안녕하세요" in content:
        content.remove("안녕하세요")
    if "배" in content:
        content.remove("배")
    if "곶감" in content:
        content.remove("곶감")    
    if "철" in content:
        if "분" in content:
            content[content.index("분")] = "분제"
            content = removing_typos("철", "분제",content)


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

# In[218]:


def listmaker(content) :
    analyzing_list = []
    words =   ["활력", "잇", "남편", "남성", "직장인", "몸", "눈"] #Keywords based on TF-IDF
    for word in words :
        if word in str(content):
            content = k.nouns(str(content))
            removing_typo(content)
            analyzing_list = content
    return analyzing_list


# In[219]:


lst2 = []
for content in contents_list:
    lst = listmaker(content)
    if lst != []:
        lst2.append(lst)


# In[220]:


import pandas as pd
from mlxtend.preprocessing import TransactionEncoder


# In[221]:


te = TransactionEncoder()
te_ary = te.fit(lst2).transform(lst2)
df = pd.DataFrame(te_ary, columns=te.columns_)


# In[222]:


from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support = 0.05, use_colnames=True)


# In[223]:


from mlxtend.frequent_patterns import association_rules


# In[224]:


rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1, support_only=False)
rules['length'] = rules['antecedents'].apply(lambda x: len(x))
rules['length2'] = rules['consequents'].apply(lambda x: len(x))
rules = rules [ (rules['length'] == 1) &
                   (rules['length2'] == 1) ]
rules


# In[225]:


import openpyxl
rules.to_excel("비타민제 소비자별 연관분석 결과/Vitamin Workers.xlsx")
#Human1 - Vitamin Men Women.xlsx
#Human2 - Vitamin 2030.xlsx
#Human3, 7 - Vitamin 4050.xlsx
#Human4 - Vitmain Pregnant.xlsx
#Human5 - Vitamin Kids.xlsx
#Human6 - Vitamin Examiniees.xlsx
#Human8 - Vitamin Workers.xlsx

