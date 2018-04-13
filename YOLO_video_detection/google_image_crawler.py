# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 02:17:29 2018

@author: Binkowsky
"""

import os
from bs4 import BeautifulSoup as Soup
import urllib.request as ulib
import json


base_url= 'https://www.google.com/search?ei=1m7NWePfFYaGmQG51q7IBg&hl=en&q={}&tbm=isch&ved=0ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ&start={}&yv=2&vet=10ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ.1m7NWePfFYaGmQG51q7IBg.i&ijn=1&asearch=ichunk&async=_id:rg_s,_pms:s'

headers = {'User-Agent': 'Chrome/41.0.2228.0 Safari/537.36'}


def get_links(search_name):
    search_name = search_name.replace(' ', '+') # replace any space with +
    url = base_url.format(search_name, 0) #format the search name into the base_url
    request = ulib.Request(url, None, headers) 
    json_string = ulib.urlopen(request).read()
    page = json.loads(json_string)
    new_soup = Soup(page[1][1], 'lxml')
    images = new_soup.find_all('img')
    links = [image['src'] for image in images] # All the download image links
    return links


def save_images(links, search_name): # save images into a dirctory which is named as the search name
    directory = search_name.replace(' ', '_') #replace any sapce in name with "_"
    if not os.path.isdir(directory):# if the dirctory is not exist
        os.mkdir(directory) # we will make a directory

    for i, link in enumerate(links):
        savepath = os.path.join(directory, '{:06}.png'.format(i))
        ulib.urlretrieve(link, savepath)

search_list=['matt damon', 'matt damon face','matt damon actor',
             'matt damon jason bourne','matt damon pictures',
             'matt damon portrait']


if __name__ == '__main__':
    for i in range(len(search_list)):
        search_name=search_list[i]  ##change the search name each time you search
        links = get_links(search_name) ##because google will ban you, if you do a
        save_images(links, search_name) ## dynamic crawling
        
    print('After collecting six times of data, you will have 600 images.'
          ' Do a manual inspection, delete those images that does not fit'
          ' for a good training model. Then run the gather_all_images.py')
