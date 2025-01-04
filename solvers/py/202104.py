class Board:
    def __init__(self, numbers, index):
        """Takes a list of lists of numbers"""
        self.rows = []
        for row in numbers:
            self.rows.append([int(n) for n in row.split(" ") if n])
        self.columns = [list(c) for c in zip(*self.rows)]
        self.index = index  # debug

    def draw(self, number):
        for row in self.rows:
            if number in row:
                row.remove(number)
                if not row:
                    remaining = sum([sum(row) for row in self.rows])
                    return number * remaining

        for column in self.columns:
            if number in column:
                column.remove(number)
                if not column:
                    remaining = sum([sum(column) for column in self.columns])
                    return number * remaining

        return False

def parse_input(ll: list[str]) -> tuple[list[int], list[Board | None]]:
    draws = [int(d) for d in ll.pop(0).split(',')]
    nonempty = [l for l in ll if l]
    boards: list[Board | None] = [Board(nonempty[i:i + 5], i / 5) for i in range(0, len(nonempty), 5)]

    return draws, boards

def part1(ll: list[str]) -> str:
    draws, boards = parse_input(ll)

    for d in draws:
        for b in boards:
            assert b is not None
            ret = b.draw(d)
            if ret != False:
                return ret
    assert False, "no solution found"

def part2(ll: list[str]) -> str:
    draws, boards = parse_input(ll)

    num_boards = len(boards)
    # print(f"{num_boards} boards")
    remaining_boards = num_boards
    for d in draws:
        # print(f"draw {d}")
        for i, b in enumerate(boards):
            if not b:
                continue
            ret = b.draw(d)
            if ret is not False:
                # print(f"board {num_boards - remaining_boards + 1} complete!")
                # print(f"score {ret}")
                if remaining_boards == 1:
                    return ret
                boards[i] = None
                remaining_boards -= 1
    assert False, "no solution found"
