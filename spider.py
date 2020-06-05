
from domain import *
from general import *
from link_finder import *
from urllib.request import urlretrieve


# URL = 'https://wordpress.org/plugins/classic-editor/'
# html =requests.get(URL).text
#
#
# soup = BeautifulSoup(html,features='lxml')
# lis = soup.find_all('li')
#
# base_url = 'downloads'
# create_dir('New_Plugins')
# with open('all_new_plugins.txt','a') as f:
#
#     for line in soup.find_all('a', href = True):
#
#         if base_url in line['href']:
#             dirs = './New_Plugins/'
#             name =dirs + line['href'].split('/')[-1]
#             urlretrieve(line['href'],name)

#create spider for crawling contents from the target website
class spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()


    def __init__(self,project_name, base_url, domain_name):

        spider.project_name = project_name
        spider.base_url = base_url
        spider.queue = set()
        spider.crawled = set()
        spider.queue_file = project_name+'\queue.txt'
        spider.crawled_file = project_name+'\crawled.txt'
        spider.domain_name = domain_name

        spider.boot()
        spider.crawling('first_spider', spider.base_url)

#set up the main word file and prepare for starting crawling
    @staticmethod
    def boot():
        create_dir(spider.project_name)
        create_data_file(spider.project_name,spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)
#start crawling the page,put the finded url to the waiting list(queue),and remove scrawled url from the queue
    @staticmethod
    def crawling(crawling_name, page_url):
        if page_url not in spider.crawled:
            print(str(crawling_name)+'now crawling'+page_url)
            print('queue'+str(len(spider.queue))+'|crawled'+str(len(spider.crawled)))
            spider.add_link_to_queue(spider.gather_links(page_url))
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.update_file()


    @staticmethod
    def add_link_to_queue(links):

        for link in links:
            if link in spider.queue or link in spider.crawled:
                continue
            if spider.domain_name not in link:
                continue
            spider.queue.add(link)

    @staticmethod
    def gather_links(page_url):
        try:
            linkfinder = Link_finder(page_url)
            linkfinder.link_finder()

        except:
            return set()

        return linkfinder.get_links()

    @staticmethod
    def update_file():
        set_to_file(spider.queue,spider.queue_file)
        set_to_file(spider.crawled,spider.crawled_file)
























