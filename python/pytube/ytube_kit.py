#!/usr/bin/env python3

import pytube
import pprint

url = "https://www.youtube.com/watch?v=QWqBPoT7d0I"
#url = "https://youtu.be/JPfuYpvMojk"

next_print = 1


def progress_function(stream, chunk, file_handle, bytes_remaining):
    global next_print
    perc_done = round((1-bytes_remaining/video.filesize)*100, 3)
    if perc_done > next_print:
        next_print = min(next_print + 1, 100)
        print(perc_done, '% done...', flush=True)


yt = pytube.YouTube(url, on_progress_callback=progress_function)
video = yt.streams.first()
print("Downlading: " + video.default_filename, flush=True)

video.download('/Users/matt.west')
