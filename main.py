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


def main():
    prng = lcg(3453252345, 723325234)
    for _ in range(10):
        print(prng.roll())


if __name__ == '__main__':
    main()
