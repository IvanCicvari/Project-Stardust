import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:SQL@.\SQLExpress2/Stardust?driver=ODBC+Driver+17+for+SQL+Server'
    
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                'log_colors': {
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'red,bold',
                },
            },
        },
        'handlers': {
            'console': {
                'class': 'colorlog.StreamHandler',
                'formatter': 'colored',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'default',
            },
        },
        'root': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    }
