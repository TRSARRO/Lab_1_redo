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



#Function to calculate error based on varience
def average_err(values):
    avg = sum(values)/len(values)
    s = 0
    for j in range(0,len(values)):
        s = s + (values[j] - avg)**2.0
    
    var = s/len(values)
    sd = var**0.5
    err = sd/(len(values)*0.5)
    return err


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


#Arrays for normalized fluxes, ratios
norm_flux = []
norm_err = []
main_ratio = []
main_ratio_err = []

#Calculate weighted mean of reference fluxes
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
    
    main_ratio.append(flux_main[i]/norm_flux[i])
    main_ratio_err.append(((err_main[i]/norm_flux[i])**(2.0)+(flux_main[i]*norm_err[i]/(norm_flux[i]**(2.0)))**(2.0))**(0.5))



#Calculate baseline flux based on non-transit, main fluxes
base_flux = []
base_err = []
for i in range(0, 60):
    base_flux.append(flux_main[i])

for i in range(310, len(flux_main)):
    base_flux.append(flux_main[i])

baseline_flux = sum(base_flux)/len(base_flux)



#Normalize the main ratio by the baseline flux
norm_flux_final = []
norm_err_final = []
for i in range(0, len(main_ratio)):
    norm_flux_final.append(main_ratio[i]/baseline_flux)
    norm_err_final.append(main_ratio_err[i]/baseline_flux)

norm_flux_final = norm_flux_final[0:399]
norm_err_final = norm_err_final[0:399]


#Binning flux data
average_flux_final = []
average_err_final = []
new_time = []
binn = 7
num = 399 - binn
for i in range(0, num, binn):
    f = []
    for j in range(0,binn):
       f.append(norm_flux_final[j+i])
    average_flux_final.append(sum(f)/len(f))
    new_time.append(time_main[i+(int(binn/2))])
    ae = average_err(f)
    average_err_final.append(ae)


#Calculate Average flux before, during, and after the transit. For use in dip analysis
norm_f_before = []
norm_f_during = []
norm_f_after = []
err_f_before = []
err_f_during = []
err_f_after = []

for i in range(0,60):
    norm_f_before.append(main_ratio[i]/baseline_flux)

for i in range(70, 295):
    norm_f_during.append(main_ratio[i]/baseline_flux)

for i in range(310, (len(main_ratio))):
    norm_f_after.append(main_ratio[i]/baseline_flux)


avg_f_before = sum(norm_f_before)/len(norm_f_before)
avg_err_before = average_err(norm_f_before)

avg_f_during = sum(norm_f_during)/len(norm_f_during)
avg_err_during = average_err(norm_f_during)

avg_f_after = sum(norm_f_after)/len(norm_f_after)
avg_err_after = average_err(norm_f_after)

avg_f_notduring = (sum(norm_f_before)+sum(norm_f_after))/(len(norm_f_before) + len(norm_f_after))
norm_f_notduring = sum([norm_f_before, norm_f_after], [])
avg_err_notduring = average_err(norm_f_notduring)

print('Average normalized flux before:', avg_f_before, '+/-', avg_err_before)
print('Average normalized flux during:', avg_f_during, '+/-', avg_err_during)
print('Average normalized flux after:', avg_f_after, '+/-', avg_err_after)
print('Average normalized flux not-during:', avg_f_notduring, '+/-', avg_err_notduring)



#Print light curve
plt.figure()
plt.errorbar(new_time,average_flux_final, yerr=average_err_final, fmt='o',  label = 'Target')
plt.xlabel('Time [min]')
plt.ylabel('Normalized Flux')
plt.legend(loc = 'best')
plt.show()
