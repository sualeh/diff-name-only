import hashlib
import os


def list_files(walk_dir):
    diff_name_only_list_path = os.path.join(walk_dir, 'diff-name-only-list.md')
    with open(diff_name_only_list_path, 'wb') as list_file:
        list_file.write(('# MD5 Checksums For Directory\n').encode('utf-8'))
        list_file.write(('%s\n' % os.path.abspath(walk_dir)).encode('utf-8'))
        for root, subdirs, files in os.walk(walk_dir):
            list_file.write(
                ('\n- `%s`\n' % os.path.relpath(os.path.abspath(root), os.path.abspath(walk_dir))).encode('utf-8'))
            for filename in files:
                file_path = os.path.join(os.path.abspath(root), filename)
                file_md5 = md5(file_path)
                list_file.write(
                    ('  - `%s`  \n' % filename).encode('utf-8'))
                list_file.write(
                    ('    %s\n' % file_md5).encode('utf-8'))


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
