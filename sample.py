# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

# pip install requests
# please get these values from http://open.youtu.qq.com
appid = 'xxxxx'
secret_id = 'xxxxx'
secret_key = 'xxxx'
userid = 'xxxxx'

#choose a end_point
#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT
#end_point = TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT 
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
session_id = "xxxxx"


#for TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT end_point
#get four-character idioms
#retlivegetfour = youtu.livegetfour(session_id)
#print retlivegetfour

#four-character live detect without face compare
#retlivedetectfour = youtu.livedetectfour('1122', 'xxx.mp4', session_id)
#print retlivedetectfour

#four-character live detect with face compare
#retlivedetectfour= youtu.livedetectfour('1122',  'xxx.mp4',  session_id,   'xxx.jpg', True)
#print retlivedetectfour

#four-character idcard live detect
#retidcardlivedetectfour = youtu.idcardlivedetectfour('123456789987654321',  '张三',  '1122', 'xxx.mp4', session_id )
#print retidcardlivedetectfour

#idcard face compare: use local image compare with id card image 
#retidcardfacecompare = youtu.idcardfacecompare('123456789987654321', '张三', 'xxx.jpg', 0, session_id)
#print retidcardfacecompare

#idcard face compare :use url image compare with id card image
#retidcardfacecompare = youtu.idcardfacecompare('123456789987654321', '张三', 'http://xxx.png', 1, session_id)
#print retidcardfacecompare

# face compare : use two local image to compare 
#retfacecompare = youtu.FaceCompare('xxx.jpg', 'xxx.jpg')
#print retfacecompare

# face compare : use two url image to compare 
#retfacecompare = youtu.FaceCompare('http://xxx.png', 'http://xxx.png', 1)
#print retfacecompare

#id card ocr: use local id card image
#retidcardocr = youtu.idcardocr('xxx.jpg', data_type = 0, card_type = 0)
#print retidcardocr

#id card ocr: use url id card image
#retidcardocr = youtu.idcardocr('http://xxx.jpg', data_type = 1, card_type = 0)
#print retidcardocr

#driver license ocr: use local image
#retdriverlicenseocr = youtu.driverlicenseocr('ocr_xsz_01.jpg', data_type = 0, proc_type = 0)
#print retdriverlicenseocr

#business card ocr: use local image
#retbcocr = youtu.bcocr('ocr_card_01.jpg', data_type = 0)
#print retbcocr

#general ocr: use local image
#retgeneralocr = youtu.generalocr('icon_ocr_common01.png', data_type = 0)
#print retgeneralocr

#id card validate: validate the idcard is correct
#retvalidateidcard = youtu.ValidateIdcard('123456789987654321', '张三', session_id)
#print retvalidateidcard
