# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

appid = 'xxx'
secret_id = 'xxxxx'
secret_key = 'xxxxxxxxx'
userid = '1234567'
#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT 
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT 

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

ret = youtu.FaceCompare('you_path_one.jpg','you_path_two.jpg')
print ret

