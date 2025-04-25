print("Welcome to the Bill Splitter app")
history = []

while True:
    choice = input("Enter 'split' to split the bill, 'history' to view past splits, 'clear' to delete history and 'quit' to exit: ").lower().strip()
    if choice == "quit":
        print("See you later")
        break
    elif choice == "split":
        bill = float(input("Enter total bill amount: "))
        people = int(input("Enter the number of people: "))
        tip_percent = float(input("Enter the tip percentage e.g(15 for 15%): "))
        if bill < 0 or people <= 0 or tip_percent < 0:
            print("Invalid input. Try again")
        else:
            tip = bill*(tip_percent/100)
            total = bill+tip
            unequal = input("Unequal split, Yes or No: ").lower().strip() == "yes"
            custom_payments = []
            remaining_total = total
            remaining_people = people
            if unequal:
                print(f"Enter custom amount upto {people-1} people (remaining split evenly): ")
                for i in range(people-1):
                    custom = input(f"Custom amount for person {i+1} (or 'done'): ").strip()
                    if custom == "done":
                        break   
                    try:
                        amount = float(custom)
                        if amount < 0 or amount > remaining_total:
                            print("Invalid amount")
                            break
                        custom_payments.append(amount)
                        remaining_total -= amount
                        remaining_people -= 1
                    except ValueError:
                        print("Invalid input")
                        break
            if remaining_people > 0:
                share = remaining_total/remaining_people
                print(f"Total with tip: ${total:.2f}")
                for i,amount in enumerate(custom_payments,1):
                    print(f"Person {i} pays: ${amount:.2f}")
                for i in range(len(custom_payments)+1,people+1):
                    print(f"person {i} pays: ${share:.2f}")
            else:
                print("To many custom payments")
                continue
            history.append([bill,people,tip_percent,custom_payments+[share]*remaining_people])
    elif choice == "history":
        if not history:
            print("No spilts yet")
        else:
            print("\n Past splits: ")
            for i,split in enumerate(history,1):
                bill,people,tip_percent,shares = split
                print(f"Split {i}: Bill = ${bill:.2f}, People = {people}, Tip = {tip_percent}%, Shares = [{', '.join(f"${s:.2f}" for s in shares)}]")
    elif choice == "clear":
        ques = input("Do you want to delete al history. Yes/No").lower().strip()
        if ques == "yes":
            history.clear()
            print("History cleared.")
    else:
        print("Invalid choice")