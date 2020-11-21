em++ simple_triangulation_3.cpp \
    ../../libs/libgmp.a \
    ../../libs/libmpfr.a \
    -U__SSE2_MATH__ \
    -I ../../includes \
    -I ../../includes/gmp \
    -I ../../includes/mpfr \
    -I ../../includes/cgal \
    -o test.js

node test.js
