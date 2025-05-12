from yt_concatenate.pipeline.steps.get_video_list import GetVideoList
from yt_concatenate.pipeline.steps.download_caption import DownloadCaptions
from yt_concatenate.pipeline.steps.preflight import Preflight
from yt_concatenate.pipeline.steps.postflight import Postflight
from yt_concatenate.pipeline.steps.step import StepException
from yt_concatenate.pipeline.pipeline import Pipeline
from yt_concatenate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
        ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()