class YoutubePage:
    videos = ""
    def __init__(self, soup= "", page_type = "none"):
        if(soup != ""):
            self.page_type = page_type
            self.soup = soup
            self.init_videos(soup)

    # Returns list of articles in the form [article1_title, article2_title, ...]
    def init_videos(self, soup):
        self.videos = []
        main_content = soup.find('div', {"id":"contents"})
        for video in main_content.findAll('ytd-rich-item-renderer'):
            video_title = video.find('yt-formatted-string', {'id':'video-title'}).get('aria-label')
            self.videos.append(video_title)