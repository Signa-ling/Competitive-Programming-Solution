import math
import time


def eratosthenes(num):
    if num > 1:
        search_list = [i for i in range(3, x+1)]
        prime_num_list = [2]
        while math.sqrt(x) > prime_num_list[-1]:
            search_num = prime_num_list[-1]
            search_list = [j for j in search_list if j % search_num != 0]
            prime_num_list.append(search_list.pop(0))

        prime_num_list.extend(search_list)
        return prime_num_list
    exit()


if __name__ == '__main__':
    x = int(input())
    start = time.time()
    prime_num = eratosthenes(x)
    finish = time.time() - start

    print("PrimeNumber: {0}\n Time: {1}".format(prime_num, finish)
          if len(prime_num) <= 5000 else "Time: {0}".format(finish))
