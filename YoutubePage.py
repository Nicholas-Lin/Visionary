class YoutubePage:
    videos = []
    def __init__(self, soup= "", page_type = "none"):
        if(soup != ""):
            self.page_type = page_type
            self.soup = soup
            if page_type == "YoutubeHome":
                self.init_home(soup)
            if page_type == "YoutubeResults":
                self.init_results(soup)

    def init_results(self, soup):
        self.videos = []
        video = []
        main_content = soup.find('div', {"id":"contents"})
        main_content = main_content.find('div', {"id":"contents"})
        '''
        shelf_content = soup.find('ytd-shelf-renderer')
        if(shelf_content != None):
            print("Found shelf")
            main_content = shelf_content.append(main_content)
        '''
        for video_html in main_content.findAll('ytd-video-renderer'):
            video_title = video_html.find('a', {'id':'video-title'}).text
            video_channel = video_html.find('ytd-channel-name', {'id':'channel-name'}).find('a').text
            video_views_html = video_html.find('div', {'id':'metadata-line'})
            video_views = video_views_html.find('span').text
            video_views = video_views.replace('M', ' million')
            video_views = video_views.replace('K', ' thousand')
            if( "ago" in video_views):
                video_views = "posted " + video_views
            else:
                video_views = "with " + video_views
            video.append(video_title)
            video.append(video_title + " posted by " + video_channel + " " + video_views)
            self.videos.append(video)
            video = []

    def init_home(self, soup):
        self.videos = []
        video = []
        main_content = soup.find('div', {"id":"contents"})
        for video_html in main_content.findAll('ytd-rich-item-renderer'):
            try:
                video_title = video_html.find('a', {'id':'video-title-link'}).text
            except:
                print()
            video_channel = video_html.find('ytd-channel-name', {'id':'channel-name'}).find('a').text
            video_views_html = video_html.find('div', {'id':'metadata-line'})
            video_views = video_views_html.find('span').text
            video_views = video_views.replace('M', ' million')
            video_views = video_views.replace('K', ' thousand')
            if( "ago" in video_views):
                video_views = "posted " + video_views
            else:
                video_views = "with " + video_views

            video.append(video_title)
            video.append(video_title + " posted by " + video_channel + " " + video_views)
            self.videos.append(video)
            video = []