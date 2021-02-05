#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --time=24:00:00
#SBATCH --job-name=ar_baseband_tasks
#SBATCH --mail-type=ALL

cd /scratch/p/pen/syedfard/B1133/gk049e/gk049e_baseband_reduction

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

source ~/.bashrc

python ar_fold.py gk049e_ar_no0004.m5b > /scratch/p/pen/syedfard/B1133/gk049e/gk049e_baseband_reduction/logs/ar/no0004.log

python ar_fold.py gk049e_ar_no0005.m5b > /scratch/p/pen/syedfard/B1133/gk049e/gk049e_baseband_reduction/logs/ar/no0005.log

python ar_fold.py gk049e_ar_no0023.m5b > /scratch/p/pen/syedfard/B1133/gk049e/gk049e_baseband_reduction/logs/ar/no0023.log

python ar_fold.py gk049e_ar_no0026.m5b > /scratch/p/pen/syedfard/B1133/gk049e/gk049e_baseband_reduction/logs/ar/no0026.log
