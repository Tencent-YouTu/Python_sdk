# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

appid = '1000054'
secret_id = 'AKIDcTZhE4OfhUOgoMzY3PiqHziE5PLziWYR'
secret_key = 'J9I1LNjWdr8TxI2VyWai3ZizTiZ2vZsp'

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key)

#ret = youtu.DetectFace('0.jpg', '3041722595')
#ret = youtu.NewPerson('jxl', '1.jpg', ['albert'])
#faceid = 1027463655356170239
#ret = youtu.FaceVerify('jxl', '0.jpg')
#ret = youtu.DelPerson('jxl')
#ret = youtu.AddFace('jxl',['0.jpg'])
#faceid0 = 1027472526515699711
#ret = youtu.DelFace('jxl', ['1027472526515699711'])
#ret = youtu.SetInfo('jxl', 'jxl', 'tag')
#ret = youtu.GetInfo('jxl')
#ret = youtu.GetGroupIds()
#ret = youtu.GetPersonIds('albert')
#ret = youtu.GetFaceIds('jxl')
#ret = youtu.GetFaceInfo('1027479018812801023')
ret = youtu.FaceCompare('you_path_one.jpg','you_path_two.jpg')
print ret

