# tencentyun-youtu-python

python sdk for [腾讯云智能优图服务](http://www.qcloud.com/product/fr.html) & [腾讯优图开放平台](http://open.youtu.qq.com)

## 安装

####依赖项
```
- Requests，获取更新版本
	http://docs.python-requests.org/en/latest/
```
####构建工程
```
1. 下载sdk到您的目录${python_sdk}
	git clone https://github.com/TencentYouTu/python_sdk.git
2. 在您需要使用sdk的文件中import TencentYoutuyun包
```

## 名词

- `AppId` 平台添加应用后分配的AppId
- `SecretId` 平台添加应用后分配的SecretId
- `SecretKey` 平台添加应用后分配的SecretKey
- `签名` 接口鉴权凭证，由AppId、SecretId、SecretKey等生成，详见<http://open.youtu.qq.com/welcome/authentication>


## 使用示例
```
# -*- coding: utf-8 -*-

import time
import TencentYoutuyun

appid = '105054'
secret_id = 'J9I1LNj5Wdr8TxI2VyWai3Ziz5TiZ2vZsp'
secret_key = 'J9I1LNjWdr8TxI2VyWai3ZizTiZ2vZsp'

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key)

ret = youtu.FaceCompare('you_path_one.jpg','you_path_two.jpg')
print ret
```

##初始化
- 示例
- `youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key)`

- 参数`ytopen_sdk::AppSign`
	- `appid` 业务中的应用标识AppId
	- `secret_id` 秘钥SecretId
	- `secret_key` 秘钥SecretKey

##接口说明
接口调用统一返回值说明
- 返回值
	`Json`格式的返回结果，具体字段参考API文档
	
###人脸检测
- 接口
`DetectFace(self, image, mode = 0)`
- 参数
	- `image` 待检测的图片路径
	- `mode` 是否大脸模式，默认非大脸模式

###人脸比对
- 接口
`FaceCompare(self, imageA, imageB):`
- 参数
	- `imageA` 待比对的A图片路径
	- `imageB` 待比对的B图片路径

###人脸验证
- 接口
`FaceVerify(self, person_id, image)`
- 参数
	- `person_id` 待验证的人脸id
	- `image` 待验证的图片路径

###人脸识别
- 接口
`FaceIdentify(self, group_id, image)`
- 参数
	- `group_id` 识别的组id
	- `image` 待识别的图片路径

###新建个体
- 接口
        `NewPerson(self, person_id, image, group_ids, person_name= '', tag='')`
- 参数
	- `person_id` 新建的个体id，用户指定，需要保证app_id下的唯一性
	- `person_name` 待验证的图片数据
	- `group_ids` 数组类型，用户指定（组默认创建）的个体存放的组id，可以指定多个组id
	- `image` 包含个体人脸的图片路径
	- `tag` 备注信息，用户自解释字段

###删除个体
- 接口
`DelPerson(self, person_id)`
- 参数
	- `person_id` 待删除的个体id

###增加人脸
- 接口
`AddFace(self, person_id, images, tag='')`
- 参数
	- `person_id` 新增人脸的个体身份id
	- `images` 数组类型，待增加的包含人脸的图片路径，可加入多张（包体大小<2m）
	-  `tag` 人脸备注信息，用户自解释字段

###删除人脸
- 接口
`DelFace(self, person_id, face_ids)`
- 参数
	- `person_id` 待删除人脸的个体身份id
	- `face_ids` 数组类型，待删除的人脸id

###获取信息
- 接口
`GetInfo(self, person_id)`
- 参数
	- `person_id` 待查询的个体身份id

###设置信息
- 接口
`SetInfo(self, person_id, person_name='', tag='')`
- 参数
	- `person_id` 待设置的个体身份id
	- `person_name` 新设置的个体名字，为空无效
	-  `tag` 新设置的人脸备注信息，为空无效

###获取组列表
- 接口
`GetGroupIds(self)`
- 参数
	- 无

###获取个体列表
- 接口
`GetPersonIds(self, group_id)`
- 参数
	- `group_id` 待查询的组id

###获取人脸列表
- 接口
`GetFaceIds(self, person_id)`
- 参数
	- `person_id` 待查询的个体id

###获取人脸信息
- 接口
`GetFaceInfo(self, face_id)`
- 参数
	- `face_id` 待查询的人脸id

```
```
更多详情和文档说明参见
[腾讯云智能优图服务](http://www.qcloud.com/product/fr.html)
[腾讯优图开放平台](http://open.youtu.qq.com)