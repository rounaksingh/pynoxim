from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime

def find_rows_of_results(results,parameter_index, parameter_value):
    return results[np.where(results[:,parameter_index]==parameter_value)[0],:]

def get_nowtime():
    return '{:%Y%m%d_%H%M%S_}'.format(datetime.today())



ms=10
ANNOTATION_MARKER=['o','+','s','d','^','*','x','<']
ANNOTATION_LINE=['-','--','.-',':']
ANNOTATION_COLOR=['r','b','g','m']

'''
# Mesh Size
a = np.genfromtxt('20181210_130558_results.csv', delimiter=',')
x_lim = ([0.01, 0.3])
y_lim = ([0, 0.25])
x_label = 'Injection Load (flits/cycle/IP)'
y_label = 'Throughput (flits/cycle/IP)'

# Mesh Size plotting
f=plt.figure();
ax=f.add_subplot(111)
annotate_index=0
for index in [4,6,8,10]:
	b=find_rows_of_results(a,0,index)
	ax.plot(b[:,1],b[:,13],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms, fillstyle='none')
	annotate_index=annotate_index+1

ax.set_ylim(min(y_lim),max(y_lim))
ax.set_ylabel(y_label)
ax.set_xlim(min(x_lim),max(x_lim))
ax.set_xlabel(x_label)
ax.grid(True)
ax.legend(['Mesh 4x4 - XY','Mesh 6x6 - XY', 'Mesh 8x8 - XY', 'Mesh 10x10 - XY'], loc='upper left')
f.savefig(get_nowtime()+'f.png')
'''

'''
# Size of flit with constant packet size
a = np.genfromtxt('20181214_204242_results.csv', delimiter=',')
x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load (flits/cycle/IP)'
y_label = 'Throughput (flits/cycle/IP)'

# Mesh Size plotting
f1=plt.figure()
f2=plt.figure()
ax1=f1.add_subplot(111)
ax2=f2.add_subplot(111)
annotate_index=0
for index in [16,32,64,128]:
	b=find_rows_of_results(a,4,index)
	# throughput
	ax1.plot(b[:,1],b[:,13],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms, fillstyle='none')
	# delay
	ax2.plot(b[:,1],b[:,10],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms, fillstyle='none')

	annotate_index=annotate_index+1

ax1.set_ylim(min(y_lim),max(y_lim))
ax1.set_ylabel(y_label)
ax1.set_xlim(min(x_lim),max(x_lim))
ax1.set_xlabel(x_label)
ax1.grid(True)
ax1.legend(['flitSize=16','flitSize=32', 'flitSize=64', 'flitSize=128'], loc='upper left')
f1.savefig(get_nowtime()+'f1.png')

ax2.set_ylim(min(b[:,10]),1000)
ax2.set_ylabel('Delay (cycles)')
ax2.set_xlim(min(x_lim),max(x_lim))
ax2.set_xlabel(x_label)
ax2.grid(True)
ax2.legend(['flitSize=16','flitSize=32', 'flitSize=64', 'flitSize=128'], loc='upper left')
f2.savefig(get_nowtime()+'f2.png')
'''

''' Iterations
# Error - Repeating the experiment
x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load (flits/cycle/IP)'
y_label = 'Throughput (flits/cycle/IP)'

# plotting
f=plt.figure();
ax=f.add_subplot(111)

annotate_index=0
a = np.genfromtxt('20181210_205342_results.csv', delimiter=',')
b=find_rows_of_results(a,2,7)
ax.plot(b[:,1],b[:,13],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms, fillstyle='none')

annotate_index=1
a = np.genfromtxt('20181211_124203_results.csv', delimiter=',')
b=find_rows_of_results(a,2,7)
ax.plot(b[:,1],b[:,13],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms, fillstyle='none')

annotate_index=2
a = np.genfromtxt('20181210_162321_results.csv', delimiter=',')
b=find_rows_of_results(a,2,7)
ax.plot(b[:,1],b[:,13],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms, fillstyle='none')

ax.set_ylim(min(y_lim),max(y_lim))
ax.set_ylabel(y_label)
ax.set_xlim(min(x_lim),max(x_lim))
ax.set_xlabel(x_label)
ax.grid(True)
ax.legend(['1st iteration','2nd iteration', '3rd iteration'], loc='upper left')
f.savefig(get_nowtime()+'f.png')
'''

