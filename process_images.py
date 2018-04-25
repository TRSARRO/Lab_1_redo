#Author: Timothy Sarro
#Date: 4/10/18
#AST 443
#process_images

import numpy as np
from astropy.io import fits
#from scipy import stats
#from scipy.stats import norm
from glob import glob


#import matplotlib

#import matplotlib.pyplot as plt


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
    
def final(sciences,master_dark,master_flat,bias):
    final = []
    for sci in sciences:
        sci = sci - bias
        fin = ((sci - master_dark)/(master_flat))#*(np.mean(master_flat))
        final.append(fin)    
    return final

biases = []
darks = []
flats = []
sciences = []
    


#darks_raw = fits.open('wasp-93-b-darkfields.05.DARK.fits')
#darks = darks_raw[0].data
#flats_raw = fits.open('wasp-93-b-domeflats.05.fits')
#flats = flats_raw[0].data
#sciences_raw = fits.open('wasp-93-b-r-band-data.00000035.fits')
#sciences = sciences_raw[0].data

                        
bias_glob = glob('Lab_1_HAT-P-27b_bias_frame.000000**.BIAS.FIT')                       
darks_glob = glob('Lab_1_HAT-P-27b_dark_frame.000000**.DARK.FIT')
flats_glob = glob('Lab_1_HAT-P-27b_dome_flat.000000**.FIT')
sciences_glob = glob('Lab_1_HAT-P-27b_science_exposures.00000***.FIT')

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
    
for sci in sciences_glob:
    sci_raw = fits.open(sci)
    sci_data = sci_raw[0].data
    sciences.append(sci_data)
                        
#for i in range(0,9):
#    darks_raw = fits.open('wasp-93-b-darkfields.0%.DARK.fits' % i)
#    darks_data = darks_raw[0].data
#    darks.append(darks_data)
#    flats_raw = fits.open('wasp-93-b-domeflats.0%.fits' % i)
#    flats_data = flats_raw[0].data
#    flats.append(flats_data)
    
#for i in range(29,50):
#    sciences_raw = fits.open('wasp-93-b-r-band-data.000000%.fits' % i)
#   sciences_data = sciences_raw[0].data
#   sciences.append(sciences_data)

              
master_bias = masterbias(biases)  
master_dark = masterdark(darks,master_bias)
master_flat = masterflat(flats,master_bias)

#plt.imshow(master_dark, cmap='gray')
#plt.imshow(master_flat, cmap='gray')


images_final = final(sciences,master_dark,master_flat,master_bias)


for i in range(1,400):
    n = i - 1
    fits.writeto('Lab_1_HAT-P-27b_processed_images.%i.FIT' %i, images_final[n])