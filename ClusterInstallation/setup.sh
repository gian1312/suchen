#/bin/bash
module load python_gpu/3.6.1
module unload cudnn cuda
module load cuda/9.0.176 cudnn/7.0
# find /cluster/apps/gcc-4.8.5/cuda-8* -type f -name "libcuda.so.*"
# ln -f -s /cluster/apps/gcc-4.8.5/cuda-8.0.61-mxdqob5lveng3f2utljrysrx4vjp7g3m/doc/man/man7/libcuda.so.7 libcuda.so.1
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/cluster/home/joosb/bin/