''' Routing Algo
#a = np.genfromtxt('20181210_162321_results.csv', delimiter=',')
a = np.genfromtxt('20181210_163624_results.csv', delimiter=',')
x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load (flits/cycle/IP)'
y_label = 'Throughput (flits/cycle/IP)'

# plotting
f=plt.figure();
ax=f.add_subplot(111)
annotate_index=0
for index in [0,4,7]:
	b=find_rows_of_results(a,2,index)
	ax.plot(b[:,1],b[:,13],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms, fillstyle='none')
	annotate_index=annotate_index+1

ax.set_ylim(min(y_lim),max(y_lim))
ax.set_ylabel(y_label)
ax.set_xlim(min(x_lim),max(x_lim))
ax.set_xlabel(x_label)
ax.grid(True)
ax.legend(['XY','Odd-Even', 'XY+Wireless'], loc='upper left')
f.savefig(get_nowtime()+'f.png')
'''

'''
#Delta
f1=plt.figure(1)
f2=plt.figure(2)
f3=plt.figure(3)
ax1=f1.add_subplot(111)
ax2=f2.add_subplot(111)
ax3=f3.add_subplot(111)

# delta 3
a = np.genfromtxt('20181212_231148_results.csv', delimiter=',')
b = find_rows_of_results(a,2,7)
ax1.plot(b[:,1],b[:,13],'-ro', markersize=ms, fillstyle='none')
ax2.plot(b[:,1],b[:,8],'-ro', markersize=ms, fillstyle='none')
ax3.plot(b[:,1],b[:,7],'-ro', markersize=ms, fillstyle='none')

# delta 4
a = np.genfromtxt('20181212_232200_results.csv', delimiter=',')
b = find_rows_of_results(a,2,7)
ax1.plot(b[:,1],b[:,13],'-b+', markersize=ms, fillstyle='none')
ax2.plot(b[:,1],b[:,8],'-b+', markersize=ms, fillstyle='none')
ax3.plot(b[:,1],b[:,7],'-b+', markersize=ms, fillstyle='none')

# delta 5
a = np.genfromtxt('20181212_232843_results.csv', delimiter=',')
b = find_rows_of_results(a,2,7)
ax1.plot(b[:,1],b[:,13],'-gs', markersize=ms, fillstyle='none')
ax2.plot(b[:,1],b[:,8],'-gs', markersize=ms, fillstyle='none')
ax3.plot(b[:,1],b[:,7],'-gs', markersize=ms, fillstyle='none')

# delta 6
a = np.genfromtxt('20181212_233647_results.csv', delimiter=',')
b = find_rows_of_results(a,2,7)
ax1.plot(b[:,1],b[:,13],'-m^', markersize=ms, fillstyle='none')
ax2.plot(b[:,1],b[:,8],'-m^', markersize=ms, fillstyle='none')
ax3.plot(b[:,1],b[:,7],'-m^', markersize=ms, fillstyle='none')

# delta 7
a = np.genfromtxt('20181212_234938_results.csv', delimiter=',')
b = find_rows_of_results(a,2,7)
ax1.plot(b[:,1],b[:,13],'--rd', markersize=ms, fillstyle='none')
ax2.plot(b[:,1],b[:,8],'--rd', markersize=ms, fillstyle='none')
ax3.plot(b[:,1],b[:,7],'--rd', markersize=ms, fillstyle='none')

# delta 8
a = np.genfromtxt('20181213_000248_results.csv', delimiter=',')
b = find_rows_of_results(a,2,7)
ax1.plot(b[:,1],b[:,13],'--b*', markersize=ms, fillstyle='none')
ax2.plot(b[:,1],b[:,8],'--b*', markersize=ms, fillstyle='none')
ax3.plot(b[:,1],b[:,7],'--b*', markersize=ms, fillstyle='none')

# XY only, no wireless 20181213_001733_results
a = np.genfromtxt('20181213_001733_results.csv', delimiter=',')
b = find_rows_of_results(a,2,0)
ax1.plot(b[:,1],b[:,13],'--k', markersize=ms, fillstyle='none')
ax2.plot(b[:,1],b[:,8],'--k', markersize=ms, fillstyle='none')
ax3.plot(b[:,1],b[:,7],'--k', markersize=ms, fillstyle='none')

x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load (flits/cycle/IP)'
y_label = 'Throughput (flits/cycle/IP)'
ax1.set_ylim(min(y_lim),max(y_lim))
ax1.set_ylabel(y_label)
ax1.set_xlim(min(x_lim),max(x_lim))
ax1.set_xlabel(x_label)
ax1.grid(True)
ax1.legend(['delta=3','delta=4', 'delta=5', 'delta=6', 'delta=7', 'delta=8', 'No Wireless'], loc='upper left')

x_lim = ([0.01, 0.3])
y_lim = ([0, 3000])
x_label = 'Injection Load (flits/cycle/IP)'
y_label = 'Delay (cycles)'
ax2.set_ylim(min(y_lim),max(y_lim))
ax2.set_ylabel(y_label)
ax2.set_xlim(min(x_lim),max(x_lim))
ax2.set_xlabel(x_label)
ax2.grid(True)
ax2.legend(['delta=3','delta=4', 'delta=5', 'delta=6', 'delta=7', 'delta=8', 'No Wireless'], loc='upper left')

x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load (flits/cycle/IP)'
y_label = 'Average Wireless Utilization'
ax3.set_ylim(min(y_lim),max(y_lim))
ax3.set_ylabel(y_label)
ax3.set_xlim(min(x_lim),max(x_lim))
ax3.set_xlabel(x_label)
ax3.grid(True)
ax3.legend(['delta=3','delta=4', 'delta=5', 'delta=6', 'delta=7', 'delta=8', 'No Wireless'], loc='upper left')

f1.savefig(get_nowtime()+'f1.png')
f2.savefig(get_nowtime()+'f2.png')
f3.savefig(get_nowtime()+'f3.png')
'''

