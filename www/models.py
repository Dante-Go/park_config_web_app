#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################################
# Copyright (C)2018 Liu Kai. All rights reserved
# Filename: models.py
# Author: LiuKai
# Description: 
# 
##############################################################
import time, uuid

from orm import Model, StringField

def next_id():
	return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class ParkSettings(Model):
	__table__ = 'tbl_settings'
	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	parkCode = StringField(ddl='varchar(50)')
	billHttpUrl = StringField(ddl='varchar(200)')
	carHttpUrl = StringField(ddl='varchar(200)')
	img_1_url = StringField(ddl='varchar(200)')
	img_2_url = StringField(ddl='varchar(200)')
	img_3_url = StringField(ddl='varchar(200)')
	invoiceSite = StringField(ddl='varchar(100)')
	payStatusHttpUrl = StringField(ddl='varchar(200)')
	qcode = StringField(ddl='varchar(50)')
	qrcodeHttpUrl = StringField(ddl='varchar(200)')
	tcmName = StringField(ddl='varchar(50)')
	tmpCarPlate = StringField(ddl='varchar(200)')
