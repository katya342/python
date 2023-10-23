if __name__ == "__name__":
    competent = True
    responsible = True
    print (competent and responsible)

competent = True
responsible = False
print (competent and responsible)

competent = True
responsible = False
print (competent or responsible)

competent = False
responsible = False
print(competent or responsible)

previously_fired = True
print (not previously_fired)

previously_fired = False
print (not previously_fired)

time = int(input ("Enter the current time in hours: "))% 24
ticket = False
money = True
luggage = False
print (money or ticket and not luggage and time > 6)
print((money or ticket) and not luggage and time > 6 )