#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --time=24:00:00
#SBATCH --job-name=ar_baseband_tasks
#SBATCH --mail-type=ALL

cd /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction

export OMP_NUM_THREADS=32           # Number of cores in mussel. If using lobster, use 16 instead

source ~/.bashrc

python ar_fold.py gk049e_ar_no0005.m5b > /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction/logs/ar/no0005.log

#python ar_fold.py gk049e_ar_no0004.m5b > /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction/logs/ar/no0004.log

#python ar_fold.py gk049e_ar_no0023.m5b > /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction/logs/ar/no0023.log

python ar_fold.py gk049e_ar_no0026.m5b > /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction/logs/ar/no0026.log
