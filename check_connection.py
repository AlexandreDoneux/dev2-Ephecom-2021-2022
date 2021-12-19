import urllib.request


def check_connection():

    try:
        urllib.request.urlopen('https://www.google.be/')
        return True
    except:
        return False

    """
    urllib.request.urlopen('https://www.google.be/')
    return True
    """

if __name__ == "__main__":
    print(check_connection())
