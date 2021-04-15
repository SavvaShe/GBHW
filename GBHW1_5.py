pr = int(input("Enter proceed: "))
ol = int(input("Enter outlay: "))
if pr > ol:
    prof = pr-ol
    rent = prof/pr
    print(f"Great work. You have {prof} profitability.Your profitability is equal to {rent}")
    w = int(input("How many people work: "))
    print(f"{prof/w} for one worker")
elif pr == ol:
    print("You have reached zero")
else:
    print("Your company is operating at a loss")