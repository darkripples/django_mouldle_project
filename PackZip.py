#!/usr/bin/env python
# coding:utf8
"""
@Time       :   2019/11/15
@Author     :   fls
@Contact    :   fls@darkripples.com
@Desc       :   打包项目文件

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/11/15 15:27   fls        1.0         create
"""

import zipfile
from ez_utils import walk_dir

IGNORE_LIST = [".idea", ".git", ".pyc", ".gitignore", "darkripples_pack.zip", "PackZip.py",
               "docs", "logs", "upload", "UnZipPack.sh",
               "README.md", ]


def main():
    filesPathList = walk_dir("./", include_dir=False)
    f = zipfile.ZipFile('darkripples_pack.zip', 'w', zipfile.ZIP_STORED)
    for filePath in filesPathList:
        canNeed = 1
        for i in IGNORE_LIST:
            if i in filePath:
                canNeed = 0
                break
        if canNeed:
            print(filePath)
            f.write(filePath)

    print("over")
    f.close()


if __name__ == "__main__":
    main()
