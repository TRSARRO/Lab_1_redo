#! /bin/bash -u

for file in $(ls -1 Lab_1_HAT-P-27b_science_exposures.00000***.fits)
do
    ftpixcalc $(basename " $file" .fits)"_dark.fits" a-b a=$file b=master_dark_test_1.fits
done

for file in $(ls -1 Lab_1_HAT-P-27b_science_exposures.00000***.fits)
do
    ftpixcalc $(basename " $file" _dark.fits)"_final.fits" a/b a=$file b=master_flat_test_5.fits
done
