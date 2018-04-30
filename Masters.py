import numpy as np
from astropy.io import fits
from glob import glob


def masterbias(biases):
    master_bias = np.median(biases, axis = 0)
    #fits.writeto('master_bias_test_2.fits', master_bias)
    return master_bias


def masterdark(darks,bias):
    darks = darks - bias
    master_dark = (np.median(darks, axis = 0))
    #fits.writeto('master_dark_test_2.fits', master_dark)
    return master_dark

def masterflat(flats,bias):
    flat_array = []
    for flat in flats:
        flat = flat - bias
        flat_value = flat.flatten()
        u = np.mean(flat_value)
        norm_flat = (flat/u) 
        flat_array.append(norm_flat)
    master_flat = np.median(flat_array, axis = 0)
    #fits.writeto('master_flat_test_6.fits', master_flat)
    return master_flat
    
    
biases = []
darks = []
flats = []


bias_glob = glob('Lab_1_HAT-P-27b_bias_frame.000000**.BIAS.fits')                       
darks_glob = glob('Lab_1_HAT-P-27b_dark_frame.000000**.DARK.fits')
flats_glob = glob('Lab_1_HAT-P-27b_dome_flat.000000**.fits')


for bias in bias_glob:
    bias_raw = fits.open(bias)
    bias_data = bias_raw[0].data
    biases.append(bias_data)

for dark in darks_glob:
    dark_raw = fits.open(dark)
    dark_data = dark_raw[0].data
    darks.append(dark_data)
                        
for flat in flats_glob:
    flat_raw = fits.open(flat)
    flats_data = flat_raw[0].data
    flats.append(flats_data)
    

master_bias = masterbias(biases)  
master_dark = masterdark(darks,master_bias)
master_flat = masterflat(flats,master_bias)


fits.writeto('Master_Bias.fits', master_bias)
fits.writeto('Master_Dark.fits', master_dark)
fits.writeto('Master_Flat.fits', master_flat)
