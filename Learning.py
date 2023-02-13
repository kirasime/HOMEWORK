from math import sqrt
print(" ")
print ("Вариант 22\n  a) 6/11 = 0.545, sqrt(83) = 9.11 \n  б) 3.7832(+-)0.0043 \n  в) 2.678" )
print(" ")

num_1_rounded = 0.545
num_2_rounded = 9.11


num_1 = round(6/11, 6)
num_2 = round(sqrt(83), 6)

limit_1 = num_1 - num_1_rounded
limit_2 = num_2 - num_2_rounded

percentage_1 = round((limit_1 / num_1_rounded) * 100, 5)
percentage_2 = round((limit_2 / num_2_rounded) * 100, 5)

print("a) compare", percentage_1, "and", percentage_2, "(percents)")

if percentage_1 > percentage_2:
    print("   Answer: sqrt(83) is more accurate than 6/11")
    print(' ')
else:
    print("   Answer: 0.545 is more accurate than sqrt(83)")
    print(' ')

##################################################################
num_b = 3.7832
num_b_plus = 0.0043

#   0.0043, ближайшее число 0.005
#   0.003 меньше чем 0.005 -> округлим число до двух знаков без всяких изменений

print("б) Answer:", round(num_b, 2))
print(" ")

##################################################################

num_c = 2.678

num_c_absolute = 0.0005
num_c_relative = num_c_absolute / num_c

print("в)  Абсолютная погрешность", num_c_absolute)
print("    Относительная погрешность", round(num_c_relative, 4)*100)






