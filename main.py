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
import globals
import voice
import navigation
import nytimes


def init():
    voice.speak("Hello, where would you like to go?")

def test_init():
    navigation.go_to_website("https://www.nytimes.com/")

def run():
    #voice.init_listen()
    while(True):
        print("Listening...")
        #input_string = voice.voice_input
        input_string = voice.get_audio()
        if(input_string == ""):
            break
        elif("exit" in input_string):
            continue
        elif("new york times" in input_string):
            globals.website = "nytimes"
            navigation.go_to_website("https://www.nytimes.com/")
        elif("youtube" in input_string):
            globals.website = "youtube"
            navigation.go_to_website("https://www.youtube.com/")
        elif("back" in input_string):
            navigation.go_back()
        if globals.website == "nytimes":
            if(globals.page_type != "Article"):
                nytimes.parse_page_input(input_string)
            elif(globals.page_type == "Article"):
                nytimes.parse_article_input(input_string)
    globals.driver.quit()

def main():
    globals.init()
    #test_init()
    init()
    run()
    
main()