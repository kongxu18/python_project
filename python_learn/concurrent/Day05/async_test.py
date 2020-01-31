"""
    协程
    asyncio 标准库模块 生态不好
    原因：只有asyncio 内部提供的协程阻塞 才能提供跳转
"""
import asyncio


async def fun01():
    print('s1')
    # 设置一个跳转节点
    await asyncio.sleep(2)
    print('end1')


async def fun02():
    print('s2')
    await asyncio.sleep(3)
    print('end2')


cor1 = fun01()
cor2 = fun02()

task = [asyncio.ensure_future(cor1),
        asyncio.ensure_future(cor2)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
