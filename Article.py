class Article:
    headline = ""
    authors = []
    date = ""
    summary = ""
    body_text = ""

    def __init__(self, article_soup):
        #Set headline
        self.headline = article_soup.find('h1', {'itemprop':'headline'}).text

        #Set authors
        author_html = article_soup.find('p', {'itemprop':'author'})
        if(author_html != None):
            for author in author_html.find('span', {'itemprop' : 'name'}):
                self.authors.append(author)

        #Set date
        self.date = article_soup.find('time').text

        #Set summary
        if(article_soup.find('p', {'id':'article-summary'}) != None):
            self.summary = article_soup.find('p', {'id':'article-summary'}).text

        #Set body_text
        section_html = article_soup.find('section', {'name' : 'articleBody'})
        paragraphs = section_html.findAll('p')
        for paragraph in paragraphs:
            self.body_text += " " + paragraph.text

            
