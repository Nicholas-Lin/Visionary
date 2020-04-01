import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import playsound

from Article import Article
from Page import Page
import voice

def get_soup():
    soup = BeautifulSoup(driver.page_source, 'lxml')
    return soup


def go_to_page(link_text):
    elem = driver.find_element_by_link_text(link_text)
    elem.click()
    global soup, page
    soup = get_soup()
    page = Page(soup, page_type)


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


def read_headers(headers):
    output = ""
    for header in headers:
        output += header + ", "
    print(output)


def read_articles(articles):
    output = ""
    counter = 1
    for article in articles:
        output += str(counter) + ". " + article + "\n"
        counter += 1
    print(output)

def go_back():
    driver.execute_script("window.history.go(-1)")
    global soup, page, page_type
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
    global driver, soup, page, page_type
    driver = webdriver.Chrome()
    url = "https://www.nytimes.com"
    driver.get(url)
    soup = get_soup()
    page_type = "Home"
    page = Page(soup, page_type)

def run():
    global page_type
    WAKE = "computer"

    print("Listening...")
    input_string = voice.get_audio()
    while(True):
        if input_string.count(WAKE) > 0:
            while(True):    
                    print("Activated...")
                    playsound.playsound("activation_beep.mp3")
                    input_string = voice.get_audio()

                    if("exit" in input_string):
                        break
                    elif("back" in input_string):
                        go_back()
                    elif(page_type != "Article"):
                        parse_page_input(input_string)
                    else:
                        parse_article_input(input_string)
            break

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
        elif("article" in input_string):
            print(page.body_text)
        else:
            print("Sorry that item was not found")
    elif("who" in input_string):
        print(page.authors[0])
    elif("when" in input_string or "date" in input_string):
        print(page.date)
    else:
        print("Sorry, this feature is not supported.")

def main():
    global driver, soup, page_type, page
    init()
    run()

main()
