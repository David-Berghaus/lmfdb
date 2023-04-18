# -*- coding: utf-8 -*-

from lmfdb.app import app
from lmfdb.logger import make_logger
from flask import Blueprint

nmf_page = Blueprint("nmf", __name__, template_folder='templates', static_folder="static")
nmf = nmf_page
nmf_logger = make_logger(nmf_page)

from . import main
assert main # silence pyflakes

app.register_blueprint(nmf_page, url_prefix="/Add/this/later")
