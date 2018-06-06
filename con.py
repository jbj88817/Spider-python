import sys


def problem1_6():
    for i in range(1, 101, 2):
        sys.stdout.write(str(i) + ' ')
        sys.stdout.flush()


if __name__ == '__main__':
    problem1_6()
