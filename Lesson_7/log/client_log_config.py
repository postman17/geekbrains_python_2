import logging
import datetime
import os


folder = os.path.dirname(os.path.abspath(__file__))
if folder.split('\\')[-1] != 'log':
    folder += '\log\client-log'
else:
    folder += '\client-log'

today = str(datetime.date.today())
name_file = f'client_log_{today}.log'

logger = logging.getLogger('client-log')
logger.setLevel(logging.INFO)

file_path = os.path.join(folder, name_file)

fh = logging.FileHandler(file_path, encoding='utf-8')
fh.setLevel(logging.INFO)
_format = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")
fh.setFormatter(_format)
logger.addHandler(fh)
