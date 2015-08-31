# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

appid = '105054'
secret_id = 'J9I1LNj5Wdr8TxI2VyWai3Ziz5TiZ2vZsp'
secret_key = 'J9I1LNjWdr8TxI2VyWai3ZizTiZ2vZsp'
userid = '1234567'
#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT 
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT 

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

ret = youtu.FaceCompare('you_path_one.jpg','you_path_two.jpg')
print ret

