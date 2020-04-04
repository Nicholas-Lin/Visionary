'''
Nicholas Lin
voice.py
4/2/20
'''
import os
import re
import time
import playsound
import keyboard
import speech_recognition as sr
from gtts import gTTS
import simpleaudio as sa
from pydub import AudioSegment

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout = None)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(e)
    return said.lower()

def speak(text):
    print(text)
    tts = gTTS(text)
    filename = "voice.mp3"
    tts.save(filename)

    # To use code without ffmpeg comment the rest of this method out
    # Comment out "from pydub import AudioSegment"
    # Add "playsound.playsound(filename)"

    # Need to convert mp3 to WAV
    sound = AudioSegment.from_mp3(filename)
    sound.export("voice.wav", format="wav")

    # Need to use sa to have control over playback
    wave_obj = sa.WaveObject.from_wave_file("voice.wav")
    play_obj = wave_obj.play() 
    #TODO: Find a way to stop playback
    while(play_obj.is_playing()):
        if keyboard.is_pressed('s'):
            play_obj.stop()

# Used for reading long input
def read(text):
    words = text.split(" ")
    read_it = ""
    for x in range(len(words)):
        read_it += words[x] + " "
        if "." in words[x] or x == len(words)-1:
            speak(read_it)
            read_it = ""
        if keyboard.is_pressed('s'):
            break
        
'''
    while(play_obj.is_playing()):
        if input() != "":
            print("keyboard interrupt detected")
            play_obj.stop()

voice_input = ""

def init_listen():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    # start listening in the background (note that we don't have to do this inside a `with` statement)
    stop_listening = r.listen_in_background(m, callback)
    # calling this function requests that the background listener stop listening
    #stop_listening(wait_for_stop=False)

# this is called from the background thread
def callback(recognizer, audio):
    global voice_input
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        said = recognizer.recognize_google(audio).lower()
        playsound.playsound("activation_beep.mp3")
        print(said)
        voice_input = said
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
'''