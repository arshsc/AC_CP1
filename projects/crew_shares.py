# AC 2nd Crew Shares

money_earned = float(input("How much money was earned: "))
crew_count = int(input("How many crew members are there: "))

money_after_divvy = money_earned - (crew_count * 500)
crew_count_updated = crew_count - 2
share = (money_after_divvy / crew_count_updated)

captain_shares = share * 7
first_mate_shares = share * 3
crew_shares = share - 500

print(f"\nHow much was earned: ${money_earned:,.2f}")
print(f"How many crew members are there: {crew_count}")
print(f"The captain gets: ${captain_shares:,.2f}")
print(f"The first mate gets: ${first_mate_shares:,.2f}")
print(f"The crew still needs: ${crew_shares:,.2f}")