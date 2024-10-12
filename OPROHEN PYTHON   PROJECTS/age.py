name = input('What is you name: ')
gender = input('Enter gender (M/F): ')
if gender.upper()=='M':
 print('MR: ' + str(name  ) +    '  Help us find you age')
else:
    if gender.upper()=='F':
     print('MS : ' + str(name  ) +    '  Help us find you age')
year1 = int(input('Enter year of birth:    '))
year2 = int(input('Enter the currernt year:    '))
age = (year2 - year1)
print(age)
print('You are :' + str(age) + 'years old')
if age < 0 or age > 50:
    print('you are at old age zone')
elif age >=0 and age <=2:
    print('You are a toddler')
elif age >=3 and age <= 5:
    print('You are preschooler')
elif age >=6 and age <= 12:
    print('You are at school age child')
elif age >=13 and age<= 14:
    print('You are an early teenager')
elif age >=15 and age<= 17:
    print('You are a mid-teenager')
elif age >=18 and age<= 19:
    print('You are a mid-teenager')
elif age >=20 and age<= 24:
    print('You are a young adult')
elif age >=23 and age<= 29:
    print('You are an adult')
elif age >= 39:
    print('You are at mid-adulthood')
elif age >=40 and age<= 50:
    print('You are at middle age adulthood')
else:
    print('You are at old age Zone') 
