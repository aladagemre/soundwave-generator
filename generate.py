from wavebender import *
from itertools import *
import time

import datetime as DT
def now(dt): 
    import datetime
    ts = DT.datetime.now()+DT.timedelta(seconds=dt)
    st = ts.strftime('%Y-%m-%d %H:%M:%S')
    return st

def generate(frequency):
    noise = cycle(islice(white_noise(amplitude=0.000), 44100))

    channels = ((sine_wave(float(frequency), amplitude=0.1), noise),
                (sine_wave(float(frequency), amplitude=0.1), noise))

    samples = compute_samples(channels)
    write_wavefile(stdout, samples)


freq = sys.argv[1]
generate(freq)
