from test_process import *
from threading import Thread
import time

jobs = []
tm = time.time()
for i in range(10):
    p = Thread(
        # target=count, args=(1, 1,)
        target=io
    )
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()

print('thread cpu', time.time() - tm)
# thread cpu 8.788640022277832
# thread cpu 6.039309024810791
