NAME = 'gmp'
VERSION = '6.2.0'
DOWNLOADS = ['ftp://ftp.gmplib.org/pub/gmp/gmp-%s.tar.bz2' % VERSION]
SOURCE_DIR = 'gmp-%s' % VERSION
CONFIGURE_CMD = 'emconfigure ./configure --disable-assembly --host none --enable-cxx'
MAKE_CMD = 'emmake make -j4'
CONFIG_PATCHES = [
    {
        'file': 'config.h',
        'patch': 'config.h.patch'
    }
]
ARTIFACTS =  {
    'includes': [{
                     'source':'gmp-%s' % VERSION,
                     'name':'gmp'
                 }],
    'libs': [{
                     'source': 'gmp-%s/.libs/libgmp.a' % VERSION,
                     'name':'libgmp.a'
                 }]
}

