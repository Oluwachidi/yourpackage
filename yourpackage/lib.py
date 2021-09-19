def try_me(num):
    for n in range(1, num+1):
        if n % 3 ==0 and n % 5 == 0:
            print("fizzbuzz")
        elif n % 3 == 0:
            print("fizz")
        elif n % 5 == 0:
            print("buzz")
        else:
            print(n)
try_me(15)