#Virtual Channels plotting
a = np.genfromtxt('20181214_220652_results.csv', delimiter=',')
b=find_rows_of_results(a,3,2)

f=plt.figure();
ax=f.add_subplot(111)
ax.plot(b[:,1],b[:,13],'-ro', markersize=ms, fillstyle='none')

#f=pn.plot_throughput(b[:,1],b[:,9], 'Injection Load (flits/cycle/IP)', 'Throughput (flits/cycle/IP)', ([0.01, 0.2]), ([0, 0.3]), '-ro','mesh 8x8 XY')
b=find_rows_of_results(a,3,4)
ax.plot(b[:,1],b[:,13],'-b*', markersize=ms, fillstyle='none')

b=find_rows_of_results(a,3,6)
ax.plot(b[:,1],b[:,13],'-gs', markersize=ms, fillstyle='none')

b=find_rows_of_results(a,3,8)
ax.plot(b[:,1],b[:,13],'-md', markersize=ms, fillstyle='none')

#f=pn.plot_throughput(f,b[:,1],b[:,9], 'Injection Load (flits/cycle/IP)', 'Throughput (flits/cycle/IP)', ([0.01, 0.2]), ([0, 0.3]), '-b*','mesh 8x8 ')
#a=pn.compare_config_routing_algorithm(injection_load_range=np.arange(0.01,0.2,0.05),routing_algorithm_indices_in_list=[0],use_winoc=False)
#pn.plot_throughput(a[:,1],a[:,9], 'Injection Load (flits/cycle/IP)', 'Throughput (flits/cycle/IP)', ([0.01, 0.2]), ([0, 0.3]), '-ro','mesh 8x8')

x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load (flits/cycle/IP)'
y_label = 'Throughput (flits/cycle/IP)'

ax.set_ylim(min(y_lim),max(y_lim))
ax.set_ylabel(y_label)
ax.set_xlim(min(x_lim),max(x_lim))
ax.set_xlabel(x_label)
ax.grid(True)
ax.legend(['XY VC=2','XY VC=4', 'XY VC=6', 'XY VC=8'])
f.savefig(get_nowtime()+'f.png')
#


'''
# Multiple channel plotting
# Single channel - 16Gbps
a = np.genfromtxt('20181211_140720_results.csv', delimiter=',')

f=plt.figure();
ax=f.add_subplot(111)

#b=find_rows_of_results(a,3,1)
ax.plot(a[:,1],a[:,13],'-ro', markersize=ms, fillstyle='none')

# Two channel - 8Gbps
#b = np.genfromtxt('20181211_141340_results.csv', delimiter=',')
b = np.genfromtxt('20181211_143100_results.csv', delimiter=',')
ax.plot(b[:,1],b[:,13],'-b*', markersize=ms, fillstyle='none')

x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load (flits/cycle/IP)'
y_label = 'Throughput (flits/cycle/IP)'

ax.set_ylim(min(y_lim),max(y_lim))
ax.set_ylabel(y_label)
ax.set_xlim(min(x_lim),max(x_lim))
ax.set_xlabel(x_label)
ax.grid(True)
ax.legend(['One channel - 16Gbps','Two channels - 8Gbps'])
f.savefig(get_nowtime()+'f.png')
'''

