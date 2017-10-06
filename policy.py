class ReplacementPolicy(object):
    def __init__(self, B):
        self.B = B
        self.buffer = [None] * B

    def access(self, page):
        raise NotImplementedError("")

    def get_buffer(self):
        return self.buffer
