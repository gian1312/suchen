ssh -Y nethz@login.leonhard.ethz.ch
module avail #available modules
module list #lists all active module
module load python_gpu/3.6.1 #Python 3.6.1, TensorFlow 1.3, CUDA 8.0.61, cuDNN 6.0
pip3 install --user tensorforce[tf_gpu] #Max Version to use TensorFlow >= 1.3
pip3 install --user scikit-image
pip3 install --user tqdm
#Load bunch of modules
  1) StdEnv            11) libjpeg-turbo/1.5.0   21) pcre/8.40
  2) gcc/4.8.5         12) jpeg/9b               22) pixman/0.34.0
  3) cuda/9.0.176       13) glib/2.49.7           23) libxcb/1.12
  4) cudnn/6.0         14) gdk-pixbuf/2.31.2     24) libxau/1.0.8
  5) python_gpu/3.6.1  15) libxml2/2.9.4         25) cairo/1.14.10
  6) boost/1.63.0      16) libpthread-stubs/0.3  26) atk/2.20.0
  7) pango/1.40.4      17) libxdmcp/1.1.2        27) fontconfig/2.11.1
  8) freetype/2.7      18) zlib/1.2.11           28) xcb-proto/1.12
  9) xcb-util/0.4.0    19) openblas/0.2.19       29) xauth/1.0.9
 10) xproto/7.0.29     20) libpng/1.6.27         30) gtkplus/2.24.31

module load boost pango freetype xcb-util xproto libjpeg-turbo glib gdk-pixbuf libxml2 libpthread-stubs libxdmcp zlib openblas libpng pcre libxcb libxau cairo atk fontconfig xcb-proto xauth gtkplus

# Attention towards cuda:
module unload cuda
module load cuda/9.0.176
# Download an Compile SDL2
Install to ~/bin/

#Use patched Vizdoom Version 1.1.4 or patch yourself as instructed below
pip3 install --user .

# Install VizDoom 1.1.4
wget https://github.com/mwydmuch/ViZDoom/archive/1.1.4.zip
unzip 1.1.4.zip
# Changes to setup.py
            cmake_arg_list.append("-DSDL2_LIBRARY=/cluster/home/joosb/bin/sdl2/lib/libSDL2.so") #-DSDL2_LIBRARY=$HOME/bin/sdl2/lib/libSDL2.so
            cmake_arg_list.append("-DSDL2_INCLUDE_DIR=/cluster/home/joosb/bin/sdl2/include")
            cmake_arg_list.append("-DCMAKE_CXX_STANDARD_LIBRARIES=-pthread")
# any SDL related errors -> add SDL/ before header file
# if any other errors persist -> module unload cmake && module load cmake/3.8.X Version



bsub -n 1 -W 4:00 -R "rusage[mem=16384, ngpus_excl_p=2]" python3 learning_tensorflow.py
bjobs
grep -A3 "Creating TensorFlow device" lsf.o194796


ldconfig -p | grep gtk

echo '#include <float.h>' | cpp


/usr/lib64/gtk-2.0/
Problem: Header files fehlen

Currently Loaded Modules:
  1) StdEnv            5) cudnn/6.0          9) boost/1.63.0  13) pango/1.40.4       17) freetype/2.7    21) xcb-util/0.4.0        25) xproto/7.0.29    29) libjpeg-turbo/1.5.0
  2) gcc/4.8.5         6) jpeg/9b           10) glib/2.49.7   14) gdk-pixbuf/2.31.2  18) libxml2/2.9.4   22) libpthread-stubs/0.3  26) libxdmcp/1.1.2   30) zlib/1.2.11
  3) openblas/0.2.19   7) libpng/1.6.27     11) pcre/8.40     15) pixman/0.34.0      19) libxcb/1.12     23) libxau/1.0.8          27) cairo/1.14.10
  4) cuda/8.0.61       8) python_gpu/3.6.1  12) atk/2.20.0    16) fontconfig/2.11.1  20) xcb-proto/1.12  24) xauth/1.0.9           28) gtkplus/2.24.31


  1) StdEnv            11) libjpeg-turbo/1.5.0   21) pcre/8.40
  2) gcc/4.8.5         12) jpeg/9b               22) pixman/0.34.0
  3) cuda/8.0.61       13) glib/2.49.7           23) libxcb/1.12
  4) cudnn/6.0         14) gdk-pixbuf/2.31.2     24) libxau/1.0.8
  5) python_gpu/3.6.1  15) libxml2/2.9.4         25) cairo/1.14.10
  6) boost/1.63.0      16) libpthread-stubs/0.3  26) atk/2.20.0
  7) pango/1.40.4      17) libxdmcp/1.1.2        27) fontconfig/2.11.1
  8) freetype/2.7      18) zlib/1.2.11           28) xcb-proto/1.12
  9) xcb-util/0.4.0    19) openblas/0.2.19       29) xauth/1.0.9
 10) xproto/7.0.29     20) libpng/1.6.27         30) gtkplus/2.24.31

readelf -s /usr/lib64/libpthread.so.0 | grep pthread_create
   204: 00000000000080a0  2569 FUNC    GLOBAL DEFAULT   13 pthread_create@@GLIBC_2.2.5
    78: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS pthread_create.c
   368: 00000000000080a0  2569 FUNC    LOCAL  DEFAULT   13 __pthread_create_2_1
   645: 00000000000080a0  2569 FUNC    GLOBAL DEFAULT   13 pthread_create@@GLIBC_2.2


