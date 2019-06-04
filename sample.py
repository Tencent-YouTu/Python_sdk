# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

# pip install requests
# please get these values from http://open.youtu.qq.com
appid = 'xxxxxx'
secret_id = 'xxxxxx'
secret_key = 'xxxxxx'
userid = 'xxxxxx'

#choose a end_point
#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT
#end_point = TencentYoutuyun.conf.API_YOUTU_VIP_END_POINT 
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
session_id = ""


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
retidcardocr = youtu.idcardocr('./idcard_1.jpg', data_type = 0, card_type = 2)
print retidcardocr

#id card ocr: use url id card image
#retidcardocr = youtu.idcardocr('http://xxx.jpg', data_type = 1, card_type = 0)
#print retidcardocr

#driver license ocr: use local image
#retdriverlicenseocr = youtu.driverlicenseocr('dlocrattach.jpg', data_type = 0, proc_type = 2)
#print retdriverlicenseocr

#business card ocr: use local image
#retbcocr = youtu.bcocr('blocr.jpg', data_type = 0)
#print retbcocr

#general ocr: use local image
#retgeneralocr = youtu.generalocr('ge.jpg', data_type = 0)
#print retgeneralocr

#creditcard ocr: use local image
#retcreditcardocr = youtu.creditcardocr('ccard.jpg', data_type = 0)
#print retcreditcardocr

#bizlicense ocr: use local image
#bizlicenseocr = youtu.bizlicenseocr('bzocr.jpg', data_type = 0)
#print bizlicenseocr

#passport ocr: use local image
#passportocr = youtu.passportocr('passport.jpg', data_type = 0, ocr_template='PassPort')
#print passportocr

#structure ocr: use local image
#structureocr = youtu.structureocr('vat.jpg', data_type = 0, ocr_template='VAT')
#print structureocr

#invoice ocr: use local image
#invoiceocr = youtu.invoiceocr('vat.jpg', data_type = 0, ocr_template='VAT')
#print invoiceocr

#waybill ocr: use local image
#waybillocr = youtu.waybillocr('waybill.jpg', data_type = 0)
#print waybillocr

#hpgeneral ocr: use local image
#hpgeneralocr = youtu.hpgeneralocr('ge.jpg', data_type = 0)
#print hpgeneralocr

#table ocr: use local image
#tableocr = youtu.tableocr('table.png', data_type = 0)
#print tableocr

#arithmetic ocr: use local image
#arithmeticocr = youtu.arithmeticocr('arithmatic.jpg', data_type = 0)
#print arithmeticocr

#finan ocr: use local image
#financocr = youtu.finanocr('jzd.jpg', data_type = 0, ocr_template='BankInSlip')
#print financocr

#vin ocr: use local image
#vinocr = youtu.vinocr('vin.png', data_type = 0)
#print vinocr

#handwriting ocr: use local image
#handwritingocr = youtu.handwritingocr('hw.jpg', data_type = 0)
#print handwritingocr

#eh ocr: use local image
#ehocr = youtu.ehocr('eh.jpg', data_type = 0)
#print ehocr

#id card validate: validate the idcard is correct
#retvalidateidcard = youtu.ValidateIdcard('123456789987654321', '张三', session_id)
#print retvalidateidcard
