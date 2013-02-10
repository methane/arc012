from __future__ import division
import sys

N, va, vb, L = map(int, sys.stdin.readline().split())

for i in range(N):
    L = vb * (L / va)

print(L)
