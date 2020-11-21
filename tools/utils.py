import os
import tarfile
import lzma
import urllib.request

def download(url, path):
    filename = url.split('/')[-1]
    file_path = os.path.join(path, filename)
    print('Downloading:%s to:%s' % tuple([url, file_path]))

    if os.path.isfile(file_path):
        print('Already downloaded')
        return file_path

    if not os.path.exists(path):
        os.makedirs(path)

    u = urllib.request.urlopen(url)
    localFile = open(file_path, 'wb')
    localFile.write(u.read())
    localFile.close()
    print('Download completed')
    return file_path

def untar(tar_filename, dest_path):
    # Check it actually needs to be unarchived
    if not is_archive_file(tar_filename):
        return

    if os.path.exists(dest_path):
        print("Already unarchived. Clean if you want to get a fresh copy")
        return

    print("Unarchiving")

    tar_file = None
    if is_lzma_archive(tar_filename):
        f = lzma.LZMAFile(tar_filename)
        tar_file = tarfile.open(fileobj=f)
    else:
        tar_file = tarfile.open(tar_filename)

    tar_file.extractall(dest_path)
    print("Finished unarchiving")

def is_archive_file(archive_path):
    return archive_path.split('.')[-1] in [ 'bz2', 'xz' ]

def is_lzma_archive(archive_path):
    return archive_path.split('.')[-1] == 'xz'
