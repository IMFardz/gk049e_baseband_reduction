cd /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction

export OMP_NUM_THREADS=32           # Number of cores in mussel. If using lobster, use 16 instead

source ~/.bashrc

python jb_fold.py gk049e_jb_no0005.vdif > /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction/logs/jb/no0005.log

python jb_fold.py gk049e_jb_no0001.vdif > /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction/logs/jb/no0001.log

python jb_fold.py gk049e_jb_no0004.vdif > /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction/logs/jb/no0004.log

python jb_fold.py gk049e_jb_no0023.vdif > /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction/logs/jb/no0005.log

python jb_fold.py gk049e_jb_no0026.vdif > /mnt/scratch-lustre/fsyed/B1133+16/Analysis2020/gk049e/gk049e_baseband_reduction/logs/jb/no0005.log




