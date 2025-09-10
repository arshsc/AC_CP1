# AC 2nd Crew Shares

money_earned = float(input("How much money was earned: "))
crew_count = float(input("How many crew members are there: "))

money_earned = money_earned - (crew_count * 500)
print(money_earned)

share = (money_earned / crew_count) * 2
captain_money_amount = share * 7
print(captain_money_amount)