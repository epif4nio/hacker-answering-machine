# offline text-to-speech
# pyttsx3 uses text-to-speech engine already installed in your platform.
# In Linux it uses espeak
# For online text-to-speech use gTTS (it uses Google's Text to Speech API)

import pyttsx3
import tempfile
import time
from pydub import AudioSegment # pydub uses ffmpeg underneath
from gtts import gTTS

#def save_text_to_audio_file(text, voice = "english-us"):
#    engine = pyttsx3.init()
#
#    engine.setProperty("rate", 150)
#    engine.setProperty("voice", voice)
#    mp3_file_path = tempfile.NamedTemporaryFile().name + ".mp3"
#    engine.save_to_file(text, mp3_file_path)
#    engine.runAndWait()
#
#    time.sleep(0.1)
#
#    wav_file_path = convert_audio_file(mp3_file_path)
#
#    return wav_file_path

def save_text_to_audio_file(text, language = "en"):
    mp3_file_path = tempfile.NamedTemporaryFile().name + ".mp3"
    tts = gTTS(text = text, lang = language, slow = False)
    tts.save(mp3_file_path)

    wav_file_path = convert_audio_file(mp3_file_path)

    return wav_file_path

def convert_audio_file(file_path):
    audio_file = AudioSegment.from_file(file_path, format="mp3")

    exported_file_path = tempfile.NamedTemporaryFile().name + ".wav"

    # export file as 8bit unsigned PCM WAV, 8Khz (32 bit rate)
    audio_file.export(exported_file_path, format="wav", parameters=["-ar", "8000", "-f", "u8", "-acodec", "pcm_u8"])

    return exported_file_path

# wav = save_text_to_audio_file("Previsão do tempo para hoje.")
# print(wav)
