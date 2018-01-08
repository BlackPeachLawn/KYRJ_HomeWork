#encoding=utf-8
import requests
import csv
import random
import time
import socket
import http.client
import re
#import urllib.request
from bs4 import BeautifulSoup

download_url = 'http://dianying.nuomi.com/movie/boxoffice'

def download_page(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) Apple WebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
            }
    
    r = requests.get(url, headers=headers)
    r.encoding = 'UTF-8'
    data =r.text
    return data

def parse_html(html):

    soup=BeautifulSoup(html,'lxml')
    movie=[]
    movie_list_soup= soup.find('div',attrs={'class':'detail-container'})
    for l in movie_list_soup.find_all('dd',attrs={'class':'each-movie clearfix'}):
        movie_title=l.find('h5',attrs={'class':'movie-title'}).getText()
        movie_day=l.find('li',attrs={'class':'days'}).getText()
        movie_total=l.find('span').getText()
        movie_today=l.find('div',attrs={'class':'column colm-2'}).getText()
        movie_pfzb=l.find('div',attrs={'class':'column colm-3'}).getText()
        movie_ppzb=l.find('div',attrs={'class':'column colm-4'}).getText()
        movie_szl=l.find('div',attrs={'class':'column colm-5'}).getText()
        movie_pzzb=l.find('div',attrs={'class':'column colm-6'}).getText()
        movie_cc=l.find('div',attrs={'class':'column colm-7'}).getText()
        movie_rc=l.find('div',attrs={'class':'column colm-8'}).getText()
        movie_cjrc=l.find('div',attrs={'class':'column colm-9'}).getText()
        movie_cjsr=l.find('div',attrs={'class':'column colm-10'}).getText()
        movie_pjpj=l.find('div',attrs={'class':'column colm-11'}).getText()
        next_page=l.find('div',attrs={'class':'column colm-1'})
        next_url='http://dianying.nuomi.com'+next_page['to-url']
        movie_details=[]
        movie_details.append(movie_title)
        movie_details.append(movie_day)
        movie_details.append(movie_total)
        movie_details.append(movie_today)
        movie_details.append(movie_pfzb)
        movie_details.append(movie_ppzb)
        movie_details.append(movie_szl)
        movie_details.append(movie_pzzb)
        movie_details.append(movie_cc)
        movie_details.append(movie_rc)
        movie_details.append(movie_cjrc)
        movie_details.append(movie_cjsr)
        movie_details.append(movie_pjpj)
        movie_details.append(next_url)
        movie.append(movie_details)
    return movie
def parse_detail(html):
    soup =BeautifulSoup(html,'lxml')
    detail=[]
    d=soup.find('div',attrs={'class':'info'})
    movie_title=d.find('h4',attrs={'class':'subtitle'}).getText()
    print('电影名：'+movie_title)
    movie_grade=d.find('span',attrs={'class':'nuomi-orange font16 fl num'}).getText()
    print('评分：'+movie_grade)
    dd=d.find('div',attrs={'class':'content'})
    p1=dd.find('p')
    p2=p1.find_next('p')
    print(p2.getText())
    p3=p2.find_next('p')
    p4=p3.find_next('p')
    print('信息：'+p3.getText())
    print(p4.getText())
    detail.append(movie_title)
    detail.append(movie_grade)
    detail.append(p2.getText())
    detail.append(p3.getText())
    detail.append(p4.getText())
    return detail
    

def main():    
   movie_details=parse_html(download_page(download_url))
   with open("movie_details.csv","w",newline='')as csvfile:
       detalimiter='\t' 
       writer=csv.writer(csvfile,dialect='excel')
       list1=["电影名","上映天数","总票房","实时票房","票房占比","排片占比","上座率","排座占比","场次","人次","场均人次","场均收入","平均票价","网址"]
       writer.writerow(list1)
       for i in movie_details:
           writer.writerow(i)
   with open(r"movie_details.csv")as datacs:
       read1=csv.reader(datacs,delimiter=',')
       for j in read1:
           print(j[0])
   with open(r"movie_details.csv")as datacsv:
       read=csv.reader(datacsv,delimiter=',')
       flag=0
       print()
       str=input("请输入你想了解的电影全名：")
       print()
       for i in read:
           if str==i[0]:
               data=download_page(i[13])
               dict1=dict(zip(list1,i))
               for key in dict1.keys():
                   print('{}:           \t{}'.format(key,dict1[key]))
               print()
               detail_mes=parse_detail(data)
               flag=1
       if flag==0:
           print("电影名有误")
if __name__ == '__main__':
    main()
