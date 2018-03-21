ssh -Y nethz@login.leonhard.ethz.ch
module avail #available modules
module list #lists all active module
module load python_gpu/3.6.1 #Python 3.6.1, TensorFlow 1.3, CUDA 8.0.61, cuDNN 6.0
pip3 install --user tensorforce[tf_gpu]==0.3.4 #Max Version to use TensorFlow >= 1.3
# Download an Compile SDL2
pip3 install --user vizdoom==1.1.4

export CMAKE_PREFIX_PATH=/cluster/home/joosb/bin/


export SDL2_PATH=/cluster/home/joosb/bin/sdl2/


export SDL2_LIBRARY=/cluster/home/joosb/bin/sdl2/lib/
export SDL2_INCLUDE_DIR=/cluster/home/joosb/bin/sdl2/include/SDL2/


export SDL2_INCLUDE_DIR=/cluster/home/joosb/bin/sdl2/include/SDL2
export SDL2_LIBRARY=/cluster/home/joosb/bin/sdl2/lib/libSDL2.so

ldconfig -p | grep gtk

echo '#include <float.h>' | cpp


/usr/lib64/gtk-2.0/
Problem: Header files fehlen

Currently Loaded Modules:
  1) StdEnv            5) cudnn/6.0          9) boost/1.63.0  13) pango/1.40.4       17) freetype/2.7    21) xcb-util/0.4.0        25) xproto/7.0.29    29) libjpeg-turbo/1.5.0
  2) gcc/4.8.5         6) jpeg/9b           10) glib/2.49.7   14) gdk-pixbuf/2.31.2  18) libxml2/2.9.4   22) libpthread-stubs/0.3  26) libxdmcp/1.1.2   30) zlib/1.2.11
  3) openblas/0.2.19   7) libpng/1.6.27     11) pcre/8.40     15) pixman/0.34.0      19) libxcb/1.12     23) libxau/1.0.8          27) cairo/1.14.10
  4) cuda/8.0.61       8) python_gpu/3.6.1  12) atk/2.20.0    16) fontconfig/2.11.1  20) xcb-proto/1.12  24) xauth/1.0.9           28) gtkplus/2.24.31

