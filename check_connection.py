import urllib.request

def check_connection():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False


