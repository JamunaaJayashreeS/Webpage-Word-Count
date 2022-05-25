# Python program to find the word count of the webpage using html2text library

from posixpath import split
import requests
from bs4 import BeautifulSoup
from collections import Counter
import html2text
import re
import pandas as pd


def word_count_url(url):

    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")

    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.escape_snob = True
    h.ignore_anchors = True
    result = h.handle(source_code)
    res = re.sub(r'[^\w\s]', '', result)
    count = len(res.split())
    print("The count of given webpage '"+url+"' is " + str(count))
    return count


# Main method - Uncomment the lines to store the output in a dataframe or a excel
if __name__ == '__main__':

    # column_names=["url","word_count"]
    #df = pd.DataFrame(columns = column_names)
    count = 0

    print("Enter the webpage url or a list of webpages separated by ',' below :")
    input = input()

    if(len(input.split(',')) == 1):
        word_count = word_count_url(input)
        #new_row = [input,word_count]
        #df.loc[count] = new_row
        #count = count+1

    elif(len(input.split(',')) > 1):
        for url in input.split(','):
            word_count = word_count_url(url)
            #new_row = [url,word_count]
            #df.loc[count] = new_row
            #count = count+1
        # df.to_excel('word_counter_authors.xlsx')
