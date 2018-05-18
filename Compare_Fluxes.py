import matplotlib.pyplot as plt
import csv



filename = 'Flux_Values_Main.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_main = time[1:-1]
flux_main = flux[1:-1]
err_main = err[1:-1]


filename = 'Flux_Values_1.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_1 = time[1:-1]
flux_1 = flux[1:-1]
err_1 = err[1:-1]


filename = 'Flux_Values_2.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_2 = time[1:-1]
flux_2 = flux[1:-1]
err_2 = err[1:-1]


filename = 'Flux_Values_3.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_3 = time[1:-1]
flux_3 = flux[1:-1]
err_3 = err[1:-1]


filename = 'Flux_Values_4.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_4 = time[1:-1]
flux_4 = flux[1:-1]
err_4 = err[1:-1]


filename = 'Flux_Values_5.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_5 = time[1:-1]
flux_5 = flux[1:-1]
err_5 = err[1:-1]


filename = 'Flux_Values_6.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_6 = time[1:-1]
flux_6 = flux[1:-1]
err_6 = err[1:-1]


filename = 'Flux_Values_7.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_7 = time[1:-1]
flux_7 = flux[1:-1]
err_7 = err[1:-1]


filename = 'Flux_Values_8.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_8 = time[1:-1]
flux_8 = flux[1:-1]
err_8 = err[1:-1]


filename = 'Flux_Values_9.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_9 = time[1:-1]
flux_9 = flux[1:-1]
err_9 = err[1:-1]


filename = 'Flux_Values_10.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_10 = time[1:-1]
flux_10 = flux[1:-1]
err_10 = err[1:-1]



plt.figure(1)
plt.plot(time_main,flux_main, label = 'Main')
plt.xlabel('Time [min]')
plt.ylabel('Flux [counts]')

plt.plot(time_1,flux_1,label = '1')


plt.plot(time_2,flux_2,label = '2')


plt.plot(time_3,flux_3,label = '3')


plt.plot(time_4,flux_4,label = '4')


plt.plot(time_5,flux_5,lable = '5')


plt.plot(time_6,flux_6,label = '6')


plt.plot(time_7,flux_7,label = '7')


plt.plot(time_8,flux_8,label = '8')


plt.plot(time_9,flux_9,label = '9')


plt.plot(time_10,flux_10,label = '10')


plt.legend(loc = 'best')
plt.show()
