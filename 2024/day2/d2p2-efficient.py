import sys
import numpy as np
def isOk(seq):
    a = np.diff(seq)
    if (a<0).sum() > (a>0).sum():
        a = -a
    risingOk = (1 <= a) & (a <= 3)
    return risingOk.sum() - len(risingOk),risingOk


totalSafe = 0
with open(sys.argv[1],"r") as f:
    for i in f:
        nums = np.array(list(map(int,i.split())))
        errors, risingOk = isOk(nums)


        if errors < -2:
            continue
        if errors == 0:
            totalSafe += 1
            continue


        if sys.argv[2] == "a":
            continue
        elif sys.argv[2] != "b":
            assert False


        errLoc, = np.where(risingOk == False)
        errLoc = errLoc[:1]
        totalSafe += (
            isOk(np.delete(nums,errLoc  ))[0] == 0 or 
            isOk(np.delete(nums,errLoc+1))[0] == 0
            )


print(totalSafe)