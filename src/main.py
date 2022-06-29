import time
from audio_to_midi import audio2midi
import sounddevice as sd
import soundfile as sf

import note_seq


# from huggingface_hub import notebook_login
#
# notebook_login()


from transformers import AutoTokenizer, AutoModelForCausalLM

with open("access_token.pwd", "r") as f:
    access_token = f.read()

tokenizer = AutoTokenizer.from_pretrained("ai-guru/lakhclean_mmmtrack_4bars_d-2048", use_auth_token=access_token)

model = AutoModelForCausalLM.from_pretrained("ai-guru/lakhclean_mmmtrack_4bars_d-2048", use_auth_token=access_token)


# fs = 44100
# sd.default.samplerate = fs
# sd.default.channels = 1
#
# duration = 4  # seconds
# myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
# sf.write("new.wav", myrecording, fs)
# sd.wait()


s_time = time.time()
audio2midi.run("new.wav", "new.mid")
e_time = time.time()
print(f'conversion took {e_time - s_time}s')