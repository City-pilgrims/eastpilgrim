# base.py의 모든 것을 가져오는 것
from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(
    env_file = os.path.join(BASE_DIR,'.env')
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['eastpilgrim.org', 'www.eastpilgrim.org', 'm.eastpilgrim.org', '64.176.228.128']

CSRF_TRUSTED_ORIGINS = [
    'https://eastpilgrim.org',
    'https://www.eastpilgrim.org',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# 쿠키 보안 설정 강화
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': read_secret('MYSQL_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}
