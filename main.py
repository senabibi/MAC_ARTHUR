def trick():
    print("This is a puzzle favored by Gen.MacArthur.You will be asked to \nsecretly type in your birthday month(as an integer) and your age\nThe computer will make a special calculation,yielding a new integer\nThe computer will then calculate,using only that special number,your\n birth month ang age")
    month=int(input("Give me your birth month:"))
    age=int(input("Give me your age:"))
    double=month*2
    add=double+5
    mutiply=add*50+age
    subs=mutiply%365
    fin=subs+115
    fins=fin%100
    print(f"The special number is:{subs}")
    print(f"The computer calculates then that you were born in the {month}\n and are {fins}")
trick()