# from doctest import OutputChecker
# from pytube import Playlist
# from moviepy.editor import *

# import sys
from pytube import YouTube


def download(videourl, file_name):
    yt = YouTube(videourl)
    progMP4 = yt.streams.filter(progressive=True, file_extension='mp4')   # 設定下載方式及格式
    targetMP4 = progMP4.order_by('resolution').desc().first()  # 由畫質高排到低選畫質最高的來下載
    # targetMP4 = yt.streams.filter(progressive=True, file_extension='mp4')   # 設定下載方式及格式
    name = f'{file_name}.mp4'  # 給下載影片名
    targetMP4.download(output_path=f'./static/musicfile/mp4/{file_name}' , filename=name) # 下載影片並給輸出路徑    
        
