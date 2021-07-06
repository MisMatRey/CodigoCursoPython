def fizzbuzz(list_num):
    for i in list_num :
        if (i % 3 == 0) and (i % 5 == 0) :
            print("FizzBuzz")
        elif (i % 3 == 0) :
            print("Fizz")
        elif (i % 5 == 0) :
            print("Buzz")
        else :
            print(i)

lista1 =  [1,2,3,4,5,15]

fizzbuzz(lista1)

