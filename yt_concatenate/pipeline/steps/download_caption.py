import  os
import yt_dlp
from .step import Step
from .step import StepException
import time

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print('dowloading caption for', url)
            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'skip_download': True,
                'subtitleslangs': ['en'],
            }

            url = 'https://www.youtube.com/watch?v=kX3nB4PpJko'

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        end = time.time()
        print('took', end - start, 'seconds')
