from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
from general import *

#get links from the web pages through the beautifulsoup tool
class Link_finder():

    def __init__(self,page_url):

        self.page_url = page_url
        self.links = set()
        self.base_url = 'downloads'
        create_dir('New_plugins')

    def link_finder(self):
        try:
            URl = requests.get(self.page_url, timeout = 5).text
            soup = BeautifulSoup(URl)
            soup.encode('utf-8')
            print('sucess')
        except requests.exceptions.RequestException as e:
            print(e)

        for link in soup.find_all('a',href =True):
            if self.base_url in link['href']:
                self.download_plugins(link['href'])
            self.links.add(link['href'])


    def get_links(self):
        return self.links

    def download_plugins(self,URL):
            dirs = './New_Plugins/'
            file_name = dirs + URL.split('/')[-1]
            urlretrieve(URL, file_name)



