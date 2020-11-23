NAME = 'zlib'
VERSION = '1.2.8'
DOWNLOADS = ['https://github.com/emscripten-ports/zlib/archive/v%s.tar.gz' % VERSION]
SOURCE_DIR = 'zlib-%s' % VERSION
CONFIGURE_CMD = ' '.join([
    'mkdir build &&',
    'cd build &&',
    'emcmake cmake ..',
])
MAKE_CMD = 'cd build && emmake make -j4'
ARTIFACTS =  {
    'includes': [{
        'source':'zlib-%s' % VERSION,
        'name': 'zlib'
    }],
    'libs': [{
        'source': 'zlib-%s/build/libz.a' % VERSION,
        'name':'libz.a'
    }]
}
