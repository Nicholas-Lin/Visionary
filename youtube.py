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
    if("play" in input_string):
        if("first" in input_string):
            navigation.go_to_page(globals.page.videos[0])
        elif("second" in input_string):
            navigation.go_to_page(globals.page.videos[1])
        elif("third" in input_string):
            navigation.go_to_page(globals.page.videos[2])
    elif("video" in input_string ):
        list_videos(globals.page.videos)
    else:
        print("Sorry, this feature is not supported.")

def parse_video_input(input_string):
    if("read" in input_string):
        if("description" in input_string):
            voice.speak(globals.page.description)
        elif("comment" in input_string):
            list_videos(globals.page.comments)
        else:
            print("Sorry that item was not found")
    elif("who" in input_string):
        #TODO: only prints first author if there is one. Might break if no authors
        print(globals.page.authors[0])
        voice.speak("The author is " + globals.page.authors[0])
    elif("when" in input_string or "date" in input_string):
        print(globals.page.date)
        voice.speak("This article was published on " + globals.page.date)
    else:
        print("Sorry, this feature is not supported.")


def list_videos(videos):
    output = "The first three videos are: "
    for i in range (3):
        if (i == 2):
            output += videos[i] + ". "
        else:
            output += videos[i] + ". The next video is "
    output += "Would you like to hear the rest?"
    voice.speak(output)
    continue_listing = voice.get_audio()
    if "yes" in continue_listing:
        output = ""
        for i in range (3, len(videos)):
            output += videos[i] + ". "
        voice.speak(output)
    else:
        return


