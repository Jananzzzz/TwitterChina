import os
import itertools
import time

proxy = [
    '123.44.55.66:1234',
    '124.135.22.145:2344',
    '222.234.111.211:2133',
    '234.111.1.11:2133',
]

# iterate through the proxy list, each ip for 120 seconds
for i in itertools.cycle(proxy):
    # print(i)
    os.environ['http_proxy'] = f"http://{i}"
    os.environ['https_proxy'] = f"http://{i}"
    time.sleep(120)






def crawl():
    print("asfas")

crawl()