import torch

from faster_whisper import WhisperModel
from typing import Iterator, TextIO

def srt_format_timestamp(seconds: float):
    assert seconds >= 0, "non-negative timestamp expected"
    milliseconds = round(seconds * 1000.0)

    hours = milliseconds // 3_600_000
    milliseconds -= hours * 3_600_000

    minutes = milliseconds // 60_000
    milliseconds -= minutes * 60_000

    seconds = milliseconds // 1_000
    milliseconds -= seconds * 1_000

    return (f"{hours}:") + f"{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def write_srt(transcript: Iterator[dict], file: TextIO):
    count = 0
    for segment in transcript:
        count +=1
        print(
            f"{count}\n"
            f"{srt_format_timestamp(segment['start'])} --> {srt_format_timestamp(segment['end'])}\n"
            f"{segment['text'].replace('-->', '->').strip()}\n",
            file=file,
            flush=True,
        )    


if __name__ == "__main__":

    device = "cpu"
    # device = "cuda"

    compute_type = "float32"
    # compute_type = "float16"
    # compute_type = "int8"

    print("device: ", device)
    print("compute_type: ", compute_type)

    language = "ja"

    # model_name = "large-v2"
    # model_name = "large-v3"
    # model_name = "tiny"
    model_name = "whisper-large-v2-japanese-5k-steps" # To get this model, we run "ct2-transformers-converter --model clu-ling/whisper-large-v2-japanese-5k-steps --output_dir whisper-large-v2-japanese-5k-steps"

    # model = WhisperModel(model_name, device=device, compute_type=compute_type, device_index=[0, 1])
    # model = WhisperModel(model_name, device=device, compute_type=compute_type)
    model = WhisperModel(model_name, device=device)

    # segments, info = model.transcribe("G:\output_audio.m4a", beam_size=5,  task="translate", language=language)
    # segments, info = model.transcribe("G:\output_audio.mp4", beam_size=5,  task="translate", language=language)
    segments, info = model.transcribe("G:\output_audio.mp3", beam_size=5,  task="translate", language=language)
    # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    # for segment in segments:
    #     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

    fn = "G:\output_audio.srt"
    count = 0

    # with open(os.path.join(output_dir, os.path.splitext(filename)[0] + f".{language}.srt"), "w") as srt:    
    with open(fn, "w") as srt:
        for segment in segments:
            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

            count +=1
            print(
                f"{count}\n"
                f"{srt_format_timestamp(segment.start)} --> {srt_format_timestamp(segment.end)}\n"
                f"{segment.text.replace('-->', '->').strip()}\n",
                file=srt,
                flush=True,
            )            



