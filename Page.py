'''
Nicholas Lin
Page.py
4/2/20
'''

class Page:
    headers = []
    headline = ""
    articles = []
    page_type = ""

    def __init__(self, soup, page_type = "none"):
        self.page_type = page_type
        self.soup = soup
        self.init_articles(soup)
        self.init_headers(soup)
        if(page_type == "Home"):
            self.init_headline(soup)

    # Stores headers in dictionary of the form [header_text]
    def init_headers(self, soup):
        self.headers = []
        if(self.page_type == "Home"):
            headers_html = soup.find('div', {"data-testid" : "masthead-mini-nav"})
        elif(soup.find('nav', {"class" : "e1se7h4u0"}) != None):
            headers_html = soup.find('nav', {"class" : "e1se7h4u0"})
        else:
            return
        for header in headers_html.findAll('a'):
            text = header.text
            # link = header['href']
            #self.headers[text] = link.split(".com")[1]
            self.headers.append(text)

    # Returns headline = {headline_text : headline_url_postfix}
    def init_headline(self, soup):
        headline_text = soup.find('span', {'class':'balancedHeadline'}).text
        #headline_link = soup.find('div', {"class":"css-1t1jowt"}).a["href"]
        #self.headline = {headline_text : headline_link}
        self.headline = headline_text

    # Returns list of articles in the form [article1_title, article2_title, ...]
    def init_articles(self, soup):
        self.articles = []
        for article_html in soup.findAll('article'):
            if(article_html.find('h2') != None):
                article_title = article_html.find('h2').text
                #article_link = article_html.a["href"]
                #article = {article_title : article_link}
                self.articles.append(article_title)