import requests
from bs4 import BeautifulSoup
# import selectors
def update_header(referer):
    header['Referer'] = '{}'.format(referer[:-4])
    return header
url = 'http://www.mmjpg.com/'
# def information(url):
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
                         'Referer':'http://www.mzitu.com'}
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mmjpg.com/mm/1500/2'}
parser = 'html.parser'
preview_pages = 3
for now_page in range (2,preview_pages+1):
    new_url = url+'home/'+str(now_page)
    now_page_infor = requests.get(new_url,headers = header)
    now_page_infor.encoding = 'utf-8' #解决get乱码
    soup = BeautifulSoup(now_page_infor.text,parser) #相当于把内容变成字典
    the_package = soup.find('ul').find_all('a',target="_blank")[1::2] #截取指定位置的信息
    for the_link in the_package: #与下一行一起列出href的内容
        link = the_link['href']
        link = requests.get(link,headers=header)
        link.encoding = 'utf-8'
        soup = BeautifulSoup(link.text,parser)
        the_all = soup.find('div',class_='page').find_all('a') #为了找出所有需要的图片的网址
        for each_pic in the_all:
            add_link = each_pic['href']
            each_url = url+add_link  #还原一个完整的url，是所有需要的图片
            print(each_url)
            # update_header(each_url)
            each_url_infor = requests.get(each_url,headers=header)
            each_url_infor.encoding = 'utf-8'
            soup = BeautifulSoup(each_url_infor.text,parser)
            pics_text = soup.find('div',class_='content').find_all('img') #列出所有需要图片的text
            # print(pics_text)
            # break
            for each_pic_text in pics_text:
                each_pic_link = each_pic_text['src']
                # print(each_pic_link)
                update_header(each_url) #each_url是每个图片的referer
                pic_name = each_pic_link.split('/')[-1]
                f = open('pic\\'+pic_name,'wb') #开始准备下载
                f.write(requests.get(each_pic_link,headers=header).content)
                f.close()
                exit()
print('下载完成')



