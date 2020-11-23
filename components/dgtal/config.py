NAME = 'dgtal'
VERSION = '1.1'
DOWNLOADS = ['https://github.com/DGtal-team/DGtal/archive/%s.tar.gz' % VERSION]
SOURCE_DIR = 'DGtal-%s' % VERSION
SOURCE_PATCHES = [
    {'file': 'cmake/CheckDGtalOptionalDependencies.cmake', 'patch': 'CheckDGtalOptionalDependencies.cmake.patch'},
]
CONFIGURE_CMD = ' '.join([
    'mkdir build &&',
    'cd build &&',
    'emcmake cmake ..',
    '-DZLIB_INCLUDE_DIR={includes}/zlib',
    '-DZLIB_LIBRARY_RELEASE={libs}/libz.a',
    '-DZLIB_LIBRARY_DEBUG={libs}/libz.a',
    '-DWITH_GMP=true',
    '-DGMP_INCLUDE_DIR:STRING={includes}/gmp',
    '-DGMP_LIBRARIES:STRING={libs}/libgmp.a',
    '-DGMPXX_LIBRARIES:STRING={libs}/libgmp.a',
    # '-DMPFR_INCLUDE_DIR:STRING={includes}/mpfr',
    # '-DMPFR_LIBRARIES:STRING={libs}/libmpfr.a',
    '-DWITH_EIGEN=true',
    '-DEIGEN3_INCLUDE_DIR={includes}/eigen3',
    '-DWITH_CGAL=true',
    '-DBoost_INCLUDE_DIR:STRING={includes}',
    '-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON',
    '-DCMAKE_BUILD_TYPE=Release',
    '-DBUILD_EXAMPLES=false',
    # '-DCMAKE_CXX_FLAGS="-v -U__SSE2_MATH__ --ignore-dynamic-linking -DCGAL_HAS_NO_THREADS -U__GNUG__ -DCGAL_NO_ASSERTIONS -DCGAL_FORWARD -DBOOST_MATH_DISABLE_STD_FPCLASSIFY -DBOOST_NO_NATIVE_LONG_DOUBLE_FP_CLASSIFY -DBOOST_MATH_NO_LONG_DOUBLE_MATH_FUNCTIONS"'
])
MAKE_CMD = 'cd build && emmake make -j4'
ARTIFACTS =  {
    'includes': [
        { 'source':'DGtal-%s/src/' % VERSION, 'name': 'dgtal' },
        { 'source':'DGtal-%s/build/src/DGtal/base/Config.h' % VERSION,
          'name': 'dgtal/DGtal/base/Config.h',
          'is_file': True,
        },
        { 'source':'DGtal-%s/build/src/DGtal/topology/tables/NeighborhoodTables.h' % VERSION,
          'name': 'dgtal/DGtal/topology/tables/NeighborhoodTables.h',
          'is_file': True,
        },
    ],
    'libs': [{
        'source': 'DGtal-%s/build/src/libDGtal.a' % VERSION,
        'name':'libDGtal.a'
    }]
}
