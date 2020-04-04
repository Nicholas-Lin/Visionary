'''
Nicholas Lin
globals.py
4/4/20
'''

from selenium import webdriver
from Page import Page
from Article import Article

def init():
    global driver, soup, page_type, page, website
    driver = webdriver.Chrome()
    soup = ""
    page_type = ""
    page = Page()
    page = Article()
    website = ""

