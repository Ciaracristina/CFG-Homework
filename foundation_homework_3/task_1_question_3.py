year = int(input('What year was your book written? '))

century = int(year / 100)

if century == 18:
    century_output = "Eighteenth"
elif century == 19:
    century_output = "Nineteenth"
else:
    century_output = "Unknown"

decade = int((year / 10) % 10)

if decade == 0:
    decade_output = "Noughties"
elif decade == 1:
    decade_output = "Tens"
elif decade == 2:
    decade_output = "Twenties"
elif decade == 3:
    decade_output = "Thirties"
elif decade == 4:
    decade_output = "Forties"
elif decade == 5:
    decade_output = "Fifties"
elif decade == 6:
    decade_output = "Sixties"
elif decade == 7:
    decade_output = "Seventies"
elif decade == 8:
    decade_output = "Eighties"
elif decade == 9:
    decade_output = "Nineties"
else:
    decade_output = "Unknown"

print("{} Century, {}".format(century_output, decade_output))
