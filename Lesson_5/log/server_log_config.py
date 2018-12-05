import logging
import datetime


today = str(datetime.date.today())
name_file = f'server_log_{today}.log'

logger = logging.getLogger('server-log')
logger.setLevel(logging.INFO)

fh = logging.FileHandler(f'log/server-log/{name_file}', encoding='utf-8')
fh.setLevel(logging.INFO)
_format = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")
fh.setFormatter(_format)
logger.addHandler(fh)
