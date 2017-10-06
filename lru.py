import policy

class LRU(policy.ReplacementPolicy):
    def __init__(self, B):
        policy.ReplacementPolicy.__init__(self, B)
        self.used = []

    def use(self, page):
        if page in self.used:
            self.used.remove(page)
        self.used.append(page)

    def access(self, page):
        # The page is already in the buffer.
        if page in self.buffer:
            self.use(page)
            return

        # There is an empty spot in the buffer.
        if None in self.buffer:
            self.buffer[self.buffer.index(None)] = page
            self.use(page)
            return

        # We evict from the buffer.
        assert(len(self.used) > 0)
        to_replace = self.used.pop(0)
        self.buffer[self.buffer.index(to_replace)] = page
        self.use(page)

if __name__ == "__main__":
    m = LRU(4)
    for p in "SEEMAWESOMEPOSSUM":
        b = list(m.get_buffer())
        m.access(p)
        print(p, p in b, m.get_buffer())
