#!/bin/bash

# Copyright 2020 Naoyuki Kanda
# MIT license

set -e
set -u
set -o pipefail

data_out=./data

# all utterances are FLAC compressed
if ! which flac >&/dev/null; then
   echo "Please install 'flac'!"
   exit 1
fi

# download & untar necessary data
if [ ! -d $data_out/original ]; then
    mkdir -p $data_out/original
    (
        cd $data_out/original
        for dataid in dev-clean test-clean; do
            wget http://www.openslr.org/resources/12/$dataid.tar.gz
            tar xvzf $dataid.tar.gz
        done
    )
fi

# convert flac to wav
if [ ! -f $data_out/.done.wavfile_gen ]; then
    for flac_file in `find $data_out/original/LibriSpeech -type f | grep '\.flac'`; do
        echo flac -d -s $flac_file ${flac_file/\.flac/.wav}
        flac -d -s $flac_file -o ${flac_file/\.flac/.wav}
    done
    for dataid in dev-clean test-clean; do
        (cd $data_out; ln -s original/LibriSpeech/$dataid $dataid)
    done
    touch $data_out/.done.wavfile_gen
fi

# generate mixed wav
if [ ! -f $data_out/.done.mix_wavfile_gen ]; then
    for datatype in dev-clean test-clean; do
        for mix in 1 2 3; do
            python utils/mix_wavs.py \
                list/${datatype}-${mix}mix.jsonl \
                $data_out \
                $data_out
        done
    done
    touch $data_out/.done.mix_wavfile_gen 
fi