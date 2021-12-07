import click
from rich.console import Console
console = Console()

@click.command()
@click.option('--youtube', default=None,
              help='put url to download a video')                         
def cli(version, hi, youtube):

  if version:
    console.print(f'Toolbox v3', style='red bold italic')
  
  if hi:
    console.print(f"Hello,,,,,,, {hi}")

  
  if youtube:
    from pytube import YouTube
    try:
      youtube = YouTube(youtube)
    except:
      return print('Invalid Video Link')
    video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    downloadFile = video.download()
    return print(downloadFile)
