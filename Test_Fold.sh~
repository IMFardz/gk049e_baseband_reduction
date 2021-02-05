#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --time=4:00:00
#SBATCH --job-name=dspsr_test
#SBATCH --mail-type=ALL  

cd /scratch/p/pen/syedfard/B1133/gk049e/gk049e_baseband_reduction

export OMP_NUM_THREADS=1

source ~/.bashrc

python ar_fold.py
