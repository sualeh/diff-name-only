import hashlib
import os
from datetime import datetime


class FileInfo:

    def __init__(self, root, filename):
        self.file_path = os.path.join(os.path.abspath(root), filename)
        self.file_md5 = self.md5(self.file_path)
        self.file_mtime = os.path.getmtime(self.file_path)

    def md5(self, filename):
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def mtime(self):
        return datetime.fromtimestamp(self.file_mtime).strftime("%a, %d %b %Y %H:%M:%S")
