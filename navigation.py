'''
Nicholas Lin
navigation.py
4/4/20
'''

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from Article import Article
from Page import Page
from YoutubePage import YoutubePage
from YoutubeVideo import YoutubeVideo
import globals
import voice

def toggle_pause():
    globals.driver.find_element_by_tag_name('body').send_keys('k')

def search(input):
    input = input.replace(" ", "+")
    go_to_website("https://www.youtube.com/results?search_query=" + input)

def update_soup():
    globals.soup = BeautifulSoup(globals.driver.page_source, 'lxml')

def go_to_website(url):
    globals.driver.get(url)
    update()
    prompt()

#TODO: Find a better way of matching link_text to uppercase
def go_to_page(link_text):
    link_text = link_text.strip()
    try:
        elem = globals.driver.find_element_by_link_text(link_text)
        elem.click()
    except Exception as e:
        print(e)
        try:
            elem = globals.driver.find_element_by_link_text(link_text.upper())
            elem.click()
        except Exception as e:
            print(e)
    update()
    prompt()

def go_back():
    globals.driver.execute_script("window.history.go(-1)")
    update()

def update():   
    update_soup()
    update_website_base()
    update_page_type()
    if("nytimes" in globals.website):
        if(globals.page_type == "Article"):
            globals.page = Article(globals.soup)
        else:
            globals.page = Page(globals.soup, globals.page_type)
    elif("youtube" in globals.website):
        if(globals.page_type == "YoutubeVideo"):
            globals.page = YoutubeVideo(globals.soup)
        else:
            globals.page = YoutubePage(globals.soup, globals.page_type)


def update_website_base():
    url = globals.driver.current_url
    globals.website = url.split(".")[1].lower()

def update_page_type():
    url = globals.driver.current_url
    if("nytimes" in url):
        if(url.endswith(".com/")):
            globals.page_type = "Home"
        elif(url.endswith(".html")):
            globals.page_type = "Article"
        else:
            globals.page_type = "Navigation"
    elif("youtube" in url):
        if(url.endswith(".com/")):
            globals.page_type = "YoutubeHome"
        elif("/watch" in url):
            globals.page_type = "YoutubeVideo"
        elif("/channel" in url):
            globals.page_type = "YoutubeChannel"
        elif("/results" in url):
            globals.page_type = "YoutubeResults"
    

def prompt():
    if(globals.website == "nytimes"):
        if (globals.page_type == "Article"):
            voice.speak("The title of this article is " + globals.page.headline)
            voice.speak("Say: \"read me the summary\" or \"read me the article\" to begin.")
        elif (globals.page_type == "Home"):
            voice.speak("You are on the homepage of the New York Times website.")
            if (globals.page.headline != ""):
                voice.speak("The headline is " + globals.page.headline)
            voice.speak("There are " + str(len(globals.page.articles)) + " articles featured on this page.")
        elif (globals.page_type == "Navigation"):
            voice.speak("The featured article in this section is: " + globals.page.articles[0])
            voice.speak("There are " + str(len(globals.page.articles)) + " articles featured on this page.")
    elif(globals.website == "youtube"):
        if(globals.page_type == "YoutubeHome"):
            voice.speak("You are on the homepage of Youtube.")
            voice.speak("There are " + str(len(globals.page.videos)) + " videos featured on this page.")
            voice.speak("Say \"search\" to search for a video.")
        elif(globals.page_type == "YoutubeResults"):
            voice.speak("There are " + str(len(globals.page.videos)) + " featured results.")

