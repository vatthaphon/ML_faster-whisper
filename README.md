# Extension of faster-whisper

## Description
I forked faster-whisper from https://github.com/SYSTRAN/faster-whisper. 

## Usage
1. Follow https://github.com/SYSTRAN/faster-whisper to create the environment.
2. If you want to transcribe the video, you first extract an audio file from the video using, e.g., "ffmpeg -ar 44100 -q:a 0 -map a output_audio.mp3 -i input_video.mp4". Then, run my_speech2txt.py to convert the audio to text.
3. Or you can use my_movie2song.py to do the second step automatically.
