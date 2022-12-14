# SWE599_Flight_Price_Estimation


#### Flight_Price_Data_Web_Scraping

* Selenium is used for webscraping
* Enuygun website is used
* 14-11-2022/14-12-2022 flights from Istanbul Airport & Sabiha Gökçen Airport to İzmir, Ankara, Antalya, Adana, Bodrum, Dalaman, Trabzon, Gaziantep, Diyarbakır, Hatay, Kars, Erzurum and Mardin destination cities.
* Dataset was collected between 14-10-2022/14-11-2022


#### Combine_Datasets_And_Feature_Extraction

* Flight information were downloaded during 30 days and 30 dataset are merged.
* Dataset consists of 129514 rows.
* Scrapped features: checked_date,company,departure_airport,arrival_airport,departure_time,arrival_time,departure_date,duration,price
* Feature extraction applied.
* Check merged.csv for dataset.
* All Features: 

![image](https://user-images.githubusercontent.com/24697147/207698243-94365157-16c8-44b5-9cd5-8afdf775c475.png)


#### Data_Visualization

* Matplotlib and seaborn libraries are used visualize dataset.
* Remaining days to flight vs price correlation visualized for each destination city.

#### Machine_Learning

* Decision Tree Regressor
* Random Forest Regressor
* KNN Regressor
* Lasso Regressor
* Ridge Regressor
* XGBoost Regressor
* Support Vector Machine

#### Learning to Rank

* XGBRanker model is used to develop recommendation model.
* Price is ranked between 1-10 for each destination city.
* Dataset is grouped by destination city.
* Prediction for each destination city is investigated.

#### Notes:

* Check report folder for code results.
