d1,m1,y1 = input().split('.')
d2,m2,y2 = input().split('.')

day1 = int(d1)
month1 = int(m1)
year1 = int(y1)

day2 = int(d2)
month2 = int(m2)
year2 = int(y2)

years_passed = year2 - year1
birthday2 = years_passed
if (month2 > month1 or (month2 == month1 and day2 >= day1)):
    birthday2 += 1

N1 = years_passed // 400
N2 = years_passed // 4
N3 = years_passed // 100

birthday1 = N1 + N2 - N3 + 1
if ((month2 == 1 or (month2==2 and day2<29)) and (year2 % 400 == 0 or (year2 % 100 != 0 and year2 % 4 == 0))):
    birthday1 -= 1

if (day1 == 29 and month1 == 2):
    birthday2 = birthday1

print(birthday1, birthday2)
