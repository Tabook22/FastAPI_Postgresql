#https://www.youtube.com/watch?v=xWt5lpn8fN8
#Here we run three coroutines parall to each other (at the same time)
import asyncio

async def myfuncA():
    while True:
        await asyncio.sleep(1)
        print("In The Name of Allah")
        
async def myfuncB():
    while True:
        await asyncio.sleep(1)
        print("Glory be to Allah and praise him Subhan Allah Almighty")

async def myfuncC():
    while True:
        await asyncio.sleep(1)
        print("Thank Allah")
              
#instantiate (creating object from a class)
loop=asyncio.get_event_loop()
try:
    asyncio.ensure_future(myfuncA())
    asyncio.ensure_future(myfuncB())
    asyncio.ensure_future(myfuncC())
    loop.run_forever()    
except KeyboardInterrupt:
    pass
finally:
    print("Glory be to Allah Almighty")
    loop.close()