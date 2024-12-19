from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import csv

#chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\chrometemp"

#  页面滚动
def scrolling():
    for i in range(5000):
        print(f'-----第{i}次点击页面--------')
        note_scroller = bro.find_element(By.CLASS_NAME,"note-scroller")
        #note_scroller = bro.find_element_by_class_name("note-scroller")
        bro.execute_script("arguments[0].scrollBy(0, 200);", note_scroller)
        time.sleep(0.15)
        try:
            element = bro.find_element(By.XPATH,"//div[@class='show-more']")
            #bro.find_element_by_xpath("//div[contains(text(),'展开')]")
            if "回复" in str(element.text):
                element.click()
        except:
            pass
        try:
            if bro.find_element(By.XPATH,"//div[contains(text(),'- THE END -')]").text:
                break
        except:
            pass
        try:
            if bro.find_element(By.XPATH,"//div[@class='no-comments']").text:
                break
        except:
            pass
def save_(title,content,date,url):
    data = bro.page_source
    tree = etree.HTML(data)
    list = tree.xpath('//div[@class="content"]')
    info = tree.xpath('//div[@class="info"]')
    print(len(list), len(info))
    with open('xhs-zfj.csv', 'a', encoding='utf-8') as f:
        row = "链接,发文时间,文章标题,内容,评论时间,评论内容\n"
        f.write(row)
        for i in range(0, len(list)):
            pl = ''.join(list[i].xpath('./text()')).replace('\n', '').replace(',', '')
            times = ''.join(info[i + 2].xpath('./div[1]/span[1]/text()'))
            print(times, pl)
            rows = "{},{},{},{},{},{}".format(url.replace('\n', ''), date, title.replace('\n', ''), content.replace('\n', ''), times, pl)
            f.write(rows)
            f.write('\n')
if __name__ == '__main__':
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    bro = webdriver.Chrome(options=options)
    #bro.get('https://www.xiaohongshu.com/search_result?keyword=MU5735')
    #time.sleep(5)
    data = bro.page_source
    time.sleep(5)
    # f = open('./xhs-tv9833.csv', 'w', encoding='UTF8', newline='')
    count = bro.find_elements(By.XPATH,"//section[@class='note-item']")
    print(len(count))
    if bro.find_elements(By.XPATH,"//section[@class='note-item']/div/a[1]"):
        all = bro.find_elements(By.XPATH,"//section[@class='note-item']/div/a[1]")
        link = [k.get_attribute('href') for k in all]
    bro.execute_script("window.open('about:blank','_blank');")
    all_handles = bro.window_handles
    bro.switch_to.window(all_handles[1])
    for url in link:
        bro.get(str(url))
        title = bro.find_element(By.CLASS_NAME,'title').text
        content = bro.find_element(By.CLASS_NAME,'desc').text
        date = bro.find_element(By.CLASS_NAME,'date').text
        check = str(date)
        if int(check[0:4]) <= 2022:
            scrolling()
            save_(title,content,date,url)
            time.sleep(1)
        else:
            pass

    #if bro.find_elements(By.CLASS_NAME,'title'):
    #    all = bro.find_elements(By.CLASS_NAME,'title')
    #    print(len(all))
    #    for k in all:
    #        print(k.text)
    #scrolling()
    #save_()