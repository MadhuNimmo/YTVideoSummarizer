import os
import sys
import googleapiclient.discovery
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from hugchat import hugchat
from hugchat.login import Login


# Setting API keys
yt_api_key = os.environ.get("yt_api_key")
huggingface_username = os.environ.get("huggingface_username")
huggingface_pwd = os.environ.get("huggingface_pwd")

# The video URL
video_url = sys.argv[1]

# Extract video ID from the video link
video_id = video_url.split('v=')[1]

# Get the transcript for the video
youtube = build('youtube', 'v3', developerKey=yt_api_key)
captions = youtube.captions().list(part='snippet', videoId=video_id).execute()
caption = captions['items'][0]['id']
transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

transcript_txt=""

for transcript in transcript_list:
    transcript_txt+=transcript['text']


if transcript_txt!="":

        # Log in to huggingface and grant authorization to huggingchat
        sign = Login(huggingface_username,huggingface_pwd)
        cookies = sign.login()

        # Save cookies to the local directory
        cookie_path_dir = "./cookies_snapshot"
        sign.saveCookiesToDir(cookie_path_dir)

        # Create a ChatBot
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        # Extract the summary from the response
        query_result = chatbot.query("Summarize in 2-3 lines: "+transcript_txt)

        # Print the summary
        print("Summary:")
        print(query_result)
else:
        print("No Transcript Found")