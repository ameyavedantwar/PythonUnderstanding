km = 10
const = 1.609344
km_to_miles = km/const
print(km_to_miles)

celcius = 35
fahrenheit = celcius*1.8
print(fahrenheit)

import calendar
yyyy = 2023
mm = 4
print(calendar.month(yyyy, mm))

#ax^2 + bx + c
#assuming values
a = 1
b = 5
c = 6

#formula = ((b^2 - 4ac)^0.5) / 2a
d = (b**2) - (4*a*c)
import math

sol1 = ((-b-math.sqrt(d)))/(2*a)
sol2 = ((-b+math.sqrt(d)))/(2*a)
print('{} , {}'.format(sol1, sol2))