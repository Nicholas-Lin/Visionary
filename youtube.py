'''
Nicholas Lin
youtube.py
4/2/20
'''

from YoutubePage import YoutubePage
import globals
import navigation
import voice

def parse_page_input(input_string):
    if("play" in input_string or "go" in input_string):
        if("first" in input_string):
            navigation.go_to_page(globals.page.videos[0][0])
        elif("second" in input_string):
            navigation.go_to_page(globals.page.videos[1][0])
        elif("third" in input_string):
            navigation.go_to_page(globals.page.videos[2][0])
    elif("list" in input_string or "what video" in input_string or "results" in input_string):
        list_videos(globals.page.videos)
    elif("search" in input_string):
        youtube_search()
    else:
        print("Sorry, this feature is not supported.")

def youtube_search():
    voice.speak("What would you like to search for?")
    #search_keywords = input()
    search_keywords = voice.get_audio()
    voice.speak("Searching for: " + search_keywords)
    navigation.search(search_keywords)

def parse_video_input(input_string):
    if("play" in input_string or "pause" in input_string):
        navigation.toggle_pause()
    elif("channel" in input_string):
        voice.speak("The name of this channel is " + globals.page.channel)
    elif("view" in input_string):
        voice.speak(globals.page.num_views)
    else:
        print("Sorry, this feature is not supported.")


def list_videos(videos):
    output = "The first three videos are: "
    for i in range (3):
        if (i == 2):
            output += videos[i][1] + ". "
        else:
            output += videos[i][1] + ". The next video is "
    output += "Would you like to hear the rest?"
    voice.speak(output)
    continue_listing = voice.get_audio()
    if "yes" in continue_listing:
        output = ""
        for i in range (3, len(videos)):
            output += videos[i][1] + ". "
        voice.speak(output)
    else:
        return


