import requests
import os
import yt_dlp
import re
import platform

# Default download directories for different platforms
DOWNLOAD_DIR_PC = os.path.join(os.path.expanduser("~"), "Downloads")  # Default for PC (Windows/Linux)
DOWNLOAD_DIR_MAC = os.path.join(os.path.expanduser("~"), "Downloads")  # Default for Mac
DOWNLOAD_DIR_ANDROID = '/storage/emulated/0/Download'  # Default for Android
DOWNLOAD_DIR_IOS = '/var/mobile/Media/Downloads'  # Placeholder for iOS

def get_download_directory():
    """Identify the device type and return the appropriate download directory."""
    system = platform.system()
    if system == 'Linux' and 'ANDROID_STORAGE' in os.environ:
        return DOWNLOAD_DIR_ANDROID
    elif system == 'Darwin':
        return DOWNLOAD_DIR_MAC
    elif system == 'Windows':
        return DOWNLOAD_DIR_PC
    else:
        return DOWNLOAD_DIR_PC  # Default for other platforms like Linux desktops

def rename_mp4_to_mp3(mp4_filepath):
    """Rename the .mp4 file to .mp3 without changing content."""
    mp3_filepath = mp4_filepath.replace('.mp4', '.mp3')
    try:
        os.rename(mp4_filepath, mp3_filepath)  # Rename file
        print(f"Renamed {mp4_filepath} to {mp3_filepath}")
    except Exception as e:
        print(f"Error renaming {mp4_filepath} to MP3: {e}")

def download_file(link, req_format="mp4"):  # Default format is mp4
    DOWNLOAD_DIR = get_download_directory()  # Get the appropriate download directory

    try:
        # Enhanced YouTube/YouTube Music link detection using regular expression
        if re.match(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be|music\.youtube\.com)/.+', link):
            try:
                ydl_opts = {
                    'format': f'best[ext={req_format}]',
                    'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
                    'quiet': True
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=True)
                    filename = ydl.prepare_filename(info)
                    
                    # Ensure the filename has correct extension and path
                    filepath = os.path.join(DOWNLOAD_DIR, os.path.basename(filename))

                    # Verify the file exists and is not empty
                    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
                        print(f"Downloaded YouTube video: {filepath}")
                        
                        # If it's an mp4 file, rename it to mp3
                        if filepath.endswith('.mp4'):
                            rename_mp4_to_mp3(filepath)
                    else:
                        print(f"Error downloading YouTube video in {req_format.upper()} format: File not found or empty.")

            except yt_dlp.utils.DownloadError as e:
                if "Requested format is not available" in str(e):
                    print(f"Error downloading YouTube video in {req_format.upper()} format: Requested format is not available.")
                else:
                    print(f"Error downloading YouTube video: {e}")
                return

        else:  # Handle regular file downloads
            response = requests.get(link, stream=True)
            response.raise_for_status()

            filename = link.split('/')[-1] or 'downloaded_file'
            content_type = response.headers.get('content-type')

            if 'video/mp4' in content_type and req_format == 'mp4':
                filename += '.mp4'
            elif 'image/jpeg' in content_type:
                filename += '.jpg'
            else:
                print(f"Unsupported file type or format: {content_type}. Supported types: MP4, JPEG.")
                return

            filepath = os.path.join(DOWNLOAD_DIR, filename)
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"Downloaded file: {filename}")

            # If it's an mp4 file, rename it to mp3
            if filename.endswith('.mp4'):
                rename_mp4_to_mp3(filepath)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

    except Exception as e:
        print(f"Error downloading: {e}")

if __name__ == '__main__':
    while True:
        link = input("Enter the link to download (or 'q' to quit): ")
        if link.lower() == 'q':
            break

        download_file(link)
