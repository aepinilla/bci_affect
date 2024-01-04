import time

from mne_lsl.lsl import StreamInlet, resolve_streams
from stream import stream

sfreq = 1024
window_size = 8

def receive():
    stream()

    streams = resolve_streams()
    inlet = StreamInlet(streams[0])
    inlet.open_stream()

    while True:
        data, ts = inlet.pull_chunk(timeout=window_size, max_samples=sfreq*window_size)
        print(data.shape) # (n_samples, n_channels)
        # del inlet


if __name__ == '__main__':
    receive()