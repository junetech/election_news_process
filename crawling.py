# -*- coding: utf-8 -*-
#pip3 install bs4 필요
import time
import csv
import requests
from bs4 import BeautifulSoup
from collections import Counter
import sys
import datetime as dt
from konlpy.tag import Twitter
from konlpy.utils import pprint
from konlpy.utils import csvwrite

reload(sys)
sys.setdefaultencoding('utf8')
twitter = Twitter()

def get_url (time, page):
    return 'http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100#&date=' + \
        time.strftime('%Y-%m-%d') + \
        ' 00:00:00&page=' + \
        str(page)

def reply_spider():
    LIMIT_DAY = 2
    PAGE_LIMIT = 2
    day = 1
    page = 1
    time = dt.datetime.now()

    # time = time - dt.timedelta(days = 1)

    # while day < LIMIT_DAY:
    #     page = 1
    #     pressresponse = []
    while day < LIMIT_DAY:
        while page < PAGE_LIMIT:
            url = get_url(time, page)
            crude_page_html = requests.get(url)
            soup_page_html = BeautifulSoup(crude_page_html.text, 'lxml')
            news_list = soup_page_html.findAll("li", {"class" : "_rcount"})
            
            for news in news_list:
                href = news.get('href')
                print(href)

            time = time - dt.timedelta(days = 1)
            page = page + 1

        day = day + 1
        # print(day)



                # pagelimit = int(pagelimit.text[pagelimit.text.find('/') + 1:pagelimit.text.find('건')].replace(',','')) / 10
            
        #     for each_newsarticle in soup_newslistpage.find_all("a", {"class", "go_naver"}):

        #         articlehref = each_newsarticle.get('href')
        #         source_ariticlepage = requests.get(articlehref)
        #         plain_source_articlepage = source_ariticlepage.text
        #         soup_articlepage = BeautifulSoup(plain_source_articlepage,'lxml')

        #         try :
        #             #기사 입력 시간
        #             articletime = soup_articlepage.find("span", {"class", "t11"}).text.encode('UTF-8')
        #         except AttributeError:
        #             print("")
        #         else:
        #             articletitle = soup_articlepage.find("h3", {"id" : "articleTitle"})
        #             print(articletitle)
        #             articletitle = articletitle.text.encode('UTF-8')
        #             articletitle = articletitle.replace("'","")
        #             articletitle = articletitle.replace('"',"")
        #             articletitle = twitter.nouns(articletitle)
        #             for title in articletitle:
        #                 print title.encode('UTF-8')
        #             articlebody = soup_articlepage.find("div", {"id" : "articleBodyContents"})
        #             articlebody = articlebody.text.encode('UTF-8')
        #             # print(articlebody)
        #             articlebody = articlebody.replace("'","")
        #             articlebody = articlebody.replace('"',"")
        #             articlebody = articlebody.replace('function _flash_removeCallback() {}',"")
        #             articlebody = articlebody.replace('// flash 오류를 우회하기 위한 함수 추가',"")
        #             articlebody = twitter.nouns(articlebody)
        #             pressresponse.append([articletitle,articlebody])
            
            # page = page + 1

        # with open('hadoop_' + TYPE + '_'+ time.strftime('%Y-%m-%d') + '.csv','w') as csvfile:
        #     for press in pressresponse:
        #         csvwrite(press, csvfile)


        # day = day + 1
        # time = time - dt.timedelta(days = 1)


reply_spider()
