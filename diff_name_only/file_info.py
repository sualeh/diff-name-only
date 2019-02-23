import hashlib
import os
from datetime import datetime


class FileInfo:

    def __init__(self, root: str, filename: str):
        assert root is not None
        self.root = root
        assert filename is not None
        self.filename = filename
        file_path = os.path.join(os.path.abspath(root), filename)
        self.file_md5 = self.md5(file_path)
        self.file_mtime = os.path.getmtime(file_path)

    def md5(self, file_path: str):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @property
    def mtime(self):
        assert self is not None
        assert isinstance(self, FileInfo)
        return datetime.fromtimestamp(self.file_mtime).strftime("%a, %d %b %Y %H:%M:%S")

    @property
    def checksum(self):
        assert self is not None
        assert isinstance(self, FileInfo)
        return self.file_md5
