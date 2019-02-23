import os

from diff_file_name_only_files import DiffFileWriter
from file_info import FileInfo


def list_files(walk_dir):
    with DiffFileWriter(walk_dir, 'diff-name-only-list.md') as list_file:
        list_file.write_header()
        list_file.write_root()
        for root, subdirs, files in os.walk(walk_dir):
            list_file.write_newline()
            list_file.write_directory(root, 0)
            for filename in files:
                list_file.write_file(FileInfo(root, filename), 1)


def main():
    walk_dir = ".."  # sys.argv[1]
    list_files(walk_dir)


main()
