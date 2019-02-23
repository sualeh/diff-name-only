import os
import time
from datetime import datetime

from file_info import FileInfo


class DiffFileWriter:

    def __init__(self, root: str, filename: str):
        self.root = root
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(os.path.join(os.path.abspath(self.root), self.filename), "wt")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file is not None:
            self.file.close()

    def write_header(self):
        self.file.write('# MD5 Checksums For Directory\n')
        self.file.write('%s\n\n' % datetime.fromtimestamp(time.time()).strftime("%a, %d %b %Y %H:%M:%S"))

    def write_root(self):
        self.file.write('`%s`\n\n' % os.path.abspath(self.root))

    def write_directory(self, directory: str, indent: int):
        self.write_indent(indent)
        self.file.write('- `%s`\n' % os.path.relpath(directory, self.root))

    def write_file(self, file_info: FileInfo, indent: int):
        self.write_indent(indent)
        self.file.write('- `%s`  \n' % file_info.filename)

        self.write_indent(indent)
        self.file.write('  %s  \n' % file_info.mtime)

        self.write_indent(indent)
        self.file.write('  %s  \n' % file_info.checksum)

    def write_indent(self, indent: int):
        if indent > 0:
            self.file.write("  " * indent)

    def write_newline(self):
        self.file.write('\n')
