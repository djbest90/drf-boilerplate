import environ
import logging
import logging.config

env = environ.Env()

env.read_env(".env")

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": env.str("DB_ENGINE"),
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.get_value("DB_PASSWORD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"{env.str('REDIS_URL', 'redis://localhost:6379/0')}",
        "KEY_PREFIX": "boilerplate",  # todo: you must change this with your project name or something else
    }
}

CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", "redis://localhost:6379")
CELERY_RESULT_BACKEND = env.str("CELERY_BROKER_URL", "redis://localhost:6379")

CELERY_TIMEZONE = "Asia/Tashkent"

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

ALLOWED_HOSTS=['*']
CORS_ORIGIN_ALLOW_ALL = True

config =  {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
            "file": {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': 'log/app.log',
                'maxBytes': 1024*1024*5, # 5MB
                'backupCount': 5,
                'formatter': 'verbose',
            },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],   
            "level": "INFO",    
            "propagate": True,
        },
    }
}

try:
    logging.config.dictConfig(config)
    logger = logging.getLogger()
    logger.debug('This is a debug message')
except ValueError as e:
    print(f"Error configuring logging: {e}")