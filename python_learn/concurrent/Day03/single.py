"""
测试多进程，线程开发效率

"""
import time
from test_process import *

tm = time.time()
for i in range(10):
    # count(1,1)
    io()
print('single cpu', time.time() - tm)
# single cpu 10.201550006866455
# single cpu 6.055437088012695
# process cpu 2.203495979309082
# process cpu 1.4692959785461426
# thread cpu 8.788640022277832
# thread cpu 6.839309024810791
