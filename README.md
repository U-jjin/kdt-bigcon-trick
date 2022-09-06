# 빅콘테스트 퓨처스리그 데이터분석 프로젝트🍊
![title](https://user-images.githubusercontent.com/70012637/188676954-b6676eac-d74d-4522-9665-e9a63819ffc8.png)
### **🍊제주도 음식물 쓰레기양 예측을 통한 배출량 감소 방안 도출🍊**

- 연간 음식물 쓰레기 배출에 대한 환경 오염 문제는 심각해지고 있습니다.<br>
- 특히, 제주도에서 클린하우스 제도를 해결방안으로 도입한 이후에도 음식물 쓰레기 배출량은 현저히 증가하는 추세입니다.<br>
- 빅콘테스트 경진대회 주최측으로부터 제주테크노파크에서 제공받은 4개년 음식물 쓰레기 배출량 관련 데이터 셋을 이용하여 <br>
음식물 배출 증가 현상 요인 분석과 예측 모델 개발을 통한 제주 읍면동별 배출량을 예측하고,<br>
제주도민을 위한 배출량 조회 서비스를 구현하였습니다.

### 프로젝트 일정

<br><br>
## 프로젝트 환경 및 사용 tool🛠
<br>

|    전처리     |                시각화                |       데이터 분석 및 머신러닝       |   배포   |
| :-----------: | :----------------------------------: | :---------------------------------: | :------: |
| Pandas, numpy | Matplotlib, Seaborn, Plotly, Tableau | Sklearn, ARIMA, ETS, forecastHybrid | AWS 예정 |
| DB구축  |    Web Server    |             개발 도구              |          협업 도구           |
| MariaDB | Django ver 3.2.4 | jupyter notebook & Colab & pycharm | Zoom & Google Drive & Github |

<br><br>
## 데이터 셋📲
![제주도 좋다 데이터 셋](https://user-images.githubusercontent.com/70012637/188687475-d0d5179c-1db5-4efa-ac78-58cc73139f10.png)
- 코로나 데이터 : 크롤링 수집
- 제주도관광객입도객현황: key-value의자료구조로api불러오기, 전처리하여활용

<br><br>
## 프로젝트 process📑
### 1. 데이터 전처리
#### 음식물쓰레기데이터NaN처리
|   |    |
|-----|-------|
|![데이터전처리1-음식물쓰레기데이터NaN처리1](https://user-images.githubusercontent.com/70012637/188682419-683f39c2-bb71-45f9-b283-818ace24c7e1.png)|![데이터전처리2-음식물쓰레기데이터NaN처리 2](https://user-images.githubusercontent.com/70012637/188682422-f79e0a06-d8b8-4456-b4fa-6ce33c91ff88.png)|


#### 그외 기타 데이터 NaN처리
|   |   |   |
|-----|-----|-----|
|![데이터전처리3-그외기타데이터NaN처리](https://user-images.githubusercontent.com/70012637/188682424-74b6ce97-6d29-4605-b4b5-937016186617.png)|![데이터전처리4](https://user-images.githubusercontent.com/70012637/188682413-df7be596-0abf-4bb2-93fe-b33e6724e1d5.png)|![데이터전처리5](https://user-images.githubusercontent.com/70012637/188682418-6522cb90-2ddc-490d-800c-ce82d7392794.png)|

#### 모델링 진행전 표준화

|변수 범위 선정|변수 Scaling|
|---|---|
|![모델링1-변수선택모델링](https://user-images.githubusercontent.com/70012637/188684810-4c109508-e0bb-40d4-9b22-9b6fa4be2006.png)|![모델링2-모델링을위한변수Scaling](https://user-images.githubusercontent.com/70012637/188684662-bc30919a-5851-4c08-98d1-333d2d7e22b8.png)|

### 2. 데이터 모델링
#### 중요 변수 선택
| stepwise | DT,RF,xgboost|
|-----|------|
|![모델링3-stepwise](https://user-images.githubusercontent.com/70012637/188684666-f9e9c8f9-9ac6-4b00-81df-462b35196850.png)|![모델링4-변수중요도 DT,RF,xgboost](https://user-images.githubusercontent.com/70012637/188684752-246b3466-5387-4d94-8796-3eb78f8b63cb.png)|
