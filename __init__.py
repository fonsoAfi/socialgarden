# check compatibility
import py4web
from py4web import Session
import os
import secrets

assert py4web.check_compatible("0.1.20190709.1")

# by importing db you expose it to the _dashboard/dbadmin
from .models import db

# import the scheduler
from .tasks import scheduler

# by importing controllers you expose the actions defined in it
from . import controllers

# optional parameters
__version__ = "0.0.0"
__author__ = "you <you@example.com>"
__license__ = "anything you want"
 
session = Session(
    secret=os.getenv("PY4WEB_SESSION_SECRET"),
    expiration=1800,  
    same_site="Strict",
)