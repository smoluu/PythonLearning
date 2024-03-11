from gtts import gTTS
import os
import ffmpeg

def text_to_speech(text):
    # Initialize gTTS with the text to convert
    speech = gTTS(text, lang="en", tld="us")

    # Save the audio file to a temporary file
    speech_file = './gTTS-ffmpeg/speech.mp3'
    speech.save(speech_file)

    # Pitch adjustment
    (
    ffmpeg.input(speech_file)
    .filter("asetrate",24000*1.05)
    .filter("aresample",24000)
    .filter("atempo",1.3)
    .output("./gTTS-ffmpeg/output.mp3")
    .run(overwrite_output=True)
    )
    os.system('cvlc --play-and-exit ' + "./gTTS-ffmpeg/output.mp3")


text_to_speech("Bullseye!. 78")