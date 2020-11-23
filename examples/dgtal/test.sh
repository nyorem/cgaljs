em++ simple.cpp \
    ../../libs/libgmp.a \
    ../../libs/libDGtal.a \
    -U__SSE2_MATH__ \
    -I ../../includes \
    -I ../../includes/gmp \
    -I ../../includes/cgal \
    -I ../../includes/dgtal \
    -o test.js

node test.js
