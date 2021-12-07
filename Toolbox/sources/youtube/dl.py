from pytube import YouTube

def download_video(url):
        global downloadFile
        global youtube
        try:
          youtube = YouTube(url)
        except:
          return print('Invalid Video Link')
        video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
  
        downloadFile = video.download()
        print(f'Downloading {url}')

        return print(downloadFile)
    