#!/usr/bin/env python
# coding:utf8
"""
@Time       :   2019/09/15
@Author     :   fls
@Contact    :   fls@darkripples.com
@Desc       :   darkripples总平台相关-应用内utils

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/09/15 08:43   fls        1.0         create
"""
from uuid import uuid1
from json import dumps, loads
from conf import REDIS_KEY_PRE_TOKEN
from ez_utils import RedisCtrl, ParamsVerifyError, get_ip


def req_invalid_check(req):
    """
    request合法性校验
    :param req:
    :return: 校验通过return ''，否则return错误信息
    """
    flag, ip = "", get_ip(req)
    # todo 此处修改自己的逻辑

    if flag:
        flag = f"当前客户端外网IP:{ip}.请斟酌调取本接口"
    return flag


def create_token(user_info: dict, expt=None):
    """
    生成token
    :param user_info: 必须为json字典，尽量简短
    :param expt: 过期时间(秒)
    :return:
    """
    if user_info.get("id"):
        r = RedisCtrl()
        token = str(uuid1()).replace('-', '')
        if not expt:
            expt = 60 * 15
        elif expt == -1:
            expt = None
        r.set_one(REDIS_KEY_PRE_TOKEN + token, dumps(user_info), expt=expt)
        return token
    else:
        raise ParamsVerifyError("生成用户token需有`id`作为必填key")


def check_token(req_token):
    """
    校验token
    :param req_token:
    :return:
    """
    user_info = {}
    ret_info = None
    if not req_token:
        ret_info = "请登录后访问"
        return ret_info, user_info
    r = RedisCtrl()
    user_info = r.get_one(REDIS_KEY_PRE_TOKEN + req_token)
    if user_info:
        user_info = loads(user_info)
    else:
        ret_info = "无效的token"
    return ret_info, user_info


def upd_token_exp(req_token, expt=60 * 15):
    """
    更新token过期时间
    :param req_token:
    :param expt: 过期时间(秒)
    :return:
    """
    r = RedisCtrl()
    user_info = r.get_one(REDIS_KEY_PRE_TOKEN + req_token)
    if user_info:
        r.set_one(REDIS_KEY_PRE_TOKEN + req_token, user_info, expt=expt)
