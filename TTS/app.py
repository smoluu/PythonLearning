from TTS.api import TTS
path = "./TTS/audio.wav"
'''
models
tts_models/en/ljspeech/tacotron2-DDC  woman
tts_models/fi/css10/vits man
tts_models/en/ek1/tacotron2 doesnt work
tts_models/en/ljspeech/glow-tts

speaker_wav="tts_models/fi/css10/vits"
'''
tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")
text = "One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten"
tts.tts_to_file(text=text, file_path=path, emotion="excited")
