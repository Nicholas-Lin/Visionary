'''
Nicholas Lin
finder.py
4/2/20
'''

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import playsound
import time

from Article import Article
from Page import Page
import voice

def get_soup():
    soup = BeautifulSoup(driver.page_source, 'lxml')
    return soup

def go_to_website(url):
    global driver
    driver.get(url)
    update()

#TODO: Find a better way of matching link_text to uppercase
def go_to_page(link_text):
    try:
        elem = driver.find_element_by_link_text(link_text)
    except Exception as e:
        print(e)
        try:
            elem = driver.find_element_by_link_text(link_text.upper())
        except Exception as e:
            print(e)
    
    elem.click()
    update()

def go_to_article(link_text):
    elem = driver.find_element_by_link_text(link_text)
    elem.click()
    global soup, page
    soup = get_soup()
    page = Article(soup)
    prompt()


def prompt():
    if (page_type == "Article"):
        print(page.headline)
        voice.speak(page.headline)
    elif (page_type == "Home"):
        print(page.headline)
        voice.speak("The headline is " + page.headline)


def read_headers(headers):
    output = ""
    for header in headers:
        output += header + ", "
    
    voice.speak(output)
    print(output)


def read_articles(articles):
    output = ""
    counter = 1
    for article in articles:
        output += str(counter) + ". " + article + "\n"
        counter += 1
    print(output)

    output = "The first three articles are:"
    for i in range (3):
        if (i == 2):
            output += articles[i] + ". "
        else:
            output += articles[i] + ". The next article is "

    output += "Would you like to hear the rest?"
    voice.speak(output)
    continue_listing = voice.get_audio()
    if "yes" in continue_listing:
        output = ""
        for i in range (3, len(articles)):
            output += article + ". "
        voice.speak(output)
    else:
        return


def go_back():
    driver.execute_script("window.history.go(-1)")

def update():   
    global soup, page
    soup = get_soup()
    update_page_type()
    if(page_type == "Article"):
        page = Article(soup)
    else:
        page = Page(soup, page_type)
    
    prompt()

def update_page_type():
    global page_type
    url = driver.current_url
    if(url.endswith(".com/")):
        page_type = "Home"
    elif(url.endswith(".html")):
        page_type = "Article"
    else:
        page_type = "Navigation"

def init():
    voice.speak("Hello, where would you like to go?")
    global driver
    driver = webdriver.Chrome()

def run():
    global page_type
    #voice.init_listen()
    while(True):
        print("Listening...")
        #input_string = voice.voice_input
        input_string = voice.get_audio()
        if("exit" in input_string):
            break
        elif(input_string == ""):
            continue
        elif("new york times" in input_string):
            go_to_website("https://www.nytimes.com/")
        elif("back" in input_string):
            go_back()
        elif(page_type != "Article"):
           parse_page_input(input_string)
        elif(page_type == "Article"):
            parse_article_input(input_string)
    driver.quit()


def parse_page_input(input_string):
    global page_type
    if("read" in input_string):
            if("header" in input_string):
                read_headers(page.headers)
            elif("article" in input_string):
                read_articles(page.articles)
            elif("headline" in input_string and page_type == "Home"):
                print(page.headline)
            else:
                print("Sorry that item was not found")
    elif("go" in input_string ):
        if("article" in input_string):
            page_type = "Article"
            if("first" in input_string):
                go_to_article(page.articles[0])
            elif("second" in input_string):
                go_to_article(page.articles[1])
            elif("third" in input_string):
                go_to_article(page.articles[2])
        else:
            for header in page.headers:
                page_type = "Navigation"
                if(header.lower() in input_string):
                    go_to_page(header)
                    break
    else:
        print("Sorry, this feature is not supported.")

def parse_article_input(input_string):
    if("read" in input_string):
        if("summary" in input_string):
            print(page.summary)
            voice.speak(page.summary)
        elif("article" in input_string):
            print(page.body_text)
            #TODO: Find a way to better output the article
            voice.speak(page.body_text)
        else:
            print("Sorry that item was not found")
            voice.speak("Sorry that item was not found")
    elif("who" in input_string):
        #TODO: only prints first author if there is one. Might break if no authors
        print(page.authors[0])
        voice.speak("The author is " + page.authors[0])
    elif("when" in input_string or "date" in input_string):
        print(page.date)
        voice.speak("This article was published on " + page.date)
    else:
        print("Sorry, this feature is not supported.")

def main():
    global driver, soup, page_type, page
    init()
    run()
    
main()