# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

# please get such values from http://open.youtu.qq.com
appid = 'x'
secret_id = 'x'
secret_key = 'x'
userid = 'x'
#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT 
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT 

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

#print  youtu.FaceCompare('you_path_one.jpg','you_path_two.jpg')

#print youtu.imageporn("./a.jpg")
#print youtu.idcardocr("./a.jpg", 1)
#print youtu.namecardocr("./a.jpg", 0, 0,)
