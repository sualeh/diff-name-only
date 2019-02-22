import hashlib
import os


def list_files(walk_dir):
    print('walk_dir = ' + os.path.abspath(walk_dir))

    list_file_path = os.path.join(walk_dir, 'diff-name-only-list.txt')
    with open(list_file_path, 'wb') as list_file:
        for root, subdirs, files in os.walk(walk_dir):
            list_file.write(('--\nroot = ' + root).encode('utf-8'))

            for subdir in subdirs:
                list_file.write(('\n\t- subdirectory %s' % subdir).encode('utf-8'))

            for filename in files:
                file_path = os.path.join(root, filename)
                file_md5 = md5(file_path)
                list_file.write(
                    ('\n\t- file %s MD5 %s (full path: %s)' % (filename, file_md5, file_path)).encode('utf-8'))


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def main():
    walk_dir = ".."  # sys.argv[1]
    list_files(walk_dir)


main()
