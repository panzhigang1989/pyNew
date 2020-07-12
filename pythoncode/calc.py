#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/11 10:47 上午 
# @Author : Aries 
# @File : calc.py 
# @Software: IntelliJ IDEA
# 计算器功能

from decimal import Decimal


class Calculator:
    # 加法
    def add(self, a, b):
        return Decimal(str(a)) + Decimal(str(b))

    # 除法
    def div(self, a, b):
        if b == 0:
            print('除数不能为0')
            return 0
        else:
            return Decimal(a / b).quantize(Decimal('0.00'))

    # 减法
    def decrease(self, a, b):
        return Decimal(a-b).quantize(Decimal('0.00'))

    # 乘法
    def multiplication(self, a, b):
        return Decimal(a * b).quantize(Decimal('0.00'))