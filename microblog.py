import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
import os
import csv
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

# https://s.weibo.com/weibo?q=mu5735&typeall=1&suball=1&timescope=custom%3A2022-03-21-0%3A2022-05-02-23&Refer=g&page=3

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    #driver.get('https://s.weibo.com/')
    #time.sleep(5)
    #driver.find_element(By.XPATH,'//*[@id="pl_login_form"]/div/div[1]/div/a[2]').click()
    #time.sleep(10)
            
    datee = ["2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2022-05-05",
            "2022-05-06",
            "2022-05-07",
            "2022-05-08",
            "2022-05-09",
            "2022-05-10",
            "2022-05-11",
            "2022-05-12",
            "2022-05-13"]
    ll = len(datee)
    for i in range(0,ll):
        new_url = "https://s.weibo.com/weibo?q=坐飞机&typeall=1&suball=1&timescope=custom%3A"+str(datee[i])+"%3A"+str(datee[i+1])+"&Refer=g&page=1"
        driver.get(new_url)
        f = open('wb-220330-220512-zfj.csv', 'a', encoding='utf-8')
        writer = csv.writer(f)
        writer.writerow(["时间","文本"])
        for i in range(0,50):
            try:
                driver.find_elements(By.PARTIAL_LINK_TEXT,'展开')
                all = driver.find_elements(By.PARTIAL_LINK_TEXT,'展开')
                for k in all:
                    try:
                        k.click()
                    except:
                        pass
            except:
                pass        
            date = driver.find_elements(By.CLASS_NAME,'from')
            txt = driver.find_elements(By.CLASS_NAME,'txt')
            l = len(txt)
            datel = len(date)
            txtl = len(txt)
            for k in range(0,l):
                dd = str(date[k%datel].text).split(" ")[0]
                writer.writerow([dd, txt[k].text])
                
            try: 
                driver.find_element(By.CLASS_NAME,'next')
                next = driver.find_element(By.CLASS_NAME,'next')
                try:
                    next.click()
                except:
                    pass
            except:
                    break
            time.sleep(0.1)

    f.close()