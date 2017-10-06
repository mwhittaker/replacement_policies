import policy

class Clock(policy.ReplacementPolicy):
    def __init__(self, B):
        policy.ReplacementPolicy.__init__(self, B)
        self.bits = [0] * self.B
        self.hand = 0

    def use(self, page):
        if page in self.used:
            self.used.remove(page)
        self.used.append(page)

    def access(self, page):
        # The page is already in the buffer.
        if page in self.buffer:
            self.bits[self.buffer.index(page)] = 1
            return

        # There is an empty spot in the buffer.
        if None in self.buffer:
            idx = self.buffer.index(None)
            self.buffer[idx] = page
            self.bits[idx] = 1
            self.hand = (idx + 1) % self.B
            return

        # We evict from the buffer.
        while (self.bits[self.hand] == 1):
            self.bits[self.hand] = 0
            self.hand = (self.hand + 1) % self.B
        self.buffer[self.hand] = page
        self.bits[self.hand] = 1
        self.hand = (self.hand + 1) % self.B

if __name__ == "__main__":
    m = Clock(4)
    for p in "SEEMAWESOME":
        b = list(m.get_buffer())
        m.access(p)
        print(p, p in b, m.get_buffer(), m.bits, m.hand)
