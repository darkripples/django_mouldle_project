#!/usr/bin/env python
# coding:utf8
"""
@Time       :   2019/09/02
@Author     :   fls
@Contact    :   fls@darkripples.com
@Desc       :   darkripples总平台相关

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/09/02 11:41   fls        1.0         create
2019/12/07 10:23   fls        1.1         增加统计类
"""

from django.urls import path, include
from django.apps import apps
from django.conf.urls.static import static as urls_static
from django.conf import settings
from django.conf.urls import url
from django.views import static as views_static

from .views import index, upload_file
from .views_ws import wsocket_init, api_websocket_msg

# 不可删除
app_name = apps.get_app_config('app_dr').name

urlpatterns = [

    # websocket
    path('wsocketInit/', wsocket_init),
    path('websocketMsg/', api_websocket_msg),

    path(r'index/', index),
    # 其它api
    path(r'api/', include('app_dr.ifs.urls', namespace='app_dr_ifs')),

    # 通用文件上传
    path(r'uploadFile/', upload_file),

    # 静态文件
    url(r'^static/(?P<path>.*)$', views_static.serve,
        {'document_root': settings.STATIC_DIR}, name='static'),
]

# 静态文件.settings.DEBUG=True时会用到
urlpatterns += urls_static('/static/', document_root=settings.STATIC_DIR)
