import sys

dow = sys.stdin.readline().strip()[:3]

remains = dict(
        Mon=5,
        Tue=4,
        Wed=3,
        Thu=2,
        Fri=1,
        Sat=0,
        Sun=0
        )

print(remains[dow])
