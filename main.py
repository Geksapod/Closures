import fibonacci as fib
import generator as ge
import list_sum as ls
import timeit

if __name__ == "__main__":

    # Task 1

    print(f"{'Task #1':-^60}")

    seq = ge.gen(1, 5, lambda x: x ** 2)
    for i in seq:
        if i == 9:
            seq.close()
        print(i, end=", ")

    print()

    # Task 2
    print(f"{'Task #2':-^60}")

    res = fib.fibonacci_memo()
    for i in range(1, 20):
        print(res(i), end=", ")

    stm_1 = """import fibonacci as fib"""
    s_1 = """
res_1 = fib.fibonacci_memo()
res_1(20)
"""
    print(f"memoization -> {timeit.timeit(stmt=s_1, setup=stm_1, number=1000)} c")

    for i in range(1, 20):
        print(fib.fibonacci_recur(i), end=", ")

    stm_2 = """import fibonacci as fib"""
    s_2 = """
res_2 = fib.fibonacci_recur(20)
"""
    print(f"recursion -> {timeit.timeit(stmt=s_2, setup=stm_2, number=1000)} c")

    # Task 3

    print(f"{'Task #3':-^60}")

    list_to_check_1 = [1, 2, 3, 4, 5]

    r = ls.list_sum(list_to_check_1, lambda x: x if not x % 2 else 0)

    print(f"The sum of the list is {r()}")

    # Or
    print("-" * 60)

    list_to_check_2 = [1, 2, 3, 4, 5]
    res = map(lambda x: x if not x % 2 else 0, list_to_check_2)
    print(f"The sum of the list is {sum(res)}")


