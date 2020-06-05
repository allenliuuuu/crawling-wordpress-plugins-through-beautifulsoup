import os

#for general operation in creating dir and files
def create_dir(directory):
    if os.path.exists(directory):
        print('the path have been created')

    else:
        print('creating directory:'+directory)
        os.mkdir(directory)


def create_data_file(project_name,base_url):

    queue = os.path.join(project_name,'queue.txt')
    crawled = os.path.join(project_name,'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(file_name,content):
    with open(file_name,'w', encoding="utf-8") as f:
        f.write(content)
    # f=open(file_name,'w')
    # f.write(content)
    # f.close()


def append_to_file(file_name,content):
    with open(file_name, 'a' ,encoding="utf-8") as f:
        f.write(content+'\n')


def delete_file_content(file_name):
    open(file_name, 'w').close()


def file_to_set(file_name):

    res=set()
    with open(file_name, 'rt', encoding="utf-8") as f:
        for line in f:
            res.add(line.replace('\n', ''))
    return res

def set_to_file(set_name, file_name):

    with open(file_name, 'w', encoding="utf-8") as f:
        for l in set_name:
            f.write(l+'\n')







