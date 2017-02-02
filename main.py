def FizzBuzz(number):
    if (number > 0):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return number
    else:
        return number

for i in range(0,100):
    print(FizzBuzz(i))