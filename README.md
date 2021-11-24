# 2018-Yonsei Bigdata Analysis Competition
## Aronamin-ing 팀

**1. Data Info **

> We were provided a year SNS crawling data which were mainly about vitamin reviews
> SNS involved Facebook, Instagram, Naver Blog, Naver Cafe, Daum Blog, Daum Cafe, and Youtube

Data Count per Brands
	- Aronamin Gold : 3,238 | Aronamin C+ : 1,118건 | Urusa : 12,330 | Impactamin : 3,099 | Centrum : 11,359
	- Vitamins : 29,736, Nutrient Supplements : 56,959
	
Data Sample
| SNS | Title | Contents | Address | Date |
| ------------ | ------------- | ------------- | ------------- | ------------- |
|naver_blog | 찬찬약사.. | 아로나민 골드, 아로나민 씨플러스 많이 들어보셨죠?? ... | https://blog.naver.com/... | 2017#### |



**2. Preprocessing**
>
>We removed Youtube because the data only contained URL and title of video, which are insufficient to analyze solid reviews.
>
>We put the most priority on the subjectivity of reviews.
>We classified reviews based on subjectivity of contents.

	1) Official Advertisement
	   Contents that the compnay voluntarily advertise their products through Facebook or official blogs
	   
	2) Unofficial Advertisement
	   Contents that certain customer or middleman to advertise
	   Removed ambiguous ones by visiting direct URL and reviewing real contents
	   ex) 'Hot-deal', 'Coupang', 'Group purchase'
	   
	3) Duplicates
	   Instagram Repost or Twitter Retweet


2-1. **Simple analysis of brand impages after preprocessing**
>>We summarized the analysis below (in Korean) :
https://docs.google.com/document/d/1j9fo8MiQO1yc5b-gLkDuwctuijfbbv4xHG0MZNV4y2g/edit?usp=sharing



**3. Analysis**
>	1) Frequency analysis
>	1-1) Wordcloud: visualize based on simple token counts
>	1-2) TFIDF
>
>	2) Association Rules
>	2-1) Apriori Association Rules
>
>	     utilized _nims jupyter_ and _Comoran Tokenizer_ on preprocessed data to tokenize nouns
>	     held minimum threshold of _support_ as 0.05
>	     held minimum thresholdl of _lift_ as 0.08
>
>	3) Similarity Analysis
>	3-1) word2vec: word embedding

>		how it works: 문장에서 같은 위치에 등장하는 단어들, 일정한 크기의 model의 창 안에 동시에 등장하는 단어들은
>		맥락을 공유하고, 결과적으로 유사한 의미를 가질 것
>		what we did: '제품명', '비타민제 시장에서 중요한 특성들(부작용, 피곤, 냄새 등)', '광고모델명' 등의
>		키워드를 중심으로 단어들 간의 유사도를 알아보았습니다.
>
>	4) Sentiment Analysis
>	4-1) KOSAC sentiment dictionary

>		KOSAC sentiment dictionary 중 Polarity 감성사전을 수정해 사용하였습니다. ngrams 중 어간과 형용사를 사용하였고 
>		‘피로‘, ‘개운’등 영양제/비타민 시장의 핵심 감성어를 커스텀 사전에 추가하였습니다. 토크나이징한 자료와 감성사전의 
>		단어를 매치하여 긍정 형태소에 +1, 부정 형태소에 -1, 중립/양립 형태소에 0의 값을 부여하였습니다. 
>		문장이 형태소 분석기로 쪼개져, 그 중 감성사전의 감성어가 등장하면 감성어가 몇 개 쓰였는지 순위를 매기고, 
>		크롤링 자료에 함께 주어졌던 날짜 데이터를 활용하여 월별 긍정형태소, 부정형태소의 개수를 그래프로 나타내었습니다.


**4. 주제별 분석**

 4-1. 경쟁 제품 대비 아로나민 브랜드 이미지와 소비자의 인식 파악

	감성분석 가격점수와 이미지점수를 산출하여 각 브랜드끼리 유사한 경우 Grouping하여 각 그룹간의 차이점 분석

 4-2. 아로나민 광고에 대한 소비자의 반응 파악 (과거 광고의 재고)

	아로나민 제품별로 '광고'와 관련된 감성분석 
	키워드를 중심으로 어떤 연관어들이 있는지를 분석후, word2vec을 통해 유사도 분석

 4-3. SNS 고객세분화 전략
 
	연관분석과 Word2Vec을 통해 시장세분화 분석
	
	- 가장 상위 계층(Human1)은 남성과 여성
	
	- 그 다음 하위 계층은 2030, 4050으로 세대별로 구분
	
	- 2030(Human2) 키워드 ‘남친 여친 남자친구 여자친구 연인’
	
	- 4050은 두 집단으로 분류하였는데, ‘남편 아내 신랑 마누라 와이프’(Human3)
	
	- ‘노인 어머니 어머님 아버지 아버님’(Human7)
	
	- 마지막으로 특정 계층별 소비자를 구분했습니다.
	
	- 우리나라만이 가지고 있는 특정 계층으로 수험생(Human6)을 추가, 키워드 기준은 ‘청소년 수험생 고3 입시’
	
	- Human4는 ‘임산부 수유부’
	
	- Human5는 유아 (키워드; 유아 아기 어린이 아이들)
	
	- Human8은 ‘직장인’을 키워드로 분류

 	분석 결과 각 계층별로 연관성이 높은 영양 성분이 달랐고, 제품을 선택할 때 주로 어떤 경로를 거치는지 확인할 수 있었습니다. 
	유사한 단어(종합 비타민, 멀티 비타민) 중에서도 어떤 단어가 각 세대에게 더 친숙한지도 파악할 수 있었습니다.

이하 분석결과를 바탕으로 아로나민측에게 아로나민의 마켓팅 전략을 세 가지 제시하였습니다.

