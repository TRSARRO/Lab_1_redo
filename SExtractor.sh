#! /bin/bash -u

for file in $(ls -1 Lab_1_HAT-P-27b_processed_images.*.new)
do 
    sex ${file} -c default.se -CATALOG_NAME $(basename " $file" .new)".cat"

done
