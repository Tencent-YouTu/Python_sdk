# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

appid = '105054'
secret_id = 'J9I1LNj5Wdr8TxI2VyWai3Ziz5TiZ2vZsp'
secret_key = 'J9I1LNjWdr8TxI2VyWai3ZizTiZ2vZsp'

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key)

ret = youtu.FaceCompare('you_path_one.jpg','you_path_two.jpg')
print ret

