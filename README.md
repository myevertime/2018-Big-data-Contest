# 2018-Bigdata-Contest
Yonsei University YBE
한국어 감정 어휘 목록



이 어휘 목록은 KOSAC 데이터를 한국어 감정 분석 연구에 폭넓게 활용할 수 있도록 형태소 단위의 감정 특성을 제공하는 것을 목적으로 한다. 여기서는 어휘의 감정 특성이 그 어휘를 포함하는 핵심 주관 표현(이하 Seed)의 감정 특성에서 도출될 수 있다고 가정하고, Seed에서 추출한 형태소 N-그램을 어휘 표제어로 삼았다. 단, 한 Seed가 다른 Seed를 포함하는 경우 상위 Seed가 하위 Seed를 인용하거나 부정하거나 강조하는 등의 방식으로 감정 특성값을 전환할 수 있으므로, 일관된 감정 특성값을 얻기 위해 다른 Seed와 중첩되지 않는 최하위 Seed에 포함된 형태소만을 사용하였다. 형태소 N-그램은 가능한 모든 것을 뽑되 한글 이외의 문자나 문장 부호가 포함된 것은 제외하였다. 여섯 가지 의미 특성의 종류 및 값의 설명은 KOSAC V 1.0 README 파일에서 볼 수 있다. 



lexicon.zip에 포함된 csv 파일 여섯 개는 각각 의미 특성 하나에 해당하며, 위에서 서술한 방식으로 얻은 형태소 N-그램 표제어 16,362개(유니그램 3,476개, 바이그램 6,579개, 트라이그램 6,307개)가 가지는 의미 특성값들의 분포로 구성되어 있다. 파일 내에서 각 행은 하나의 N-그램의 감정 특성을 가리킨다. 열에 해당하는 값의 의미는 순서대로 다음과 같다.



	- ngram: 표제어 N-그램을 이루는 형태소

	- freq: 해당 N-그램을 포함하는 Seed의 개수

	- (의미 특성값): 해당 N-그램을 포함하는 Seed 중 이 값을 가지는 것들의 비율

	- max.value: 가장 높은 비율을 차지하는 값의 이름

	- max.prop: 가장 높은 비율의 수치
