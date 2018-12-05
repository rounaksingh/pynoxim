import yaml
import subprocess
import math
import numpy as np
from pathlib import Path
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def createNoximYAMLConfig(YAMLConfigFilename='test.yaml', dim_x=4,dim_y=4,use_winoc=False,injectionRate=0.01):
	YAMLConfig='''
# Simple config of a 16x16 mesh with 4 RadioHubs
# Each parameter is overwritten when corresponding command line value is set
#
# NOC & WIRED CONFIGURATION
#
#
# X and Y mesh sizes
mesh_dim_x: '''+str(dim_x)+'''
mesh_dim_y: '''+str(dim_y)+'''
# number of flits for each router buffer
buffer_depth: 2
# size of flits, in bits
flit_size: 32
# lenght in mm of router to hub connection
r2h_link_length: 2.0
# lenght in mm of router to router connection
r2r_link_length: 1.0
n_virtual_channels: 4

# Routing algorithms:
#   XY
#   WEST_FIRST
#   NORTH_LAST
#   NEGATIVE_FIRST
#   ODD_EVEN
#   DYAD
#   TABLE_BASED
# Each of the above labels should match a corresponding
# implementation in the routingAlgorithms source code directory
routing_algorithm: DYAD
routing_table_filename: ""

# Routing specific parameters
#   dyad_threshold: double
dyad_threshold: 0.1

# Selection Strategies:
#   RANDOM
#   BUFFER_LEVEL
#   NOP
# Each of the above labels should match a corresponding
# implementation in the selectionStrategies source code directory
selection_strategy: RANDOM

#
# WIRELESS CONFIGURATION
#
Hubs:
    defaults:
    # channels from which Hub can receive/transmit
        rx_radio_channels: [0]
        tx_radio_channels: [0]
    # list of node tiles attached to the hub
        attached_nodes: []
    # size of buffers connecting the hub to tiles
        to_tile_buffer_size: 4
        from_tile_buffer_size: 4
    # size of antenna tx/rx
        rx_buffer_size: 64
        tx_buffer_size: 64

# for each hub, the same parameters specified above can be customized
# If not specified, the above default values will be used
# What is usually needed to be customized specifically for each hub is
# the set of nodes that are connected to it. In this simple topology
# we have 4 hubs (0-3) connected to the four nodes of the 2x2
# sub-meshes
'''+generate_hub_connections(dim_x,dim_y,use_winoc)+'''

#
# Transmission channels configuration
# each channel modelizes the transmission over a given frequency that
# can be used by a set of communicating hubs
RadioChannels:
    defaults:
    # data rate in Gb/s affect the number of cycles required for a
    # flit transmission
        data_rate: 16
    # bit error rate (CURRENTLY UNSUPPORTED)
        ber: [0, 0]
    # mac policies:

    # who has the token releas only when a complete packet has
    # been sent
        #[TOKEN_PACKET]

    # who has the token, release only after a fixed number of
    # cycles, even no transmission is occurring
        #[TOKEN_HOLD, num_hold_cycles]

    # who has the token, holds the packet until needed for
    # transmissions, until a max number of cycles is reached
        #[TOKEN_MAX_HOLD, max_hold_cycles]

        mac_policy: [TOKEN_PACKET]

#
# SIMULATION PARAMETERS
#
clock_period_ps: 1000
# duration of reset signal assertion, expressed in cycles
reset_time: 1000
# overal simulation lenght, expressed in cycles
simulation_time: 20000
# collect stats after a given number of cycles
stats_warm_up_time: 1000
# power breakdown, nodes communication details
detailed: false
# stop after a given amount of load has been processed
max_volume_to_be_drained: 0
show_buffer_stats: false

# Winoc
# enable wireless, when false, all wireless channel configuration is
# ignored
use_winoc: '''+str(use_winoc).lower()+'''
# experimental power saving strategy
use_wirxsleep: false

# Verbosity level:
#   VERBOSE_OFF
#   VERBOSE_LOW
#   VERBOSE_MEDIUM
#   VERBOSE_HIGH
verbose_mode: VERBOSE_OFF

# Trace
trace_mode: false
trace_filename: ""

min_packet_size: 64
max_packet_size: 64
packet_injection_rate: '''+str(injectionRate/64)+'''
probability_of_retransmission: 0.01

# Traffic distribution:
#   TRAFFIC_RANDOM
#   TRAFFIC_TRANSPOSE1
#   TRAFFIC_TRANSPOSE2
#   TRAFFIC_HOTSPOT
#   TRAFFIC_TABLE_BASED
#   TRAFFIC_BIT_REVERSAL
#   TRAFFIC_SHUFFLE
#   TRAFFIC_BUTTERFLY
traffic_distribution: TRAFFIC_RANDOM
# when traffic table based is specified, use the following
# configuration file
traffic_table_filename: "t.txt" '''

	with open(YAMLConfigFilename,'w') as configFile:
		print(YAMLConfig,file=configFile)

# It will print the message on screen and also log it in the file
def noxim_log(logme):
	print(logme)
	with open('noxim.log','a') as logFile:
		print(logme,file=logFile)

def get_nowtime():
	return '{:%Y%m%d_%H%M%S_}'.format(datetime.today())

# Saves the results as a table
def save_results(results,results_header):
	np.savetxt(get_nowtime()+"results.csv", results, delimiter=",",header=results_header)

