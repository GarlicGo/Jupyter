#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：error_type.py
@Author  ：zhaolin
@Date    ：2022/5/9 17:10
"""
from enum import Enum


class ErrorType(Enum):
    DISTANCE_1 = 1  # 压接位置到绝缘皮位置错误
    DISTANCE_2 = 2  # 绝缘皮裸露长度错误
    LINE_ERROR = 3  # 线芯污染或损坏
    TUBE_ERROR = 4  # 压线筒污染或损坏
    TUBE_BENDING = 5  # 压线筒弯曲
    SUCCESS = 6  # 一切正常
    UNKNOWN = 0  # 未知


error_type_map = {
    ErrorType.DISTANCE_1: "压痕位置与压线筒端子距离异常",
    ErrorType.DISTANCE_2: "压线筒端子与线芯绝缘层距离异常",
    ErrorType.LINE_ERROR: "线芯污染或损坏",
    ErrorType.TUBE_ERROR: "压线筒污染或损坏",
    ErrorType.TUBE_BENDING: "压线筒弯曲",
    ErrorType.SUCCESS: "未检测到异常",
    ErrorType.UNKNOWN: "图片异常"
}
error_type_value_map = {
    ErrorType.DISTANCE_1.value: "压痕位置与压线筒端子距离异常",
    ErrorType.DISTANCE_2.value: "压线筒端子与线芯绝缘层距离异常",
    ErrorType.LINE_ERROR.value: "线芯污染或损坏",
    ErrorType.TUBE_ERROR.value: "压线筒污染或损坏",
    ErrorType.TUBE_BENDING.value: "压线筒弯曲",
    ErrorType.SUCCESS.value: "未检测到异常",
    ErrorType.UNKNOWN.value: "图片异常",
}
error_type_text_map = {
    "压痕位置与压线筒端子距离异常": ErrorType.DISTANCE_1.value,
    "压线筒端子与线芯绝缘层距离异常": ErrorType.DISTANCE_2.value,
    "线芯污染或损坏": ErrorType.LINE_ERROR.value,
    "压线筒污染或损坏": ErrorType.TUBE_ERROR.value,
    "压线筒弯曲": ErrorType.TUBE_BENDING.value,
    "未检测到异常": ErrorType.SUCCESS.value,
    "图片异常": ErrorType.UNKNOWN.value,
    '全部': -1
}
