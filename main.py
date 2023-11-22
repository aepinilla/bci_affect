"""
1. Loading the data
2. Preprocessing
3. Feature extraction
4. Train models
"""

import numpy as np
import pyxdf
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import pyxdf
import mne
from mne.datasets import misc

from settings import eeg_stream_name, markers_stream_name, ecg_stream_name, markers_dict, gtec_channels_list

# 1. Loading the data
## Read file
fname = '3I6EY.xdf'
print("Reading data...")
streams, fileheader = pyxdf.load_xdf( 'data/%s' % (fname)) # Read streams

## What is the index of the EEG and markers streams?
streams_names = [streams[s]['info']['name'][0] for s in range(len(streams))]
eeg_stream_index = streams_names.index(eeg_stream_name)
markers_stream_index = streams_names.index(markers_stream_name)

## Read data and markers
data = streams[eeg_stream_index]["time_series"].T
markers = streams[markers_stream_index]["time_series"].T
# TODO: Append markers to MNE data

assert data.shape[0] == 12
sfreq = float(streams[0]["info"]["nominal_srate"][0])
info = mne.create_info(gtec_channels_list, sfreq, ["eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg","eeg",])
raw = mne.io.RawArray(data, info)
raw.plot(duration=1, start=0)

# 2. Preprocessing
## Notch filter: Remove powerline noise using a notch filter at 50 Hz.
freqs = (50, 60)
raw_notch = raw.copy().notch_filter(freqs=freqs)
raw_notch.plot(duration=1, start=0)
## TODO: Adjust for real-time filtering. Filtering always introduces artifacts on the edges of the array. Therefore, we need to allow a few seconds of additional data at each edge of the array, so that the artifacts are applied to that extra data. Then, the additional data should be removed and appended to the following chunk in the data buffer.

## Remove bad channels: Remove channels where a flatline longer than 5 s is detected, or whose correlation with nearby channels is lower than 80%.

## Remove artifacts: Remove artifacts caused by eye movements, eye blinks, and other noise sources using Artifact Subspace Reconstruction (ASR)

## Re-referencing: Perform common-average referencing.

## Band-pass filter: Apply band-pass filter to remove frequencies below 4 Hz and above 45 Hz.

## Extract epochs: Each video (trial) is equivalent to one epoch. Thus, the length of each epoch is 60 s.

## Baseline removal: Remove the baseline of the 3 s prior to the beginning of each epoch.

## Down-sampling: Down-sample to 128 Hz to increase processing speed.

# 3. Feature extraction
## Relative Power Spectral Density (RPSD) (Antons et al., 2014)

## Frontal asymmetry (Huster et al., 2009)

## Spectral envelope (Kraljevic et al., 2017)

## Number of zero-crossings (Patil et al., 2016)

## Katz fractal dimension (Akar et al., 2015)

## Hjorth parameters (Mehmood and Lee, 2015)

## Petrosian fractal dimension (Balan et al., 2020)

# 4. Train models