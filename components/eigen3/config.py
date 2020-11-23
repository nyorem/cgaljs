NAME = 'eigen3'
VERSION = '3.3.7'
DOWNLOADS = ['https://github.com/eigenteam/eigen-git-mirror/archive/%s.tar.gz' % VERSION ]
SOURCE_DIR = 'eigen-%s' % VERSION
ARTIFACTS =  {
        'includes': [{
            'source':'eigen-git-mirror-%s' % VERSION,
            'name':'eigen3'
        }]
    }


