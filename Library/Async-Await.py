import asyncio
async def my_function():
    result = await some_async_operation()
    print('Result:', "Hello World")
    return result

def some_async_operation():
    return asyncio.sleep(5)


print(asyncio.run(my_function()))