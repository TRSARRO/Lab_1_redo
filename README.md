# Lab_1_redo

The files here are to be used for a redo of Lab 1 in Stony Brook's AST 443 course, Observational Techniques. The codes and files were run on Stony Brook's Astro Computing Lab's Uhura Machine.


Procedure:

Run the Masters.py code to produce the master-dark, master-flat, and master-bias frames.

Run the Process.sh code to process the science images.

Run the solve_field.sh code to align the images.

Run the SExtractor.sh code to extract the flux data from the science images.

Run the Image_Times.py code to extract the times each each science image was taken.

Run the Write_Data_Files.py code to write the time and flux values from each star in the analysis to a text file.

Run the Compare_Fluxes.py and Norm_stars_Plot.py codes to examine the fluxes of the reference stars.

Run the Light_Curve.py code to produce the light curve and read the average flux values for before, during, after the transit.


During the initial analysis, Uhura was connected to using ssh. Some of the codes did not run properly when run from ssh, but worked fine when the codes were run manually a few lines at a time (copy and pasted from a text editor).
