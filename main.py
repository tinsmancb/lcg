import matplotlib.pyplot as plt

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


def main():
    prng = lcg(344, a=16598013, c=12820163, m=2**24)
    sample = [prng.roll_norm() for _ in range(1_000_000)]
    plt.hist(sample, bins=30)
    plt.show()


if __name__ == '__main__':
    main()
