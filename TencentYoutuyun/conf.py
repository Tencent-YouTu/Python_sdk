# -*- coding: utf-8 -*-
import pkg_resources
import platform
API_YOUTU_END_POINT = 'http://api.youtu.qq.com/youtu/api/'
APPID = '105054'
SECRET_ID = 'AKIDc55TZh5E4OfhUOgoMzY3Piq5HziE5PLziWYR'
SECRET_KEY = 'J9I1LNj5Wdr8TxI2VyWai3Ziz5TiZ2vZsp'

_config = {
    'end_point':API_YOUTU_END_POINT,
    'appid':APPID,
    'secret_id':SECRET_ID,
    'secret_key':SECRET_KEY,
}

def get_app_info(cate='image'):
    if 'image' == cate:
        return _config
    else:
        return _config

def set_app_info(appid=None,secret_id=None,secret_key=None):
    if appid:
        _config['appid'] = appid
    if secret_id:
        _config['secret_id'] = secret_id
    if secret_key:
        _config['secret_key'] = secret_key


