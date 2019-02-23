import os
import time
from datetime import datetime

from file_info import FileInfo


def list_files(walk_dir):
    diff_name_only_list_path = os.path.join(walk_dir, 'diff-name-only-list.md')
    with open(diff_name_only_list_path, 'wb') as list_file:
        list_file.write(('# MD5 Checksums For Directory\n').encode('utf-8'))
        list_file.write(
            ('%s\n\n' % datetime.fromtimestamp(time.time()).strftime("%a, %d %b %Y %H:%M:%S")).encode(
                'utf-8'))
        list_file.write(('`%s`\n' % os.path.abspath(walk_dir)).encode('utf-8'))
        for root, subdirs, files in os.walk(walk_dir):
            list_file.write(
                ('\n- `%s`\n' % os.path.relpath(os.path.abspath(root), os.path.abspath(walk_dir))).encode('utf-8'))
            for filename in files:
                file_info = FileInfo(root, filename)
                list_file.write(
                    ('  - `%s`  \n' % filename).encode('utf-8'))
                list_file.write(
                    ('    %s  \n' % file_info.mtime()).encode(
                        'utf-8'))
                list_file.write(
                    ('    %s  \n' % file_info.file_md5).encode('utf-8'))


def main():
    walk_dir = ".."  # sys.argv[1]
    list_files(walk_dir)


main()
