import time

import numpy as np


def sum_np():
    list = np.arange(15_000_000, dtype=np.int64)
    total = np.sum(list)
    print('Sum is:', total)

start_d = time.time()
sum_np()
end_d = time.time()
print(end_d - start_d)
# 0.039893388748168945