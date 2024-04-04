import time

def brewCoffee():
    print("Start Brew coffee")
    time.sleep(3)
    print("End brew coffee")
    return "Coffee ready"

def toastBagel():
    print("Start toasting Bagel")
    time.sleep(5)
    print("End toasting Bagel")
    return "Bagel ready"

def main():
    start = time.time()
    result_coffee = brewCoffee()
    result_bagel = toastBagel()
    end = time.time()

    elapsed_time = end - start

    print(f"The elapsed time is {elapsed_time}")
    print(f"The result of coffee is {result_coffee}")
    print(f"The result of bagel is {result_bagel}")

if __name__ == "__main__":
    main()