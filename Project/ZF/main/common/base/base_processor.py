#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：base_processor.py
@Author  ：zhaolin
@Date    ：2022/3/14 15:11
"""
import abc
from typing import Any

from numpy import ndarray

from common.utils.timeit import timeit


class BaseImageProcess(metaclass=abc.ABCMeta):
    @timeit
    @abc.abstractmethod
    def process_image(self, image: ndarray) -> (ndarray, Any):
        """
        :param image: 读入的图片
        :return: 第一个返回值是处理后的图片，第二个返回值是额外的信息，包括异常的位置、轮廓(如果有)等信息
        """
        pass

