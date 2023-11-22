# For this tutorial we are going to use only 7 channels: F3, F4, T7, T8, P3, P4 and Cz.
# subset_channels = {'F3': 4,
#                    'F4': 27,
#                    'T7': 7,
#                    'T8': 24,
#                    'P3': 12,
#                    'P4': 19,
#                    'Cz': 32}


# Gtec channels
gtec_channels = {
    'ref_ch':       0,
    'f3_ch':        1,
    'f4_ch':        2,
    'p3_ch':        3,
    'p4_ch':        4,
    't7_ch':        5,
    't8_ch':        6,
    'cz_ch':        7,
    'zm_ch':        9,
    'zm_ref_ch':    10,
    'cs_ch':        11,
    'cs_ref_ch':    12,
}

gtec_channels_list = [
    'ref_ch',
    'f3_ch',
    'f4_ch',
    'p3_ch',
    'p4_ch',
    't7_ch',
    't8_ch',
    'cz_ch',
    'zm_ch',
    'zm_ref_ch',
    'cs_ch',
    'cs_ref_ch']

# Brain Products channel
ecg_ch = 0

# Psychopy markers
markers_ch = 0

# Markers used during the experiment
markers_dict = {
    'start_practice_block': 0,
    'end_practice_block': 1,
    'start_baseline': 2,
    'end_baseline': 3,
    'start_exp_task': 4,
    'end_exp_task': 5,
    'cross': 6,
    'start_video': 7,
    'end_video': 8}

# Streams names
eeg_stream_name = 'g.USBamp'
markers_stream_name = 'psychopy_marker_oddball'
ecg_stream_name = 'BrainVision RDA'