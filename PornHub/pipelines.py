# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from PornHub.items import PornVideoItem


class PornhubMongoDBPipeline(object):
    def __init__(self):
        # 提供 MongoDB 服务器的地址、端口以及认证信息
        clinet = pymongo.MongoClient("localhost", 27017, username='wq', password='qifeng')
        # 选择数据库,不存在则创建
        db = clinet["PornHub"]
        # 选择集合,不存在则创建
        self.PhRes = db["PhRes"]

    def process_item(self, item, spider):
        print('MongoDBItem', item)
        """ 判断类型 存入MongoDB """
        if isinstance(item, PornVideoItem):
            print('PornVideoItem True')
            try:
                self.PhRes.insert(dict(item))
            except Exception:
                pass
        return item
