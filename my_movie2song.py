# import torch

# from faster_whisper import WhisperModel
# from typing import Iterator, TextIO

# def srt_format_timestamp(seconds: float):
#     assert seconds >= 0, "non-negative timestamp expected"
#     milliseconds = round(seconds * 1000.0)

#     hours = milliseconds // 3_600_000
#     milliseconds -= hours * 3_600_000

#     minutes = milliseconds // 60_000
#     milliseconds -= minutes * 60_000

#     seconds = milliseconds // 1_000
#     milliseconds -= seconds * 1_000

#     return (f"{hours}:") + f"{minutes:02d}:{seconds:02d},{milliseconds:03d}"

# def write_srt(transcript: Iterator[dict], file: TextIO):
#     count = 0
#     for segment in transcript:
#         count +=1
#         print(
#             f"{count}\n"
#             f"{srt_format_timestamp(segment['start'])} --> {srt_format_timestamp(segment['end'])}\n"
#             f"{segment['text'].replace('-->', '->').strip()}\n",
#             file=file,
#             flush=True,
#         )    

import os
from os import listdir
from os.path import isfile, join
from pathlib import Path


if __name__ == "__main__":


    # cwd = os.getcwd()
    cwd = "G:\VMware\Share dir"
    onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if 
    os.path.isfile(os.path.join(cwd, f))]
    # print(onlyfiles)    


    for file in onlyfiles:

        dir_path = os.path.dirname(file)
        fn_w_ext = os.path.basename(file)
        fn_wo_ext = Path(file).stem
        
        
        get_audio_cmd = "ffmpeg -y -map 0:a -acodec copy \"" + dir_path + "/" + fn_wo_ext + ".m4a\" -i \"" + file + "\""
        print(get_audio_cmd)
        os.system(get_audio_cmd)

        norm_cmd = "ffmpeg-normalize -ar 44100 -ext m4a -c:a aac -b:a 192k  -lrt 10 -f \"" + dir_path + "/" + fn_wo_ext + ".m4a\""
        print(norm_cmd)
        os.system(norm_cmd)
        
        os.remove(dir_path + "/" + fn_wo_ext + ".m4a")


