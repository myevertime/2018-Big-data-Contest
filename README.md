# 2018-Yonsei Bigdata Analysis Competition
## Team Aronamin-ing

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
We summarized the analysis below (in Korean) :
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
>	     
>	     held minimum threshold of _support_ as 0.05
>	     
>	     held minimum thresholdl of _lift_ as 0.08
>
>	3) Similarity Analysis
>	3-1) word2vec: word embedding

>	     analyzed similarity between keywords of product name, important features (ex) side effects, smells) and advertisement actors
>
>	4) Sentiment Analysis
>	4-1) KOSAC sentiment dictionary

>	     utilized _Polarity_ dictionary of KOSAC sentiment dictionary


**4. Results**

 4-1. Identify brand images and brand awareness

	produced price score and image score
	if several brands are correlated each other, we grouped them and analyzed differences

 4-2. Identify customers' reactions on past advertisements 

	extracted the data that are related to advertisements 
	conducted similarity analysis by using word2vec on several keywords

 4-3. Strategy of customization
 	
	Categorized prospective customer into 6 groups (ex) Kids, Pregnant women, Students...)
 
 	There were differences of highly-related nutrients between groups, which are important factors when selecting products.
	Also, we examined familiar keywords of each group such as multivitamin and general vitamins

Based on these results, we suggested marketing strategies to a target company
