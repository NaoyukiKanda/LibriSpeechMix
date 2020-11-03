# LibriSpeechMix

The evaluation dataset for multi-talker speech recognition research. 
- Unique properties
  - Partially overlapped speech (i.e. not fully overlapped speech), which is closer to real senarios.
  - Carefully designed for ASR evaluation. WERs of different number of speaker mixtures (e.g., WERs for 2-speaker-mixed and 3-speaker-mixed test sets) can be compared meaningfully.
    - For N-speaker-mixed evaluation set, each utterance in the original LibriSpeech evaluation data is used exactly N times.
    - Each mixed audio does not contain multiple utterances of the same speaker.
  - Including the information for speaker profile extraction, which is specially tailored for speaker-attributed automatic speech recogntion (SA-ASR) experiments.
- The dataset was used for the papers listed below. 
  - Naoyuki Kanda, Yashesh Gaur, Xiaofei Wang, Zhong Meng, Takuya Yoshioka: Serialized Output Training for End-to-End Overlapped Speech Recognition, Proc. Interspeech, pp. 2797-2801, 2020. [[pdf]](https://www.isca-speech.org/archive/Interspeech_2020/pdfs/0999.pdf)
  - Naoyuki Kanda, Yashesh Gaur, Xiaofei Wang, Zhong Meng, Zhuo Chen, Tianyan Zhou , Takuya Yoshioka: Joint speaker counting, speech recognition, and speaker identification for overlapped speech of any number of speakers. Proc. Interspeech, pp. 36-40, 2020. [[pdf]](https://www.isca-speech.org/archive/Interspeech_2020/pdfs/1085.pdf)
- Intersted readers may also refer the related paper.
  -  Naoyuki Kanda, Xuankai Chang, Yashesh Gaur, Xiaofei Wang, Zhong Meng, Zhuo Chen, Takuya Yoshioka: Investigation of End-To-End Speaker-Attributed ASR for Continuous Multi-Talker Recordings. Proc. SLT, 2021 (to appear). [[pdf]](https://arxiv.org/pdf/2008.04546.pdf)

## Prerequisites
- Linux
  - python3
  - flac

## How to Generate Data
Following commands will first download LibriSpeech evaluation data ("dev_clean" and "test_clean"), and then generate mixed audio.
```sh
$ pip install soundfile librosa numpy
$ bash run.sh
```
Mixed audio is generated under ./data/ directory according to the information in *.jsonl file.
```
list/
├── dev-clean-1mix.jsonl
├── dev-clean-2mix.jsonl
├── dev-clean-3mix.jsonl
├── test-clean-1mix.jsonl
├── test-clean-2mix.jsonl
└── test-clean-3mix.jsonl
```

## Data Format of *.jsonl file
### Each line of *.jsonl corresponds to a string of JSON data.
|Element|Type|Meaning|
|---|---|---|
|id|Required|Utterance id|
|mixed_wav|Required|Path to the mixed audio (NOTE: relative path from ./data/)|
|texts|Required|Transcription|
|speaker_profile|Option for SA-ASR|Audio list for speaker profile extraction (NOTE: relative path from ./data/)|
|speaker_profile_index|Option for SA-ASR|Index of speaker profile corresponding to each utterance in the mixed audio|
|wavs||Original wav files used to generage the mixed audio (NOTE: relative path from ./data)|
|delays||Delay (sec) for each utterance when the mixed audio is generated|
|speakers||Speaker id of each utterance|
|durations||Duration of each original wav file|
|genders||Gender of the speaker of each utterance in the mixed audio|

### Example of 2-speaker-mixed audio (indented for visibility)
```
{
    "id": "dev-clean-2mix/dev-clean-2mix-0000", 
    "mixed_wav": "dev-clean-2mix/dev-clean-2mix-0000.wav", 
    "texts": [
        "MISTER QUILTER IS THE APOSTLE OF THE MIDDLE CLASSES AND WE ARE GLAD TO WELCOME HIS GOSPEL",
        "THAT ENCHANTMENT HAD POSSESSED HIM USURPING AS IT WERE THE THRONE OF HIS LIFE AND DISPLACING IT WHEN IT CEASED HE WAS NOT HIS OWN MASTER"], 
    "speaker_profile": [
        ["dev-clean/6241/61943/6241-61943-0008.wav", "dev-clean/6241/61946/6241-61946-0001.wav"], 
        ["dev-clean/174/84280/174-84280-0011.wav", "dev-clean/174/50561/174-50561-0005.wav"], 
        ["dev-clean/1988/147956/1988-147956-0007.wav", "dev-clean/1988/24833/1988-24833-0011.wav"],
        ["dev-clean/7850/281318/7850-281318-0016.wav", "dev-clean/7850/286674/7850-286674-0013.wav"],
        ["dev-clean/1919/142785/1919-142785-0024.wav", "dev-clean/1919/142785/1919-142785-0034.wav"],
        ["dev-clean/6295/244435/6295-244435-0023.wav", "dev-clean/6295/64301/6295-64301-0002.wav"],
        ["dev-clean/2428/83699/2428-83699-0005.wav", "dev-clean/2428/83705/2428-83705-0025.wav"], 
        ["dev-clean/1272/141231/1272-141231-0022.wav", "dev-clean/1272/128104/1272-128104-0005.wav"]], 
    "speaker_profile_index": [7, 5], 
    "wavs": ["dev-clean/1272/128104/1272-128104-0000.wav", "dev-clean/6295/64301/6295-64301-0026.wav"]
    "delays": [0.0, 4.469242864375414], 
    "speakers": ["1272", "6295"], 
    "durations": [5.855, 10.43], 
    "genders": ["m", "m"], 
}
```

## Citation
```
@inproceedings{kanda2020serialized,
  title={Serialized Output Training for End-to-End Overlapped Speech Recognition},
  author={Kanda, Naoyuki and Gaur, Yashesh and Wang, Xiaofei and Meng, Zhong and Yoshioka, Takuya},
  booktitle={Proc. Interspeech},
  pages={2797--2801},
  year={2020}
}

@inproceedings{kanda2020joint,
  title={Joint speaker counting, speech recognition, and speaker identification for overlapped speech of any number of speakers},
  author={Kanda, Naoyuki and Gaur, Yashesh and Wang, Xiaofei and Meng, Zhong and Chen, Zhuo and Zhou, Tianyan and Yoshioka, Takuya},
  booktitle={Proc. Interspeech},
  pages={36--40},
  year={2020}
}

@article{kanda2020investigation,
  title={Investigation of End-To-End Speaker-Attributed ASR for Continuous Multi-Talker Recordings},
  author={Kanda, Naoyuki and Chang, Xuankai and Gaur, Yashesh and Wang, Xiaofei and Meng, Zhong and Chen, Zhuo and Yoshioka, Takuya},
  journal={arXiv preprint arXiv:2008.04546},
  year={2020}
}
```