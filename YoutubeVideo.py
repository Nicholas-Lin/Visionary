'''
Nicholas Lin
video.py
4/2/20
'''

class YoutubeVideo:
    title = ""
    channel = ""
    date = ""
    description = ""
    comments = []
    #num_views = 0

    def __init__(self, video_soup = ""):
        if(video_soup != ""):
            #Set title
            self.title = video_soup.find('h1', {'class':'title'}).text

            #Set channel
            channel_html = video_soup.find('div', {'class':'ytd-channel-name'})
            if(channel_html != None):
                self.channel = channel_html.find('a').text

            #Set date
            date_html = video_soup.find('div', {'id':'date'})
            if(date_html != None):
                self.date = channel_html.find('yt-formatted-string').text

            #Set description
            description_html = video_soup.find('div', {'id':'description'})
            if(description_html != None):
                self.description = description_html.text

            #Set num_views
            #views_html = video_soup.find('span', {'class' : 'view-count'})
            #self.num_views = views_html.text