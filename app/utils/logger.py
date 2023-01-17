import logging
import os
import yaml


def get_logger(name: str = '', log_dir: str = '/var/log/app'):
    base = os.path.dirname(os.path.abspath(__file__))
    conf_file = os.path.join(base, 'logger.yml')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        logfile = f'{log_dir}/app.log'
        open(logfile, 'w')

    with open(conf_file, 'r') as f:
        logging.config.dictConfig(yaml.safe_load(f))

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    return logger
