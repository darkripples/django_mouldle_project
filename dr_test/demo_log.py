#!/usr/bin/env python
# coding:utf8
"""
@Time       :   2020/7/9
@Author     :   fls    
@Contact    :   fls@darkripples.com
@Desc       :   For log

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 14:42   fls        1.0         create
"""


def t_01():
    from ez_utils import flog
    flog.debug('this is a debug level message')
    flog.info('this is info level message')
    flog.warning('this is warning level message')
    flog.error('this is error level message')
    flog.critical('this is critical level message')


if __name__ == '__main__':
    t_01()
