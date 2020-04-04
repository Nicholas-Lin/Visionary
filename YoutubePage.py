class YoutubePage:
    page_type = ""

    def __init__(self, soup= "", page_type = "none"):
        if(soup != ""):
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
        if(soup.find('div', {'class':'css-1t1jowt'}) != None):
            headline_html = soup.find('div', {'class':'css-1t1jowt'})
            headline_text = headline_html.find('span').text
            self.headline = headline_text
        else:
            self.headline = ""
        #headline_link = soup.find('div', {"class":"css-1t1jowt"}).a["href"]
        #self.headline = {headline_text : headline_link}
        

    #TODO: Make sure all articles are actually articles
    # Returns list of articles in the form [article1_title, article2_title, ...]
    def init_articles(self, soup):
        self.articles = []
        if soup.find('section', {"data-testid":"block-Briefings"}):
            soup.find('section', {"data-testid":"block-Briefings"}).decompose()

        for article in soup.findAll('article'):
            article_html = article.find('h2')
            if(article_html != None):
                if(article_html.find('span') != None):
                    article_title = article_html.find('span').text
                else:
                    article_title = article_html.text
                #article_link = article_html.a["href"]
                #article = {article_title : article_link}
                self.articles.append(article_title)