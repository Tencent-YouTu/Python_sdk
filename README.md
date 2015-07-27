# TencentYoutuyun-person-face-service
python sdk for [腾讯优图云人脸服务](http://open.youtu.qq.com/)

## 安装
本sdk依赖于Requests包，用户需自己安装

### 下载源码
从github下载源码装入到您的程序中，并加载TencentYoutuyun包


## 人脸对比示例
```python
# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

appid = '105054'
secret_id = 'AKIDc55TZh5E4OfhUOgoMzY3Piq5HziE5PLziWYR'
secret_key = 'J9I1LNj5Wdr8TxI2VyWai3Ziz5TiZ2vZsp'
userid = '1234567'

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid)
ret = youtu.FaceCompare('you_path_one.jpg','you_path_two.jpg')
print ret
```