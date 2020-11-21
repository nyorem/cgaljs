emcc test.c ../../libs/libmpfr.a ../../libs/libgmp.a -I ../../includes/gmp -I ../../includes/mpfr -o test.js
node test.js
