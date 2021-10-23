from EnSite.settings.dev import SECRET_KEY
import os
from .build import *

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = "kjlsdkhdfakojtjsnKKSKALSnUB!GwfaYffsUgfdvd^784tef#()\lmgldm|lmslrfghxddgs"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost','http://enactusjmi.org/','enactus.org','35.244.7.161','127.0.0.1','enactus-300513.el.r.appspot.com','enactus-300513.appspot.com','enactusofficialwebsite-env.eba-xp4xt2nd.ap-south-1.elasticbeanstalk.com']
# STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
STATIC_URL = '/static/'
STATIC_ROOT = 'static'


