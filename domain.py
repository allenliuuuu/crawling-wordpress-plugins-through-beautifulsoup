from urllib.parse import urlparse



def get_domain_name(url):
    domains = get_sub_domain_name(url)
    return 'wordpress'


def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''