def norm1(n):
    """Normalize 1 -> 1 , 0 -> -1"""
    return 2 * int(n) - 1

def norm2(n):
    """Normalize +ve -> 1, -ve -> 0"""
    assert n != 0
    return ((n // abs(n)) + 1) // 2

class Node:
    def __init__(self):
        self.count = 0
        self.zeros = None
        self.ones = None

    def store(self, l, number):
        self.count += 1
        if l:
            left_bit = l.pop(0)
            if not self.zeros:
                # Always initialize both children
                assert not self.ones
                self.zeros = Node()
                self.ones = Node()
            if left_bit == '0':
                self.zeros.store(l, number)
            else:
                assert self.ones is not None
                self.ones.store(l, number)

    """02 rating => mode == True, co2 rating => mode == False"""
    def rating(self, mode):
        node = self
        number = 0
        while node.zeros:
            number *= 2
            assert node.ones
            assert node.zeros.count or node.ones.count
            if not node.zeros.count or (node.ones.count and (node.zeros.count <= node.ones.count) == mode):
                number += 1
                node = node.ones
            else:
                node = node.zeros
        return number

def part1(ll: list[str]) -> str:
    normed_lines = list([map(norm1, l) for l in ll])
    line_len = len(ll[0])
    columns = list(sum(l) for l in zip(*normed_lines))
    gamma_list = list(map(norm2, columns))

    gamma = 0
    for i, d in enumerate(reversed(gamma_list)):
        gamma += d * 2**i

    epsilon = 2 ** line_len - 1 - gamma

    return gamma * epsilon

def part2(ll: list[str]) -> str:
    root = Node()
    for l in ll:
        number = int(''.join(list(l)), 2)
        root.store(list(l), number)

    o2 = root.rating(True)
    co2 = root.rating(False)
    
    return str(o2 * co2)
