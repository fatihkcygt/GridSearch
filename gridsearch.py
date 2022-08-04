#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    first_index_arr = []
    for j in range(len(G)):
        count = j
        if str(P[0]) in str(G[j]):
            n = 0
            while n <= len(G[j]) - 1:
                if P[0] in G[j][n:]:
                    first_index_arr.append(str(G[j][n:]).find(P[0]) + n)
                    n = (str(G[j][n:]).find(P[0]) + n) + len(P[0])
                else:
                    break
            print(first_index_arr)
            for i in range(1, len(P)):
                count += 1
                for x in first_index_arr:
                    if P[i] not in G[count][x:x + len(P[i])]:
                        first_index_arr.remove(x)

                if len(first_index_arr) == 0:
                    break
                if i == len(P) - 1:
                    return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
