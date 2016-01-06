#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

height = float(input('please input you height: '))
weight = float(input('please input you weight: '))

BMI = weight/(height*height)
print('your BMI is : ',BMI)
if BMI<18.5 :
    print('too slow')
elif BMI<=25:
    print('normal')
elif BMI<=28:
    print('too heavey')
elif BMI<=32:
    print('very heavey')
else :
    print('very very heavey')

