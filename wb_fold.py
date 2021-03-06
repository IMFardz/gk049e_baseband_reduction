"""
Script for reducing WB data
"""
import astropy.units as u
from baseband import vdif
from astropy.time import Time, TimeDelta
import numpy as np
import sys
import folding_pipeline as sr
from baseband_tasks.shaping import Reshape
from baseband_tasks.io import hdf5
import traceback
import time

# OS Things
fdir = '/mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/baseband_data/wb/'
fname = sys.argv[1]
output_name = '/mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/numpy_arrays/wb/' + fname[:-5]
print("Output File Name: {}".format(output_name))

# Load Data
frequency = np.array([[332.00], [332.00]]) * u.MHz

# NOTE: Sideband should be [[-1,-1], [1,1]] according to .vex file. Data did not turn our great however so I am looking into it.
sideband = np.array([[1, 1], [-1, -1]])

polarization = ['R', 'L']   # Right circular polarization & left circular polarization
dispersion_measure = 4.84066 * u.pc / u.cm**3
polyco_file = '/mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/polycos/wb/polyco_new.dat'
fullpol = False
print("Parameters set")

# Creating stream reader. For other formats, such as vdif, use vdif.open(...)
fh = vdif.open(fdir + fname, 'rs')
rh = Reshape(fh, (2, 2))
dt = TimeDelta(10, format='sec')

# Rounding Time
start = Time(rh.time)
start_time_str = start.iso.__str__()
new_time = Time(start_time_str, precision = -1)
new_time_str = new_time.iso.__str__()
start_time = Time(new_time_str) + dt
print("Opened stream reader with sample shape:", rh.sample_shape)
print("Starting at time:", start_time)

# Initial waterfall interpretor
WF = sr.Fold(rh, dispersion_measure, frequency, sideband, polyco_file, polarization, fullpol,start=start_time, nthreads=1)
print("Initialized waterfall interpretor with shape:", WF.integrator.shape)

# EXPERIMENTAL: Create stream writer.
h5w = hdf5.open("/mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/hdf5_files/wb/" + fname[:-5] + ".hdf5", 'w', template=WF.integrator)
print("Output File name: " + "/mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/hdf5_files/wb/" + fname[:-5] + ".hdf5")

# Determine how many samples to output at a time. I reccomend 1.
nsamples = WF.integrator.shape[0]
nsamples_per_output = 1
times = []

# Start the timer
print("Starting timer")
runtime_start = time.time()

# Loop through integrator, creating one time bin at a time
try:

    while WF.integrator.tell() < nsamples - nsamples_per_output:
        # OUTPUT to hdf5 file
        current_time = WF.integrate_and_save(count=nsamples_per_output, output=h5w)
        print("Run-time so far: ", time.time() - runtime_start)
        print()

    # Get the run-time
    runtime_end = time.time()
    runtime = runtime_end - runtime_start
    print("Run-Time For Program : {}".format(runtime))

    # Save File
    h5w.close()

except:
    print("Something went wrong. Likely, you inputted noise or too small of a sample set")
    print(traceback.format_exc())
    print(sys.exc_info()[0])

    # Get the run-time
    runtime_end = time.time()
    runtime = runtime_end - runtime_start
    print("Run-Time For Program : {}".format(runtime))

    # Same File
    h5w.close()
