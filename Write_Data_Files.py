import numpy as np
import datetime
import time
import os 


#Removes files from directory if this code has been run before
if os.path.isfile('Flux_Values_Main.txt'):
    os.remove('Flux_Values_Main.txt')
    os.remove('Flux_Values_1.txt')
    os.remove('Flux_Values_2.txt')
    os.remove('Flux_Values_3.txt')
    os.remove('Flux_Values_4.txt')
    os.remove('Flux_Values_5.txt')
    os.remove('Flux_Values_6.txt')
    os.remove('Flux_Values_7.txt')
    os.remove('Flux_Values_8.txt')
    os.remove('Flux_Values_9.txt')
    os.remove('Flux_Values_10.txt')
    


#Creates the files containing the data for the target star and the reference stars
f = open('Flux_Values_Main.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_1.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_2.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_3.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_4.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_5.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_6.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_7.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_8.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_9.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

f = open('Flux_Values_10.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()


#Load image times
time_data = np.loadtxt('ImageTimes.txt', dtype=str)

#Open and extract data from each file one at a time
for i in range (1,400):
    if i<10:
        filename = "Lab_1_HAT-P-27b_science_exposures.0000000" + str(i) + ".FIT_bias.fits_dark.fits_final.new.cat"
    
    elif i<100:
        filename = "Lab_1_HAT-P-27b_science_exposures.000000" + str(i) + ".FIT_bias.fits_dark.fits_final.new.cat"
    
    else:
        filename = "Lab_1_HAT-P-27b_science_exposures.00000" + str(i) + ".FIT_bias.fits_dark.fits_final.new.cat"
    
    data  = np.loadtxt(filename, skiprows = 17)
    last_line = data[:][-1]
    last_value = int(last_line[0])
    
    e_ra = 0.0007
    e_dec = 0.0007
    count = 0
    count_m = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    tm = time.strptime(time_data[(i-1)], '%H:%M:%S.%f')
    tm = datetime.timedelta(hours=tm.tm_hour,minutes=tm.tm_min,seconds=tm.tm_sec).total_seconds()/60
    
    
    #Write data for each star to a text file
    for j in range (0, last_value):
        ra = data[j][3]
        dec = data[j][4]
        flux = data[j][5]
        err = data[j][6]
        
        if abs(ra-222.7673)<e_ra and abs(dec-5.9474)<e_dec:
            f = open('Flux_Values_Main.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_m = 1
        elif abs(ra-222.8092)<e_ra and abs(dec-5.9498)<e_dec:
            f = open('Flux_Values_1.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_1 = 1
        elif abs(ra-222.8852)<e_ra and abs(dec-6.0515)<e_dec:
            f = open('Flux_Values_2.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_2 = 1
        elif abs(ra-222.6405)<e_ra and abs(dec-5.8399)<e_dec:
            f = open('Flux_Values_3.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_3=1
        elif abs(ra-222.5721)<e_ra and abs(dec-5.9430)<e_dec:
            f = open('Flux_Values_4.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_4=1
        elif abs(ra-222.9342)<e_ra and abs(dec-5.8219)<e_dec:
            f = open('Flux_Values_5.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_5=1
        elif abs(ra-222.7551)<e_ra and abs(dec-6.0705)<e_dec:
            f = open('Flux_Values_6.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_6=1
        elif abs(ra-222.7304)<e_ra and abs(dec-6.0506)<e_dec:
            f = open('Flux_Values_7.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_7=1
        elif abs(ra-222.7833)<e_ra and abs(dec-5.7665)<e_dec:
            f = open('Flux_Values_8.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_8=1
        elif abs(ra-222.6193)<e_ra and abs(dec-5.8978)<e_dec:
            f = open('Flux_Values_9.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_9=1
        elif abs(ra-222.8507)<e_ra and abs(dec-6.0263)<e_dec:
            f = open('Flux_Values_10.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_10=1    
        
    if count != 11:
        if count_m !=1:
            print('Main')
        elif count_1 !=1:
           print('1')
        elif count_2 !=1:
            print('2')
        elif count_3 !=1:
            print('3')
        elif count_4 !=1:
            print('4')
        elif count_5 !=1:
            print('5')
        elif count_6 !=1:
            print('6')
        elif count_7 !=1:
            print('7')
        elif count_8 !=1:
            print('8')
        elif count_9 !=1:
            print('9')
        elif count_10 !=1:
            print('10')

