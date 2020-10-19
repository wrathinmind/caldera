import os


class Packer:
    def __init__(self):
        self.name = 'upx'

    def pack_payload(self, file, contents):
        return file, contents
