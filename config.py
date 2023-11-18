import os

basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = 'tu_clave_secreta_para_Flask'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://invipv6:invipv6++@localhost/invipv6'