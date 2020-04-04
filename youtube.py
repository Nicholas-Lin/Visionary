'''
Nicholas Lin
youtube.py
4/2/20
'''

from Article import Article
from Page import Page
import globals
import navigation
import voice

def parse_page_input(input_string):
    if("read" in input_string):
            if("header" in input_string):
                read_headers(globals.page.headers)
            elif("article" in input_string):
                read_articles(globals.page.articles)
            elif("headline" in input_string and globals.page_type == "Home"):
                print(globals.page.headline)
            else:
                print("Sorry that item was not found")
    elif("go" in input_string ):
        if("article" in input_string):
            globals.page_type = "Article"
            if("first" in input_string):
                navigation.go_to_page(globals.page.articles[0])
            elif("second" in input_string):
                navigation.go_to_page(globals.page.articles[1])
            elif("third" in input_string):
                navigation.go_to_page(globals.page.articles[2])
        else:
            for header in globals.page.headers:
                globals.page_type = "Navigation"
                if(header.lower() in input_string):
                    navigation.go_to_page(header)
                    break
    else:
        print("Sorry, this feature is not supported.")


def read_headers(headers):
    output = ""
    for header in headers:
        output += header + ", "
    
    voice.speak(output)

def read_articles(articles):
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
            output += articles[i] + ". "
        voice.speak(output)
    else:
        return

