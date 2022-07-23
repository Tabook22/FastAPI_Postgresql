import asyncio 

async def getnumbers(x):
    print("Just started the process will take 5 seconds ")
    #the sleep statement would typically represents an IO operation 
    await asyncio.sleep(5)
    for i in range(x):
        print(i)
    print("In the Name of Allah")
    
async def main():
    print("*" * 50)
    print("--Start of Process--")
    await getnumbers(10) # Calling the getnumbers
    print("Thank God")
    print("*" * 50)
    print("--End of Process--")
    

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(5.0)
    return x + y

async def print_sum(x, y):
    #here we add taks
    Task1=asyncio.create_task(compute(x, y))
    Task2=asyncio.create_task(printnumbers(x))
   # result = await compute(x, y)
    result=await Task1
    print("still waitting")
    print("%s + %s = %s" % (x, y, result))
    await Task2
async def printnumbers(n):
    for i in range(n):
        print(i)
        await asyncio.sleep(3.0)

#Her we instantiate a loop. keep in mind that instatiation means creating a new object from a class
loop = asyncio.get_event_loop()

#here we start the loop, and we passing our coroutin(here print_sum(x,y) is th coroutine)
loop.run_until_complete(print_sum(5, 2))
loop.close()


#if __name__=="__main__":
    #this is the starting point for our asyncio 
   # asyncio.run(main())