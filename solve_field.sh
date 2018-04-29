#! /bin/bash -u

for file in $(ls -1 Lab_1_HAT-P-27b_processed_images.*.fits)
do 
    solve-field --ra 222.7667 --dec 5.9472 --radius 1 ${file}
done
