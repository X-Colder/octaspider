#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:pitmaner
# Datetime:2018/2/9 上午9:41
# Software: PyCharm
# Project: tushare_test
# Filename: demo01

import tushare as ts
import tornado.ioloop
import tornado.web
import pymongo
import json
import sys


MONGODB_CONFIG = {
    'host': '10.40.35.39',
    'port': 27017,
    'db_name': 'stock',
    'username': None,
    'password': None
}


class MongoConn(object):

    def __init__(self):
        # connect db
        try:
            self.conn = pymongo.MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
            self.db = self.conn[MONGODB_CONFIG['db_name']]  # connect db
            self.username = MONGODB_CONFIG['username']
            self.password = MONGODB_CONFIG['password']
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True
        except Exception as e:
            print(e)
            print('Connect Statics Database Fail.')
            sys.exit(1)
