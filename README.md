---

## 📥 YouTube/Mp3/URL Downloader

This Python script allows users to download videos from YouTube and other URLs, saving them directly to the appropriate download directory based on the device's operating system. It also includes a feature to convert downloaded .mp4 files to .mp3 format.

## ⚙️ Prerequisites

Before running this script, ensure Python is installed. Additionally, install the required libraries listed below.

## 📦 Required Libraries

## Install the following libraries:

- requests
- yt-dlp
- re
- platform
- os


## Install these libraries using pip:

pip install requests yt-dlp


---

## 📝 Features

Platform-Specific Download Path
Automatically detects the operating system (Windows, macOS, Linux, Android) and saves downloads to the default directory.

YouTube and YouTube Music Link Detection
Uses regular expressions to identify and download content from YouTube and YouTube Music.

File Download and Conversion
Downloads files in the specified format and automatically renames .mp4 files to .mp3 for audio playback.



---

## 📂 Code Syntax

import requests
import os
import yt_dlp
import re
import platform

## 🧩 Functions Overview

1. get_download_directory()
- 🗂️ Detects the user's operating system and returns the corresponding download directory.


2. rename_mp4_to_mp3(mp4_filepath)
- 🔄 Renames a downloaded .mp4 file to .mp3.


3. download_file(link, req_format="mp4")
- 🎬 Handles downloading files from the specified link. By default, downloads .mp4 format but can also save other formats.

Uses yt_dlp to download YouTube or YouTube Music videos.

For other content, downloads directly using requests.





---

## 🚀 Usage

Run the script by executing:

python your_script_name.py

Upon running, the script will prompt you for a download link. Type q to quit at any time.

Enter the link to download (or 'q' to quit): <your_link_here>

## 🌐 Example Usage

1. Downloading a YouTube Video
Enter a YouTube video link to download in .mp4 format. The script saves it in the default download directory for your OS.


2. Downloading and Converting to MP3
After downloading a video in .mp4 format, the script renames it to .mp3 for audio playback.




---

## 📝 Notes

Compatibility: This script supports Windows, macOS, Linux, and Android.

iOS Compatibility: The download path for iOS is defined but may require adjustments based on the user environment.



---

## 🔗 License

-- Created By JaysonC

Distributed under the MIT License. See LICENSE for more information.

---











