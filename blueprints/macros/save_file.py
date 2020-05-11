import os
from werkzeug.utils import secure_filename

from data.model_files import File

from blueprints.macros.convert_ru_to_eng import convert_ru_to_eng

PRE_PATH = '/home/SuperCereal/status-false/'
PRE_PATH = ''


def save_file(data, path, **some_id):
    if not os.path.exists(path):
        os.mkdir(path)
    filename = PRE_PATH + secure_filename(convert_ru_to_eng(data.filename))
    data.save(os.path.join(path, filename))
    file = File(
        path=os.path.join(path, filename),
        **some_id
    )
    return file
