balance = 5000
statement=[]

while True:

    print("\nATM MENU")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Statement")
    print("5.Exit")

    choice=input("Enter choice: ")

    if choice=="1":
        print("Balance =",balance)

    elif choice=="2":
        amount=float(input("Enter deposit amount: "))
        balance+=amount
        statement.append(f"Deposited {amount}")

    elif choice=="3":
        amount=float(input("Enter withdraw amount: "))
        
        if amount>balance:
            print("Insufficient Balance")
        else:
            balance-=amount
            statement.append(f"Withdrawn {amount}")

    elif choice=="4":
        for i in statement:
            print(i)

    elif choice=="5":
        break

    else:
        print("Invalid Choice")