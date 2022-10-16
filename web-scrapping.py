from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as selexcept
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging


# Pandas imports using Pandas for structuring our data
import pandas as pd
from datetime import datetime
import os
import os.path
from os import path
import re
import sys
import glob
import time
import boto3

client = boto3.client("s3")
# date_list = pd.date_range(start='14.11.2022',end='14.12.2022').strftime('%d.%m.%Y').tolist()

# airports=[["izmir", "adnan-menderes-havalimani","adb"],
#           ["ankara", "esenboga-havalimani","esb"],
#           ["antalya","havalimani","ayt"],
#           ["adana","sakir-pasa-havalimani","ada"],
#           ["bodrum","milas-havalimani","bjv"],
#           ["dalaman","havalimani","dlm"],
#           ["trabzon","havalimani","tzx"],
#           ["gaziantep","oguzeli-havalimani","gzt"],
#           ["diyarbakir","havalimani","diy"],
#           ["hatay","havalimani","hty"],
#           ["kars","havalimani","ksy"],
#           ["erzurum","havalimani","erz"],
#           ["mardin","havalimani","mqm"],
# ]

date_list = pd.date_range(start='14.11.2022',end='15.11.2022').strftime('%d.%m.%Y').tolist()

airports=[["izmir", "adnan-menderes-havalimani","adb"],
          ["ankara", "esenboga-havalimani","esb"],          
]

URLs=[]
for date_len in range(0,len(date_list)):
    for dep in range(0,len(airports)):
        url= "https://www.enuygun.com/ucak-bileti/istanbul-"+ airports[dep][0]+"-"+airports[dep][1]+"-ista-"+airports[dep][2]+"/?gidis="+date_list[date_len]+"&yetiskin=1&sinif=ekonomi&aktarmasiz=1&save=1&geotrip=domestic&trip=domestic"
        URLs.append(url)

count=0
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
options.headless = True
options.add_argument("--no-sandbox")
df = pd.DataFrame()

for num in range(0,len(URLs)):
    #run driver on Chrome
    try:
        with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options) as driver:
            driver.get(URLs[num])
            print("Running for url: {}".format(URLs[num]))
            
            time.sleep(2)
        
            #get flights
            flights= driver.find_elements(By.CLASS_NAME, "flight-summary-infos")
            flights_list=[]
            print(driver.title)
            #push each flight info to flights_list
            for flight in flights: 
                print("Start checking for ")

                checked_date=datetime.now().strftime("%d/%m/%Y %H:%M")
                company= flight.find_elements(By.CLASS_NAME, "summary-marketing-airlines")[0].text
                departure_airport= flight.find_elements(By.CLASS_NAME, "itemAirport")[0].text
                arrival_airport= flight.find_elements(By.CLASS_NAME, "itemAirport")[2].text
                departure_time= flight.find_elements(By.CLASS_NAME, "flight-departure-time")[0].text
                arrival_time= flight.find_elements(By.CLASS_NAME, "flight-arrival-time")[0].text
                departure_date= flight.find_elements(By.XPATH, "//*[@id='SearchRoot']/div/div[1]/div/div[1]/div")[0].text.split('|')[1]
                duration= flight.find_elements(By.XPATH, "//*[@id='SearchRoot']/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[3]/div[2]/span")[0].text
                price= flight.find_elements(By.CLASS_NAME, "money-int")[0].text + flight.find_elements(By.CLASS_NAME, "money-decimal")[0].text

                flight_item={
                    'checked_date':checked_date,
                    'company':company,
                    'departure_airport':departure_airport,
                    'arrival_airport': arrival_airport,
                    'departure_time': departure_time,
                    'arrival_time': arrival_time,
                    'departure_date':departure_date,
                    'duration': duration,
                    'price':price,
                }
                print("Item:")
                print(flight_item)
                flights_list.append(flight_item)
            df = df.append(flights_list, ignore_index=True)
                # close browser

    except Exception as e:
        logging.error(e, exc_info=True)
        pass    

#convert dataframe
file_path = 'dataset/{}.csv'.format(datetime.now().strftime("%d-%m-%Y %H:%M"))
#save to local file
if not path.exists('dataset'):
    print("Creating Dataset Folder")
    os.mkdir('dataset')

print("Found flight count {}".format(df.count()))
df.to_csv(file_path, index = True, header=True)
print("Uploading s3")
client.upload_file(file_path, "ertugoguz", "")