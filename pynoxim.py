import yaml
import subprocess
import math
import numpy as np
from pathlib import Path
from datetime import datetime
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
    

class Pynoxim:
    annotation_marker=['o','+','s','d','^','*','x','<']
    
    def __init__(self, noxim_bin_path=None, noxim_YAML_config_path='./.test.yaml', noxim_log_path='./.noxim.log'):
        self.noxim_bin_path=noxim_bin_path
        self.noxim_YAML_config_path=noxim_YAML_config_path
        self.noxim_log_path=noxim_log_path

        if self.noxim_bin_path is None or self.noxim_bin_path=='':
            print("You must enter the noxim binary path.")
        else:
            # Test the noxim bin path
            self.create_noxim_YAML_config()
            try:
                print('Finding and Testing Noxim... Please wait...')
                returnedVal=subprocess.check_output(self.noxim_bin_path+'/noxim'+' -config '+self.noxim_YAML_config_path+' -power '+noxim_bin_path+'/power.yaml',shell=True,stderr=subprocess.STDOUT)
                returnedVal=returnedVal.decode('utf-8')
                #print(returnedVal)
                print('Noxim Found!\nReady!')
            except:
                print("Noxim not found.\nPlease compile noxim and provide the correct noxim binary path.")


    def create_noxim_YAML_config(self, dim_x=4,dim_y=4,use_winoc=False,injectionRate=0.01):
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
'''+self.generate_hub_connections(dim_x,dim_y,use_winoc)+'''

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

        with open(self.noxim_YAML_config_path,'w') as configFile:
            print(YAMLConfig,file=configFile)

    # It will print the message on screen and also log it in the file
    def noxim_log(self,log_me,print_log=False,save_log=False):
        if print_log==True:
            print(log_me)
        if save_log==True:
            if self.noxim_log_path!='':
                with open(self.noxim_log_path,'a') as logFile:
                    print(log_me,file=logFile)

    def delete_log_file(self,log_file_name):
        temp_log_file_path=Path(log_file_name)
        if temp_log_file_path.is_file():
            temp_log_file_path.unlink()


    def get_nowtime(self):
        return '{:%Y%m%d_%H%M%S_}'.format(datetime.today())

    # Saves the results as a table
    def save_results(self, results,results_header):
        np.savetxt(self.get_nowtime()+"results.csv", results,  fmt='%.4G', delimiter=",",header=results_header)
        print('Output CSV file written!')

    # For mesh only and requires dim_x and dim_y to be multiple of 2, but dim_x>2 or dim_y>2
    def generate_hub_connections(self, dim_x=4,dim_y=4, use_winoc=False):
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
    def get_results(self,output_str):
        splittedStr=output_str.split('%')
        # 
        total_received_packets=int(splittedStr[1].split(':')[1])
        total_received_flits=int(splittedStr[2].split(':')[1])
        received_flits_ratio=float(splittedStr[3].split(':')[1])
        average_wireless_utilization=float(splittedStr[4].split(':')[1])
        global_average_delay=float(splittedStr[5].split(':')[1])
        max_delay=float(splittedStr[6].split(':')[1])
        network_throughput=float(splittedStr[7].split(':')[1])
        average_IP_throughput=float(splittedStr[8].split(':')[1])
        total_energy=float(splittedStr[9].split(':')[1])
        dynamic_energy=float(splittedStr[10].split(':')[1])
        static_energy=float(splittedStr[11].split(':')[1])

        return [total_received_packets, total_received_flits, received_flits_ratio, average_wireless_utilization, global_average_delay, max_delay, network_throughput, average_IP_throughput, total_energy, dynamic_energy, static_energy]

    def print_result_list(self,result_list):
        print('''
Total Received Packets: {}
Total Received Flits: {}
Received Flits Ratio: {}
Average Wireless Utilization: {}
Global Average Delay: {}
Max Delay: {}
Network Throughput: {}
Average IP Throughput: {}
Total Energy; {}
Dynamic Energy: {}
Static Energy: {}
'''.format(*result_list))

    def run(self):
        # Runs the shell command for noxim
        returnedVal=subprocess.check_output(self.noxim_bin_path+'/noxim'+' -config '+self.noxim_YAML_config_path+' -power '+self.noxim_bin_path+'/power.yaml',shell=True,stderr=subprocess.STDOUT)
        return returnedVal.decode('utf-8')

    def compare_config_injection_load(self,injection_load_range,mesh_dim_range,use_winoc=False):
        results=[]
        for core_it in mesh_dim_range:
            for i in injection_load_range:
                self.noxim_log('=================================================\
                \nRunning Noxim for mesh of '+str(core_it)+'x'+str(core_it)+' with Injection Load of '+'{:.8G}'.format(i)+' at '+str(datetime.now()),print_log=True,save_log=True)

                self.create_noxim_YAML_config(core_it,core_it,use_winoc,i)

                # Runs the shell command for noxim
                #returnedVal=subprocess.check_output(noxim_bin_path+'/noxim'+' -config '+noximConfigFilePath+' -power '+noxim_bin_path+'/power.yaml',shell=True,stderr=subprocess.STDOUT)
                returnedVal=self.run()

                # log returned output from noxim
                #print(returnedVal)
                #self.noxim_log(returnedVal,save_log=True)

                result=self.get_results(returnedVal)
                results.append([core_it,i]+result)
                self.print_result_list(result)

        results_matrix=np.row_stack(results)
        #save_results(results_matrix,'mesh_dimension,injection_load,throughput,delay')
        self.save_results(results_matrix,'mesh_dimension,injection_load,total_received_packets, total_received_flits, received_flits_ratio, average_wireless_utilization, \
global_average_delay, max_delay, network_throughput, average_IP_throughput, total_energy, dynamic_energy, static_energy')

        return results


'''




'''

if __name__=='__main__':
    pn=Pynoxim('~/noxim/noxim/bin')
    # Testing running noxim for injection load 0.1 to 0.3 steps 0.05 for a mesh of 4x4 and 6x6
    # Save the results as csv file.
    a=pn.compare_config_injection_load(np.arange(0.1,0.3,0.05),[4,6])



''' Plotting using Matplotlib

    #figures for throughput and delay
    f1=plt.figure(1)
    ax1=f1.add_subplot(111)
    f2=plt.figure(2)
    ax2=f2.add_subplot(111)

    # plotting
    ax1.plot(injectionL,tp,'r'+annotation_marker[core_it-2],injectionL,tp,'k')
    ax2.plot(injectionL,delay,'r'+annotation_marker[core_it-2],injectionL,delay,'k')
    #plt.draw()

    ax1.set_ylim(0, 1)
    ax1.set_ylabel('average_IP_throughput (flit/cycle/IP)')
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



import matplotlib.pyplot as plt
f1=plt.figure(1)
ax1=f1.add_subplot(111)
p1=ax1.plot([1,2,3])
f1.show()
'''
