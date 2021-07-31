from helper import CheggHelper
import os

ff = CheggHelper()

email = os.environ['mail']
password = os.environ['password']

ff.tryLogin(email, password)