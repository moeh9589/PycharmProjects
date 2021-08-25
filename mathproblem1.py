import itertools
from time import sleep

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = list(itertools.permutations(nums))
a = 0
b = 1
c = 2
white = (255, 255, 255)
black = (0, 0, 0)


def check(a1, b1, c1):
    if a1 + c1 == b1:
        return True


def find_num_of_checks(n):
    times = len(n) // 2
    return times


def main():
    successes = 0
    total = 0

    for i in x:
        # print(i)
        # for j in range(find_num_of_checks(nums)):
        #     if check(i[a], i[b], i[c]):
        #         a += 3
        #         b += 3
        #         c += 3
        #         print("SUCCESS:")

        if check(i[0], i[1], i[2]) and check(i[2], i[3], i[4]) and check(i[4], i[5], i[6]) and check(i[6], i[7], i[8]):
            print()
            print("SUCCESS:")
            print(f"{i[0]} {i[2]} {i[4]} {i[6]} {i[8]} \n {i[1]} {i[3]} {i[5]} {i[7]}")
            sleep(1.5)
            successes += 1
            total += 1

        else:
            print()
            print(f"{i[0]} {i[2]} {i[4]} {i[6]} {i[8]} \n {i[1]} {i[3]} {i[5]} {i[7]}")
            total += 1

    print()
    print(f"Total successes: {successes} out of {total} permutations.")
    print(find_num_of_checks(nums))


main()
