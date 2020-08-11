import asyncio
import json
import logging
import os
import uuid

import marshmallow as ma
from aiohttp import web
from aiohttp_jinja2 import template, render_template

from app.objects.secondclass.c_link import Link
from app.service.app_svc import Error
from app.service.auth_svc import check_authorization
from app.utility.base_world import BaseWorld

class BaseView(BaseWorld, web.view):
    def __init__(self, services):
        self.log = logging.getLogger('rest_api')
        self.data_svc = services.get('data_svc')
        self.app_svc = services.get('app_svc')
        self.auth_svc = services.get('auth_svc')
        self.file_svc = services.get('file_svc')
        self.rest_svc = services.get('rest_svc')



