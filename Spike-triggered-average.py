"""
Created on Wed Apr 22 15:21:11 2015

Code to compute spike-triggered average.
"""

from __future__ import division
import numpy as np
import pandas as pd
import pickle

# I put this here because it make the most sense. This is the data I will be dealing with
filename = "/Users/ivicino/Documents/PythonScripts/Computational Neuroscience - Coursera/Week 2/Week1quiz-Coursera/c1p8.pickle"

infile = open(filename,'rb')
spike_info = pickle.load(infile)
infile.close()

df = pd.DataFrame(data=spike_info)
dfnump = pd.DataFrame(data=spike_info).to_numpy()
# dfnump is the numpy dataframe

stim = dfnump[:,0]
rho = dfnump[:,1]

def compute_sta(stim, rho, num_timesteps):
    """Compute the "spike-triggered average" from a stimulus and spike-train.
    
    Args:
        stim: stimulus time-series
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA
        
    Returns:
        spike-triggered average for num_timesteps timesteps before spike"""
    
    sta = np.zeros((num_timesteps,)) #This is a vector with the length of num_timesteps

    # This command finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0]  + num_timesteps

    # Fill in this value. Note that you should not count spikes that occur
    # before 300 ms into the recording.
    
    ''' 
    want to start looking for rho=1 after 300ms, and each stimulus value is 
    taken every 2 seconds, so 300 ms = 150 values of stimulus data.
    
    '''
    
    # Data = df.iloc[150:600000,:]
    
    # Spikez = Data['rho'].isin([1]) 
    # # see file "stimulusData-SneakPeak" to see what this code does. 
     
    
    num_spikes = len(spike_times)

    
    
    # Compute the spike-triggered average of the spikes found.
    
    # To do this, **compute the average of all of the vectors
    # starting 300 ms (exclusive) before a spike and ending at the time of
    # the event (inclusive). Each of these vectors defines a list of
    # samples that is contained within a window of 300 ms before each
    # spike. The average of these vectors should be completed in an
    # element-wise manner.
    
    # Your code goes here.
    
    # What I have:
    # spike_times, tells me where the spikes occur
    # num_spikes, tells me the number of spikes
    
    
    
    # Lst.append(np.average(stim[spike_times] - 150)) <--totally wrong
    # print('calculating...')
    # # sta = np.where(sta==0, AvgSpike, sta)
    # # print('writing to sta')
    
    Lst =([])
    Lst2 =([])
    
    for i in range(150):
        X = stim[spike_times - i]
        # print(X)
        Lst.append(X)
    for i in Lst:
        # print(i)
        Lst2.append(np.average(i))
  
    sta = np.where(sta==0, Lst2, sta)
        
    # print('Number of spikes:')
    # print(num_spikes)
    
    
    
    return sta


# print('\n')
# print(compute_sta(stim, rho, 150))
# print(num_spikes)
