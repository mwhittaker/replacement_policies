import policy

class MRU(policy.ReplacementPolicy):
    def __init__(self, B):
        policy.ReplacementPolicy.__init__(self, B)
        self.mru = None

    def access(self, page):
        # The page is already in the buffer.
        if page in self.buffer:
            self.mru = page
            return

        # There is an empty spot in the buffer.
        if None in self.buffer:
            self.buffer[self.buffer.index(None)] = page
            self.mru = page
            return

        # We evict from the buffer.
        assert(self.mru is not None)
        self.buffer[self.buffer.index(self.mru)] = page
        self.mru = page

if __name__ == "__main__":
    m = MRU(4)
    for p in "SEEMAWESOMEPOSSUM":
        b = list(m.get_buffer())
        m.access(p)
        print(p, p in b, m.get_buffer())