# For mesh only and requires dim_x and dim_y to be multiple of 2, but dim_x>2 or dim_y>2
def generate_hub_connections(dim_x=4,dim_y=4, use_winoc=False):
	if use_winoc==False:
		return ''
	else:
		num_hub=dim_x/2*dim_y/2
		hub=[[] for i in range(int(num_hub))]

		for i in range(dim_x):
		  for j in range(dim_y):
		    hub_id=int(dim_y/2)*int(i/2)+int(j/2)
		    hub[hub_id].append(int(dim_y*i+j))
		a=''
		for i in range(int(num_hub)):
		    a=a+'    '+str(i)+':\n        attached_nodes: '+str(hub[i])+'\n'
		return a
'''
    0:
        attached_nodes: [0,1,4,5]

    1:
        attached_nodes: [2,3,6, 7]

    2:
        attached_nodes: [8,9,12,13]

    3:
        attached_nodes: [10,11,14,15]
'''


'''




'''
if __name__=='__main__':
	noximBinPath='/home/rn5949/noxim/noxim/bin'
	noximConfigFilePath='test.yaml'

	annotation_marker=['o','+','s','d','^','*','x','<']

	logFile=Path('./noxim.log')
	if logFile.is_file():
		logFile.unlink()

	#figures for throughput and delay
	f1=plt.figure(1)
	ax1=f1.add_subplot(111)
	f2=plt.figure(2)
	ax2=f2.add_subplot(111)
	
	# the injection Load is in flit/cycle.
	# In YAML file, injection load should be in packet/cycle.
	injectionL= np.arange(0.15,0.3,0.05)
	#WiNoC=True
	WiNoC=True
	
	for core_it in range(8,10,2):
		dim_mesh=core_it
		tp=[]
		delay=[]
		for i in injectionL:
			noxim_log('=================================================\
			\nRunning Noxim for mesh of '+str(dim_mesh)+'x'+str(dim_mesh)+' with Injection Load of '+str(i)+' at '+str(datetime.now()))

			createNoximYAMLConfig(noximConfigFilePath,dim_mesh,dim_mesh,WiNoC,i)
			
			# Runs the shell command for noxim
			#returnedVal=subprocess.check_output(noximBinPath+'/noxim'+' -config '+noximConfigFilePath+' -power '+noximBinPath+'/power.yaml',shell=True,stderr=subprocess.STDOUT)
			returnedVal=subprocess.check_output(noximBinPath+'/noxim'+' -config '+noximConfigFilePath+' -power '+noximBinPath+'/power.yaml',shell=True)
			returnedVal=returnedVal.decode('utf-8')
			
			# log returned output from noxim
			#print(logme)
			noxim_log(returnedVal)

			#Split the output using '%' as dilimiter
			splittedStr=returnedVal.split('%')

			totalReceivedPackets=int(splittedStr[1].split(':')[1])
			totalReceivedFlits=int(splittedStr[2].split(':')[1])
			receivedFlitsRatio=float(splittedStr[3].split(':')[1])
			averageWirelessUtilization=float(splittedStr[4].split(':')[1])
			globalAverageDelay=float(splittedStr[5].split(':')[1])
			maxDelay=float(splittedStr[6].split(':')[1])
			networkThroughput=float(splittedStr[7].split(':')[1])
			averageIPThroughput=float(splittedStr[8].split(':')[1])
			totalEnergy=float(splittedStr[9].split(':')[1])
			dynamicEnergy=float(splittedStr[10].split(':')[1])
			staticEnergy=float(splittedStr[11].split(':')[1])

			# Save throughput and delay
			tp.append(averageIPThroughput)
			delay.append(globalAverageDelay)

		results_matrix=np.column_stack((injectionL,tp,delay))
		save_results(results_matrix,'injectionLoad,throughput,delay')

		#
		noxim_log('=================================================')
		noxim_log('injectionLoad 	throughput 		delay')
		noxim_log(str(results_matrix))
		noxim_log('=================================================')
		'''noxim_log('injectionLoad:'+str(injectionL))
		noxim_log('throughput:'+str(tp))
		noxim_log('delay:'+str(delay))'''

		# plotting
		ax1.plot(injectionL,tp,'r'+annotation_marker[core_it-2],injectionL,tp,'k')
		ax2.plot(injectionL,delay,'r'+annotation_marker[core_it-2],injectionL,delay,'k')
		#plt.draw()
	
	ax1.set_ylim(0, 1)
	ax1.set_ylabel('averageIPThroughput (flit/cycle/IP)')
	ax1.set_xlim(min(injectionL),max(injectionL))
	ax1.set_xlabel('Injection Load (flit/cycle)')
	ax1.grid(True)
	
	#ax2.set_ylim()
	ax2.set_ylabel('delay (cycles)')
	ax2.set_xlim(min(injectionL),max(injectionL))
	ax2.set_xlabel('Injection Load (flit/cycle)')
	ax2.grid(True)

	# Export the results
	f1.savefig(get_nowtime()+'f1.png')
	f2.savefig(get_nowtime()+'f2.png')


'''
import matplotlib.pyplot as plt
f1=plt.figure(1)
ax1=f1.add_subplot(111)
p1=ax1.plot([1,2,3])
f1.show()
'''
