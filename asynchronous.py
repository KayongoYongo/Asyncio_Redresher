import time
import asyncio

async def brewCoffee():
    print("Start Brew coffee")
    # Some functions are awaitable, others are not
    await asyncio.sleep(3)
    print("End brew coffee")
    return "Coffee ready"

async def toastBagel():
    print("Start toasting Bagel")
    # Some functions are awaitable, others are not
    await asyncio.sleep(5)
    print("End toasting Bagel")
    return "Bagel ready"

async def main():
    start = time.time()
    # The batch stores the coroutine objects
    # batch = asyncio.gather(brewCoffee(), toastBagel())
    # result_coffee, result_bagel = await batch

    coffee_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toastBagel())

    result_coffee = await coffee_task
    result_bagel = await toast_task

    end = time.time()

    elapsed_time = end - start

    print(f"The elapsed time is {elapsed_time}")
    print(f"The result of coffee is {result_coffee}")
    print(f"The result of bagel is {result_bagel}")

if __name__ == "__main__":
    # Since the function is a coroutine, it gets called in a different way
    asyncio.run(main())