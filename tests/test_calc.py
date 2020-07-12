#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 11:46 下午
# @Author : Aries
# @File : test_calc.py
# @Software: IntelliJ IDEA
#
import pytest
import sys

import yaml

sys.path.append("..")
print(sys.path)

from pythoncode.calc import Calculator
from decimal import Decimal


class TestCalc:

    # 类里面执行
    def setup_class(self):
        print("类级别setup")
        self.calc = Calculator()

    def teardown_class(self):
        print("类级别teardown")

    @pytest.mark.parametrize('list1', yaml.safe_load(open('./../calc.yml'))['add'])
    def test_add(self, list1, calc):
        add_result = self.calc.add(list1[0], list1[1])
        print(f'实际结果为：{add_result}, 类型为{type(add_result)}')
        assert Decimal(list1[2]).quantize(Decimal('0.00')) == add_result

    @pytest.mark.parametrize('list1', yaml.safe_load(open('./../calc.yml'))['div'])
    def test_div(self, list1, calc):
        assert Decimal(list1[2]).quantize(Decimal('0.00')) == self.calc.div(list1[0], list1[1])

    @pytest.mark.parametrize('list1', yaml.safe_load(open('./../calc.yml'))['decrease'])
    def test_decrease(self, list1, calc):
        assert Decimal(list1[2]).quantize(Decimal('0.00')) == self.calc.decrease(list1[0], list1[1])

    @pytest.mark.parametrize('list1', yaml.safe_load(open('./../calc.yml'))['multiplication'])
    def test_multiplication(self, list1, calc):
        print(list1)
        assert Decimal(list1[2]).quantize(Decimal('0.00')) == self.calc.multiplication(list1[0], list1[1])
