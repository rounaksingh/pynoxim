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


''' Mesh Size
a = np.genfromtxt('20181210_130558_results.csv', delimiter=',')
x_lim = ([0.01, 0.3])
y_lim = ([0, 0.25])
x_label = 'Injection Load'
y_label = 'Throughput (flits/cycle/IP)'

# Mesh Size plotting
f=plt.figure();
ax=f.add_subplot(111)
annotate_index=0
for index in [4,6,8,10]:
	b=find_rows_of_results(a,0,index)
	ax.plot(b[:,1],b[:,11],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms)
	annotate_index=annotate_index+1

ax.set_ylim(min(y_lim),max(y_lim))
ax.set_ylabel(y_label)
ax.set_xlim(min(x_lim),max(x_lim))
ax.set_xlabel(x_label)
ax.grid(True)
ax.legend(['Mesh 4x4 XY','Mesh 6x6 XY', 'Mesh 8x8 XY', 'Mesh 10x10 XY'], loc='upper left')
f.savefig(get_nowtime()+'f.png')
'''


# Error - Repeating the experiment
x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load'
y_label = 'Throughput (flits/cycle/IP)'

# plotting
f=plt.figure();
ax=f.add_subplot(111)

annotate_index=0
a = np.genfromtxt('20181210_205342_results.csv', delimiter=',')
b=find_rows_of_results(a,2,7)
ax.plot(b[:,1],b[:,11],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms)

annotate_index=1
a = np.genfromtxt('20181211_124203_results.csv', delimiter=',')
b=find_rows_of_results(a,2,7)
ax.plot(b[:,1],b[:,11],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms)

annotate_index=2
a = np.genfromtxt('20181210_162321_results.csv', delimiter=',')
b=find_rows_of_results(a,2,7)
ax.plot(b[:,1],b[:,11],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms)

ax.set_ylim(min(y_lim),max(y_lim))
ax.set_ylabel(y_label)
ax.set_xlim(min(x_lim),max(x_lim))
ax.set_xlabel(x_label)
ax.grid(True)
ax.legend(['XY','Odd-Even', 'XY+Wireless'], loc='upper left')
f.savefig(get_nowtime()+'f.png')


''' Routing Algo
#a = np.genfromtxt('20181210_162321_results.csv', delimiter=',')
a = np.genfromtxt('20181210_163624_results.csv', delimiter=',')
x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load'
y_label = 'Throughput (flits/cycle/IP)'

# plotting
f=plt.figure();
ax=f.add_subplot(111)
annotate_index=0
for index in [0,4,7]:
	b=find_rows_of_results(a,2,index)
	ax.plot(b[:,1],b[:,11],ANNOTATION_LINE[0]+ANNOTATION_COLOR[annotate_index]+ANNOTATION_MARKER[annotate_index], markersize=ms)
	annotate_index=annotate_index+1

ax.set_ylim(min(y_lim),max(y_lim))
ax.set_ylabel(y_label)
ax.set_xlim(min(x_lim),max(x_lim))
ax.set_xlabel(x_label)
ax.grid(True)
ax.legend(['XY','Odd-Even', 'XY+Wireless'], loc='upper left')
f.savefig(get_nowtime()+'f.png')
'''




'''Virtual Channels plotting
b=find_rows_of_results(a,3,1)
print(b)
f=plt.figure();
ax=f.add_subplot(111)
ax.plot(b[:,1],b[:,11],'-ro', markersize=ms)

#f=pn.plot_throughput(b[:,1],b[:,9], 'Injection Load', 'Throughput (flits/cycle/IP)', ([0.01, 0.2]), ([0, 0.3]), '-ro','mesh 8x8 XY')
b=find_rows_of_results(a,3,2)
ax.plot(b[:,1],b[:,11],'-b*', markersize=ms)

b=find_rows_of_results(a,3,3)
ax.plot(b[:,1],b[:,11],'-gs', markersize=ms)

b=find_rows_of_results(a,3,4)
ax.plot(b[:,1],b[:,11],'-md', markersize=ms)

#f=pn.plot_throughput(f,b[:,1],b[:,9], 'Injection Load', 'Throughput (flits/cycle/IP)', ([0.01, 0.2]), ([0, 0.3]), '-b*','mesh 8x8 ')
#a=pn.compare_config_routing_algorithm(injection_load_range=np.arange(0.01,0.2,0.05),routing_algorithm_indices_in_list=[0],use_winoc=False)
#pn.plot_throughput(a[:,1],a[:,9], 'Injection Load', 'Throughput (flits/cycle/IP)', ([0.01, 0.2]), ([0, 0.3]), '-ro','mesh 8x8')

x_lim = ([0.01, 0.3])
y_lim = ([0, 0.15])
x_label = 'Injection Load'
y_label = 'Throughput (flits/cycle/IP)'

ax.set_ylim(min(y_lim),max(y_lim))
ax.set_ylabel(y_label)
ax.set_xlim(min(x_lim),max(x_lim))
ax.set_xlabel(x_label)
ax.grid(True)
ax.legend(['XY VC=1','XY VC=2', 'XY VC=3', 'XY VC=4'])
f.savefig(get_nowtime()+'f.png')
#
'''

