# YouTubeVideoSummarizer

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Video Summary and Note Saver is a powerful tool designed to save you time and enhance your video-watching experience. With this project, you can effortlessly summarize any video's content, eliminating the need to watch long, time-consuming videos while also providing a handy note-taking feature to capture the key points.

## Purpose

Have you ever wanted to quickly grasp the essential content of a lengthy video without having to watch the entire thing? Video Summary and Note Saver is here to help! Whether it's an insightful lecture, an engaging tutorial, or a captivating presentation, our project aims to simplify your video consumption by providing concise text summaries.

The major goals of this project are:

- Automatically summarize video content in text format.
- Save time by avoiding long video playback.
- Enable users to store essential notes for future reference.

## System Requirements

This project requires Python3. Ensure that you have Python 3 installed on your system before running the project. You can download Python 3 from the official Python website: [Python Downloads](https://www.python.org/downloads/).

To check if Python 3 is installed on your system, you can open a terminal or command prompt and run the following command:

```
python3 --version
```

## Setup Instructions

To get started with YTVideoSummarizer, you need to set some environment variables and install the necessary dependencies.

## Setting up YouTube API Key and Hugging Face Credentials

Before you can use YTVideoSummarizer, you need to obtain a YouTube API key and Hugging Face credentials. Here's how you can set up these credentials:

### Obtaining a YouTube API Key:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. Create a new project or select an existing one from the project dropdown.

3. In the left sidebar, click on "APIs & Services" and then "Library."

4. In the "Library" section, search for "YouTube Data API v3" and enable it for your project.

5. After enabling the API, click on "Credentials" in the left sidebar.

6. Click on "Create Credentials" and select "API Key."

7. Your new API key will appear on the screen. Click on the "Restrict Key" button to add restrictions if needed, such as restricting it to your IP address.

8. Copy the API key and set it as the `yt_api_key` environment variable as explained in the next setup instructions.

### Obtaining Hugging Face Credentials:

1. Go to the Hugging Face website (https://huggingface.co/).

2. Sign up for an account if you don't already have one.

3. Once you have an account and are logged in, navigate to your account settings.

4. In your account settings, you will find your Hugging Face username and an option to set your password.

5. Copy your Hugging Face username and set it as the `huggingface_username` environment variable.

6. Set your Hugging Face password as the `huggingface_pwd` environment variable.

With these credentials in place, you'll be able to use YTVideoSummarizer to summarize videos and save notes effectively.


### Setting Environment Variables

Before you can fetch a YouTube API key, Hugging Face username, and password from the environment, you need to set these variables. You can set environment variables as follows:

**On Windows :**

```shell
set yt_api_key=your_youtube_api_key_here
set huggingface_username=your_huggingface_username_here
set huggingface_pwd=your_huggingface_pwd_here
```

**On MacOS and Linux :**

```
export yt_api_key=your_youtube_api_key_here
export huggingface_username=your_huggingface_username_here
export huggingface_pwd=your_huggingface_pwd_here
```

**Setup Dependencies**
Next, install the required Python packages by running the following command:
```
pip install -r requirements.txt
```

**Running Instructions**
You can use Video Summary and Note Saver to summarize a video and save notes by running the following command:
```
python3 script.py <Link to Video>
```
Replace <Link to Video> with the actual URL of the video you want to summarize.

**Contributing**
We welcome contributions from the community to make this project even better. If you encounter any issues or have suggestions for improvements, please feel free to use the issue tracker to report problems or propose enhancements. Your feedback is valuable, and we appreciate your help in making this projecvt more efficient and user-friendly.

Thank you for using tool! I hope it simplifies your video-watching experience and boosts your productivity.
