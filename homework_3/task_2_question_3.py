import random

ticketNumbers = [7, 13, 5, 22, 28, 19, 41]

lotteryNumbers = []

for i in range(0, 7):
    number = random.randint(1, 50)

    while number in lotteryNumbers:
        number = random.randint(1, 50)

    lotteryNumbers.append(number)

lotteryNumbers.sort()

print(">>> Today's lottery numbers are: ")
print(lotteryNumbers)

matchingNumbers = set(lotteryNumbers).intersection(set(ticketNumbers))

if len(matchingNumbers) > 2:
    print('You have won a prize')

else:
    print('Sorry, no luck this time')

