
from spider import *
from general import *
from queue import Queue
import threading


PROJECT_NAME = 'new_plugins'
HOME_PAGE = 'https://wordpress.org/plugins/'
DOMAIN_NAME = 'wordpress'
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()

spider(PROJECT_NAME,HOME_PAGE,DOMAIN_NAME)

#Creating multiple spiders for speed up the crawling speed
def create_worker(NUMBER):
    for i in range(NUMBER):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url= queue.get()
        spider.crawling(threading.current_thread(),url)
        queue.task_done()


def create_job():

    for link in file_to_set(QUEUE_FILE):
        queue.put(link)

    queue.join()
    crawl()


def crawl():

    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links))+'in the queue')
        create_job()


create_worker(NUMBER_OF_THREADS)
crawl()
print('finished')


#remain_problem: the web crawler always stucked in request.get method, and cannot figure out the main reason.
#temprary solution: rerun the project, it will start crawling from the previous page


