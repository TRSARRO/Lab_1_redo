import numpy as np
from astropy.io import fits
from glob import glob

times = []

science_glob = glob('Lab_1_HAT-P-27b_science_exposures.00000***.FIT')

for sci in science_glob:
    sci_raw = fits.open(sci)
    sci_header = sci_raw[0].header
    times.append(sci_header['TIME-OBS'])
    
np.asarray(times)
    
np.savetxt('ImageTimes.txt',times, fmt="%s")
