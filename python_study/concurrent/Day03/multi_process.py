from test_process import *
from multiprocessing import Process
import time

jobs = []
tm = time.time()
for i in range(10):
    p = Process(
        # target=count, args=(1, 1,)
        target=io
    )
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()

print('process cpu', time.time() - tm)
# process cpu 2.203495979309082
# process cpu 1.4692959785461426
