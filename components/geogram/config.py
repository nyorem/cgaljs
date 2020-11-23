NAME = 'geogram'
VERSION = '1.7.4'
DOWNLOADS = ['https://github.com/alicevision/geogram/archive/v%s.tar.gz' % VERSION]
SOURCE_DIR = 'geogram-%s' % VERSION
SOURCE_PATCHES = [
    {'file': 'cmake/platforms/Emscripten-clang/config.cmake', 'patch': 'config.cmake.patch'},
    {'file': 'src/lib/geogram/basic/process_unix.cpp', 'patch': 'process_unix.cpp.patch'},
]
CONFIGURE_CMD = ' '.join([
    'sh -f configure.sh Emscripten-clang',
])
MAKE_CMD = 'cd build/Emscripten-clang-Release && make -j4'
ARTIFACTS =  {
    'includes': [
        { 'source':'geogram-%s/src/lib' % VERSION, 'name': 'geogram' },
    ],
    'libs': [
        {
            'source': 'geogram-%s/build//Emscripten-clang-Release/lib/libgeogram.a' % VERSION,
            'name':'libgeogram.a',
        },
        {
            'source': 'geogram-%s/build//Emscripten-clang-Release/lib/libgeogram_gfx.a' % VERSION,
            'name':'libgeogram_gfx.a',
        },
        {
            'source': 'geogram-%s/build//Emscripten-clang-Release/lib/libgeogram_num_3rdparty.a' % VERSION,
            'name':'libgeogram_num_3rdparty.a',
        },
        {
            'source': 'geogram-%s/build//Emscripten-clang-Release/lib/libexploragram.a' % VERSION,
            'name':'libexploragram.a',
        },
     ]
}
