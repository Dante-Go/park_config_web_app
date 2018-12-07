#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################################
# Copyright (C)2018 Liu Kai. All rights reserved
# Filename: config_default.py
# Author: LiuKai
# Description: 
# 
##############################################################

configs = {
	'debug': True,
	'db':{
		'host': '127.0.0.1',
		'port': 3306,
		'user': 'lk',
		'password': 'liukai',
		'database': 'DB_parking_config'
	},
	'session':{
		'secret': 'liukai'
	}
}
