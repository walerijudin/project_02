# 1

print("Буква q -  выход")
while True:
    s = input("Sign (+, -, *, /):")
    if s == "q":
        break

    if s in ("+", "-", '*', "/"):
        x = float(input("x =  "))
        y = float(input("y =  "))
        if s == "+":
            print(x + y)
        elif s == "-":
            print(x - y)
        elif s == "*":
            print(x * y)
        elif s == "/":
            if y != 0:
                print(x / y)
            else:
                print("delenie na 0")
    else:
        print("ne korrektny znak")

# 2


print("Буква q -  выход")
while True:
    s = input("Sign (+, -, *, /):")
    match s:
        case "q":
            break
        case "+":
            x = float(input("x =  "))
            y = float(input("y =  "))
            print(x + y)
        case "-":
            x = float(input("x =  "))
            y = float(input("y =  "))
            print(x - y)
        case "*":
            x = float(input("x =  "))
            y = float(input("y =  "))
            print(x * y)
        case "/":
            x = float(input("x =  "))
            y = float(input("y =  "))
            if y != 0:
                print(x / y)
            else:
                print("delenie na 0")
        case _:
            print("ne korrektny znak")



# блок try exept finally

x = 5
y = 0
try:
    print(x / y)
except ZeroDivisionError:
    print("delenie na 0")
else:
    print("block else")
finally:
    print("block finally")





    
        