# -*- coding: utf-8 -*-
"""
@Author: shining
@File: text_to_audio.py
@Date: 2022/1/12 8:48 下午
@Version: python 3.10
@Describe:
"""
from gtts import gTTS


class TextToAudio:
    """
    测试hive机审
    """

    def read_text_file(self, file_path):

        with open(file_path, 'r', encoding="utf8") as f:
            return f.read()

    def transfer_to_audio(self, file):

        audio = gTTS(self.read_text_file(file))
        audio.save(file.split('.')[0] + ".mp3")


if __name__ == "__main__":

    file = "video_to_audio.txt"
    ta = TextToAudio()
    ta.transfer_to_audio(file)


