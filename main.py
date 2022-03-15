# region Variables
import audioplayer.abstractaudioplayer

Audio = ""  # mp3 local path
Volume_min = 0  # volume in conventional units, adjusted by selection
Script_lifetime = -1  # script lifetime in milliseconds, -1 == infinity
# endregion

# region Source Code
import sounddevice as sd
import numpy as np
import datetime
from audioplayer import AudioPlayer


def print_sound(indata, outdata, frames, time, status):
    volume_norm = int(np.linalg.norm(indata) * 100)
    if volume_norm > Volume_min:
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Detected loud sound. Volume level: {volume_norm}")
        try:
            AudioPlayer(Audio).play(block=True)
        except audioplayer.abstractaudioplayer.AudioPlayerError:
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Cannot find mp3 file.")



with sd.Stream(callback=print_sound):
    sd.sleep(Script_lifetime)
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Shutdown of the script...")
# endregion
