#!/usr/bin/python
activate_this = '/var/www/FlaskApp/app/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0,"/var/www/FlaskApp/app")
from app import app as application
