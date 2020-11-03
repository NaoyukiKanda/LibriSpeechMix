#!/usr/bin/env python

# Copyright 2020 Naoyuki Kanda
# MIT license

import sys
import os
import json
import soundfile
import librosa
import numpy as np


def get_delayed_audio(wav_file, delay, sampling_rate=16000):
    audio, _ = soundfile.read(wav_file)
    delay_frame = int(delay * sampling_rate)
    if delay_frame != 0:
        audio = np.append(np.zeros(delay_frame), audio)
    return audio


def mix_audio(wavin_dir, wav_files, delays):
    for i, wav_file in enumerate(wav_files):
        if i == 0:
            audio = get_delayed_audio(os.path.join(wavin_dir, wav_file), delays[i])
        else:
            additional_audio = get_delayed_audio(os.path.join(wavin_dir, wav_file), delays[i])
            # tune length & sum up to audio
            target_length = max(len(audio), len(additional_audio))
            audio = librosa.util.fix_length(audio, target_length)
            additional_audio = librosa.util.fix_length(additional_audio, target_length)
            audio = audio + additional_audio
    return audio


if __name__ == "__main__":
    jsonl_file = sys.argv[1]
    wavin_dir = sys.argv[2]
    wavout_dir = sys.argv[3]

    with open(jsonl_file, "r") as f:
        for line in f:
            data = json.loads(line)
            mixed_audio = mix_audio(wavin_dir, data['wavs'], data['delays'])

            outfile_path = os.path.join(wavout_dir, data['mixed_wav'])
            outdir = os.path.dirname(outfile_path)
            if not os.path.exists(outdir):
                os.makedirs(outdir)
            soundfile.write(outfile_path, mixed_audio, samplerate=16000)
