import time

import numpy as np
from matplotlib import pyplot as plt
from mne import pick_types
# from mne import pick_types, set_log_level

from mne_lsl.datasets import sample
from mne_lsl.lsl import StreamInlet, resolve_streams
from mne_lsl.player import PlayerLSL as Player
from mne_lsl.stream import StreamLSL as Stream

from mne.datasets import sample
# from mne.io import read_raw_fif

# set_log_level("WARNING")

def stream():
    fname = sample.data_path() / "sample-ant-raw.fif"
    player = Player(fname)
    player.start()


if __name__ == '__main__':
    stream()