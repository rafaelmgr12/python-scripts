
import logging
from urllib2 import urlopen
from threading import Thread
from json import JSONDecoder

# Define a crawl function that retrieves data from a url and places the result in results[index]
# The 'results' list will hold our retrieved data
# The 'urls' list contains all of the urls that are to be checked for data
results = [{} for x in urls]


def crawl(url, result, index):
    # Keep everything in try/catch loop so we handle errors
    try:
        data = urlopen(url).read()
        logging.info("Requested..." + url)
        result[index] = data
    except:
        logging.error('Error with URL check!')
        result[index] = {}
    return True

# create a list of threads
threads = []
# In this case 'urls' is a list of urls to be crawled.
for ii in range(len(urls)):
    # We start one thread per url present.
    process = Thread(target=crawl, args=[urls[ii], result, ii])
    process.start()
    threads.append(process)

# We now pause execution on the main thread by 'joining' all of our started threads.
# This ensures that each has finished processing the urls.
for process in threads:
    process.join()

# At this point, results for each URL are now neatly stored in order in 'results'
