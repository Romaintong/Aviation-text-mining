# f = open('./xhs-tv9833.csv', 'w', encoding='UTF8', newline='')
#chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\chrometemp"
from selenium.webdriver.chrome.options import Options
import time
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from lxml import etree

def scrolling():
    for i in range(100):
        try:
            if bro.find_element(By.XPATH,"//div[contains(text(),'暂时没有更多评论')]").text:
                break
        except:
            pass
        print(f'-----第{i}次点击页面--------')
        nn = bro.find_element(By.XPATH,"//div[contains(text(),'加载中')]")
        bro.execute_script("arguments[0].scrollIntoView();", nn)
        time.sleep(0.15)
        try:
            element = bro.find_element(By.XPATH,"//div[contains(text(),'展开')]")
            if "回复" in str(element.text) or "更多" in str(element.text):
                element.click()
        except:
            pass
        try:
            if bro.find_element(By.XPATH,"//div[contains(text(),'暂时没有更多评论')]").text:
                break
        except:
            pass

if __name__ == '__main__':
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    bro = webdriver.Chrome(options=options)
    data = bro.page_source
    time.sleep(1)
    '''
    uu = []
    for i in range(1,500):
        try:
            t = '//*[@id="douyin-right-container"]/div[2]/div/div[3]/div[1]/ul/li['+str(i)+']/div/div/a/div/div[2]/div/div[2]/span[2]'
            x = '//*[@id="douyin-right-container"]/div[2]/div/div[3]/div[1]/ul/li['+str(i)+']/div/div/a'
            url = bro.find_element(By.XPATH, x)
            tt = bro.find_element(By.XPATH, t).text
            if tt == "1年前":
                uu.append(url.get_attribute('href'))
                print(tt)
            else:
                pass
        except:
            pass
    print(uu)
    '''
    urls = ['https://www.douyin.com/video/7120850222766411021', 'https://www.douyin.com/video/7115766786108263717', 'https://www.douyin.com/video/7092706720346131719', 'https://www.douyin.com/video/7097117688673160461', 'https://www.douyin.com/video/7125733655883926820', 'https://www.douyin.com/video/7035434870453046541', 'https://www.douyin.com/video/6742788987368393997', 
            'https://www.douyin.com/video/6538408777094270216', 'https://www.douyin.com/video/7022923541834140941', 'https://www.douyin.com/video/6576525878891646216', 'https://www.douyin.com/video/7117784327773080840', 'https://www.douyin.com/video/6964598627503230245', 'https://www.douyin.com/video/6782111516830256391', 'https://www.douyin.com/video/7016622652743781668', 'https://www.douyin.com/video/6749112449795951875', 'https://www.douyin.com/video/6944875706279005470', 
            'https://www.douyin.com/video/6791827372124507407', 'https://www.douyin.com/video/6870832022013660427', 'https://www.douyin.com/video/6955013113276140813', 'https://www.douyin.com/video/6974633918112746760', 'https://www.douyin.com/video/6777205981991439630', 'https://www.douyin.com/video/6882574749269003534', 'https://www.douyin.com/video/6831120854668037387', 'https://www.douyin.com/video/7117828868219718920', 'https://www.douyin.com/video/7076376519618153736', 
            'https://www.douyin.com/video/7112088727849061645', 'https://www.douyin.com/video/6990656068091202846', 'https://www.douyin.com/video/7003700799171857700', 'https://www.douyin.com/video/6967547727425146144', 'https://www.douyin.com/video/6924904985809472779', 'https://www.douyin.com/video/7011118732399365384', 'https://www.douyin.com/video/6854886913795493135', 'https://www.douyin.com/video/6878497635813084420', 'https://www.douyin.com/video/6963420497346317579', 
            'https://www.douyin.com/video/6726682082556398852', 'https://www.douyin.com/video/6562062011885161735', 'https://www.douyin.com/video/6590938479352352013', 'https://www.douyin.com/video/6875971430782209295', 'https://www.douyin.com/video/6806923137045908749', 'https://www.douyin.com/video/7083889323472391424', 'https://www.douyin.com/video/7111639277376638215', 'https://www.douyin.com/video/7063628555556605188', 'https://www.douyin.com/video/7086758739079941411', 
            'https://www.douyin.com/video/7119111372272586019', 'https://www.douyin.com/video/7077771653484154146', 'https://www.douyin.com/video/7068117390143393037', 'https://www.douyin.com/video/7061971127026945295', 'https://www.douyin.com/video/7072335192924392741', 'https://www.douyin.com/video/7103463681672924457', 'https://www.douyin.com/video/6988802703996587300']
    print(len(urls))
    f = open('dy-zfj.csv', 'a', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(["时间","标题","评论","评论时间"])
    for url in urls:
        bro.get(str(url))
        date = bro.find_element(By.XPATH,"//span[contains(text(),'发布时间')]").text
        date = str(date).split('：')[1]
        date = date.split(' ')[0]
        print(date)
        title = bro.find_element(By.XPATH,'//*[@id="douyin-right-container"]/div[3]/div/div[1]/div[3]/div/div[1]/div/h1/span/span[2]/span') 
        #title = bro.find_element(By.XPATH,'//*[@id="douyin-right-container"]/div[3]/main/div[2]/div[2]/h1')
        title = str(title.text)
        print(title)

        if data[0:4] == "2022" or data[0:4] == "2018":
            pl = bro.find_element(By.XPATH,'//*[@id="douyin-right-container"]/div[3]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]')
            pl.click()
            time.sleep(float(random.randint(1, 5) / 12))
            scrolling()
            comment = bro.find_elements(By.CLASS_NAME,"a9uirtCT")
            datee = bro.find_elements(By.CLASS_NAME,"L4ozKLf7")
            l = len(comment)
            for i in range(0,l):
                cc = comment[i].text
                dd = datee[i].text
                new = [cc,dd]
                writer.writerow([date,title,cc,dd])
        else:
            pass
        time.sleep(0.15)
    f.close()
    
    #bro.send_keys(Keys.DOWN)