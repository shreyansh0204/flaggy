import os


class Config:
    SECRET_KEY = '5161bd589b12b4018bcc3515ad2be48e'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site1.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')