import requests
from bs4 import BeautifulSoup
    #  -*- coding: utf-8 -*-
    #  -*- chcp 65001 -*-
def web_scraper(loc,base_url,file_path):
    base_url = 'https://www.yelp.co.uk/search?find_desc=&find_loc='
    loc='Newport+Beach,+CA'
    current_page=0
    while current_page<201:
        print(current_page)
        url=base_url+loc+"&start="+str(current_page)
        yelp_r=requests.get(url)
        yelp_soup=BeautifulSoup(yelp_r.text,'html.parser')
        businesses=yelp_soup.findAll('div',{'class':'biz-listing-large'})
        file_path="D:\Python\Pycharm\Scraping-{loc}.txt".format(loc=loc)
        with open(file_path,"a") as textfile:
            businesses=yelp_soup.findAll('div',{'class':'biz-listing-large'})
            for biz in businesses:
                print(biz)
                title=biz.findAll('a',{'class':'biz-name'})[0].text
                print(title)
                second_line=""
                first_line=""
                try:
                    address=biz.findAll('address')[0].contents
                    for item in address:
                        if "br" in str(item):
                            second_line+=item.getText().strip(" \n\t\r")
                        else:
                            first_line=item.strip(" \n\t\r")
                    print(first_line)
                    print(second_line)
                except:
                    pass
                    print("\n")
                    phone=biz.findAll('span',{'class':'biz-phone'})[0].getText().strip(" \n\t\r")
                    print(phone)
                    page_line="{title}\n{address_1}\n{address_2}\n{phone}\n\n".format(
                    title=title,
                    address_1=first_line,
                    address_2=second_line,
                    phone=phone
                    )
                    textfile.write(page_line)
            current_page+=10
(web_scraper(loc='Newport+Beach,+CA',base_url='https://www.yelp.co.uk/search?find_desc=&find_loc=',file_path="D:\Python\Pycharm\Scraping-{loc}.txt"))
