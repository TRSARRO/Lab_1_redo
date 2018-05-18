import matplotlib.pyplot as plt
import numpy as np
import csv


#Function to exctract time, flux, and flux error from the star data files, produce normalized fluxes/errors
def Extract_Data(filename):
    f =  open(filename)
    file = csv.reader(f)
    time = []
    flux = []
    err = []
    norm_flux = []
    norm_err = []
    for row in file:
        time.append(row[0])
        flux.append(row[1])
        err.append(row[2])
    
    time_new = time[1:-1]
    flux_new = flux[1:-1]
    err_new = err[1:-1]
    time_list = list(map(float, time_new))
    flux_list = list(map(float, flux_new))
    err_list = list(map(float, err_new))
    
    u_flux = np.mean(flux_list)
    for x in flux_list:
        normfl = x/u_flux
        norm_flux.append(normfl)
        
    for y in err_list:
        normer = y/u_flux
        norm_err.append(normer)
        
    i = 0
    while i < len(norm_flux): 
        if norm_flux[i] < 0.89:
            norm_flux[i] = None
            norm_err[i] = None
        i = i + 1
        
    return time_list, flux_list, err_list, norm_flux, norm_err



#Use the Extract_Data function to load the desired data into variables
time_main, flux_main, err_main, norm_flux_main, norm_err_main = Extract_Data('Flux_Values_Main.txt')
time_1, flux_1, err_1, norm_flux_1, norm_err_1 = Extract_Data('Flux_Values_1.txt')
time_2, flux_2, err_2, norm_flux_2, norm_err_2 = Extract_Data('Flux_Values_2.txt')
time_3, flux_3, err_3, norm_flux_3, norm_err_3 = Extract_Data('Flux_Values_3.txt')
time_4, flux_4, err_4, norm_flux_4, norm_err_4 = Extract_Data('Flux_Values_4.txt')
time_5, flux_5, err_5, norm_flux_5, norm_err_5 = Extract_Data('Flux_Values_5.txt')
time_6, flux_6, err_6, norm_flux_6, norm_err_6 = Extract_Data('Flux_Values_6.txt')
time_7, flux_7, err_7, norm_flux_7, norm_err_7 = Extract_Data('Flux_Values_7.txt')
time_8, flux_8, err_8, norm_flux_8, norm_err_8 = Extract_Data('Flux_Values_8.txt')
time_9, flux_9, err_9, norm_flux_9, norm_err_9 = Extract_Data('Flux_Values_9.txt')
time_10, flux_10, err_10, norm_flux_10, norm_err_10 = Extract_Data('Flux_Values_10.txt')


#Array of the normalized fluxes (and errors) from each star being analyzed
norm_flux_r = [norm_flux_1,norm_flux_2,norm_flux_4,norm_flux_6,norm_flux_7,norm_flux_9]
norm_err_r = [norm_err_1,norm_err_2,norm_err_4,norm_err_6,norm_err_7,norm_err_9]


#Normalize Fluxes
norm_flux = []
norm_err = []

for i in range(0, len(norm_flux_1)):
    numerator = 0
    denominator = 0
    for j in range(0, len(norm_flux_r)):
        f = norm_flux_r[j][i]
        sig = norm_err_r[j][i]
        if f == None:
            pass
        else:
            numerator = numerator + (f / (sig**2.0))
            denominator = denominator + (1.0/(sig**2.0))
    norm_flux.append(numerator/denominator)
    norm_err.append((1.0/denominator)**0.5)



#Plot normaized fluxex
plt.figure()
plt.plot(time_main,norm_flux_main, label = 'Target')
plt.xlabel('Time [min]')
plt.ylabel('Normalized Flux')
plt.plot(time_1,norm_flux_1, label = '1')
plt.plot(time_2,norm_flux_2, label = '2')
#plt.plot(time_3,norm_flux_3, label = '3')
plt.plot(time_4,norm_flux_4, label = '4')
#plt.plot(time_5,norm_flux_5, label = '5')
plt.plot(time_6,norm_flux_6, label = '6')
plt.plot(time_7,norm_flux_7, label = '7')
#plt.plot(time_8,norm_flux_8, label = '8')
plt.plot(time_9,norm_flux_9, label = '9')
#plt.plot(time_10,norm_flux_10, label = '10')
plt.plot(time_main, norm_flux, label = 'avg')
plt.legend(loc = 'best')
plt.show()
