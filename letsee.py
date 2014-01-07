import sys
import pycurl

class ContentCallback:
        def __init__(self):
                self.contents = ''

        def content_callback(self, buf):
                self.contents = self.contents + buf

t = ContentCallback()
curlObj = pycurl.Curl()
curlObj.setopt(curlObj.URL, 'http://tch511915.tch.quora.com/up/chan5-8886/updates?min_seq=36132401&channel=main-w-dep26-4042272742440482018&callback=jsonp1436d282deddb7211c76c2cf')
curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
curlObj.perform()
curlObj.close()
print t.contents
