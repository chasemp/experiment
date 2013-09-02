import urllib2
import os

def request(url, trail):
    req = urllib2.Request(url=url + str(trail))
    return urllib2.urlopen(req).read()

if __name__ == '__main__':

    item = 0
    getid = '12345'
    while isinstance(item, int):
        response = request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=', getid)
        try:
            item = int(response.split()[-1].strip())
        except ValueError:
            print response
            if all(map(lambda i: i in response.lower(), ['divide', 'two'])):
                item = item / 2
            else:
                break
        print item
        getid = item
