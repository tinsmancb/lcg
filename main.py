class lcg:
    def __init__(self, seed, a=1, c=0, m=2**64-1):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.current_val = seed
        self.counter = 0

    def roll(self):
        self.current_val = (self.a*self.current_val + self.c) % self.m
        self.counter += 1
        return self.current_val

    def roll_norm(self):
        return self.roll()/self.m

    def roll_byte(self):
        return self.roll() % 0x100

def lcg_cypher(text: bytearray, key: int) -> bytearray:
    out = bytearray()

    #TODO: Initialize an LCG, using key as the seed

    for i, j in zip(text, cycle(key)):
        #TODO: Instead of cylcing through key,
        #TODO: Draw bytes from the LCG and use those
        #TODO: to encypt your message.
        out.append(i ^ j)

    return out
    #TODO: Check that you can encrypt and decrypt messages
    #TODO: succesfully.

def main():
    prng = lcg(344, a=77, c=76, m=2**16+1)
    for _ in range(10):
        print(hex(prng.roll_byte()))


if __name__ == '__main__':
    main()
