#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/11 11:06 下午 
# @Author : Aries 
# @File : conftest.py 
# @Software: IntelliJ IDEA
# 参数和结合fixture使用
# 1。传入值和数据
# 2。传入fixture方法 将数据传入到fixture方法中，
#       fixture使用request接受数据，方法体中使用request.param使用数据


import pytest
import yaml


@pytest.fixture()
def calc():
    print("开始计算")
    # yield 激活fixture的teardown方法
    # print(request.param[0])
    yield
    print("计算结束")


# session每个项目执行一次 module每个py文件执行一次
@pytest.fixture()
def login():
    print("登陆")
    # yield 激活fixture的teardown方法
    # print(request.param[0])
    yield ['username', 'password']
    print("teardown")
