#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################################
# Copyright (C)2018 Liu Kai. All rights reserved
# Filename: handlers.py
# Author: LiuKai
# Description: 
# 
##############################################################

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post
from models import ParkSettings, next_id

@get('/')
async def index(request):
	config = await ParkSettings.findByField('parkCode', '20000002')
	return {
		'__template__': 'test.html',
		'config': config
	}

@get('/api/settings')
async def api_get_settings():
	settings = await ParkSettings.findByField('parkCode', '20000002')
	if settings is None:
		return dict(settings=())
	return dict(settings=settings)
