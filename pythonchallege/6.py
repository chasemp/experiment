import urllib2
import os
import pickle

def request(url, trail):
    req = urllib2.Request(url=url + str(trail))
    return urllib2.urlopen(req).read()

if __name__ == '__main__':
    res = request('http://www.pythonchallenge.com/pc/def/', 'banner.p')
    print pickle.loads(res)

