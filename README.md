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

appid = 'xxx'
secret_id = 'xxxxxxx'
secret_key = 'xxxxxxxx'
userid= 'xxx'

#end_point = TencentYoutuyun.conf.API_TENCENTYUN_END_POINT  // 腾讯云
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT        // 优图开放平台

youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

ret = youtu.FaceCompare('you_path_one.jpg','you_path_two.jpg')
print ret
```

###SDK内部错误码说明
    IMAGE_FILE_NOT_EXISTS  -1     //文件不存在
    IMAGE_NETWORK_ERROR  -2       //网络错误
    IMAGE_PARAMS_ERROR  -3        //图片参数错误
    PERSON_ID_EMPTY  -4           //参数person_id 为空
    GROUP_ID_EMPTY   -5           //参数group_id 为空
    GROUP_IDS_EMPTY  -6           //参数group_ids 为空
    IMAGES_EMPTY     -7           //参数images 集合为空
    FACE_IDS_EMPTY   -8           //参数face_ids 集合为空
    FACE_ID_EMPTY    -9           //参数face_id为空
    LIST_TYPE_INVALID  -10        //不是list类型
    IMAGE_PATH_EMPTY  -11         //传入的image_path为空
    
    OCR_NOT_ENOUGH_TEXTLINES -5201      //名片无足够的文本
    OCR_TEXTLINES_SKEWED     -5202      //名片文本行倾斜角度太大
    OCR_TEXTLINES_FUZZY      -5203      //名片模糊
    OCR_UNRECOG_NAME         -5204      //名片姓名识别失败
    OCR_UNRECOG_TEL           -5205     //名片电话识别失败
    
##初始化
- 示例
- `youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)`

- 参数`ytopen_sdk::AppSign`
	- `appid` 业务中的应用标识AppId
	- `secret_id` 秘钥SecretId
	- `secret_key` 秘钥SecretKey
    - `userid`    用户id
    - `end_point` 服务后台路径，默认是优图开放平台，支持腾讯云
    
##接口说明
接口调用统一返回值说明
- 返回值
	`Json`格式的返回结果，具体字段参考API文档
	
###人脸检测
- 接口
`DetectFace(self, image_path, mode = 0, data_type = 0)`
- 参数
	- `image_path` 待检测的图片路径
	- `mode` 是否大脸模式，默认非大脸模式
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
    
###人脸配准
- 接口
`FaceShape(self, image_path, mode = 0, data_type = 0)`
- 参数
	- `image_path` 待检测的图片路径
	- `mode` 是否大脸模式，默认非大脸模式
    - `data_type` 用于表示image是图片还是url, 0代表图片，1代表url
    
###人脸比对
- 接口
`FaceCompare(self, image_pathA, image_pathB, data_type = 0):`
- 参数
	- `image_pathA` 待比对的A图片路径
	- `image_pathB` 待比对的B图片路径
    - `data_type` 用于表示image_pathA, image_pathB是图片还是url, 0代表图片，1代表url
    
###人脸验证
- 接口
`FaceVerify(self, person_id, image_path, data_type = 0)`
- 参数
	- `person_id` 待验证的个体id
	- `image_path` 待验证的图片路径
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
     
###人脸识别
- 接口
`FaceIdentify(self, group_id, image_path, data_type = 0)`
- 参数
	- `group_id` 识别的组id
	- `image_path` 待识别的图片路径
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
    
###新建个体
- 接口
`NewPerson(self, person_id, image_path, group_ids, person_name= '', tag='', data_type = 0)`
- 参数
	- `person_id` 新建的个体id，用户指定，需要保证app_id下的唯一性
	- `person_name` 个体对应的姓名
	- `group_ids` 数组类型，用户指定（组默认创建）的个体存放的组id，可以指定多个组id
	- `image_path` 包含个体人脸的图片路径
	- `tag` 备注信息，用户自解释字段
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
    
###删除个体
- 接口
`DelPerson(self, person_id)`
- 参数
	- `person_id` 待删除的个体id

###增加人脸
- 接口
`AddFace(self, person_id, images, tag='', data_type = 0)`
- 参数
	- `person_id` 新增人脸的个体身份id
	- `images` 数组类型，待增加的包含人脸的图片路径，可加入多张（包体大小<2m）
	-  `tag` 人脸备注信息，用户自解释字段
    - `data_type` 用于表示images是图片还是url, 0代表图片，1代表url
    
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
	- `tag` 新设置的人脸备注信息，为空无效

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

### 获取人脸列表
- 接口
`GetFaceIds(self, person_id)`
- 参数
	- `person_id` 待查询的个体id

### 获取人脸信息
- 接口
`GetFaceInfo(self, face_id)`
- 参数
	- `face_id` 待查询的人脸id
```
```
### 模糊检测
`fuzzydetect(self, image_path, data_type = 0, seq = '')`
- 参数
    - `image_path` 标识图片信息
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
    
### 美食检测
`fooddetect(self, image_path, data_type = 0, seq = '')`
- 参数
    - `image_path` 标识图片信息
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
    
### 图片分类
`imagetag(self, image_path, data_type = 0, seq = '')`
- 参数
    - `image_path` 标识图片信息
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
    
### 色情图像检测
`imageporn(self, image_path, data_type = 0, seq = '')`
- 参数
    - `image_path` 标识图片信息
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
```
```
### 身份证OCR识别
`idcardocr(self, image_path, data_type = 0, card_type = 1 ,seq = '')`
- 参数
    - `image_path` 标识图片信息
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
    - `card_type` 0 代表输入图像是身份证正面， 1代表输入是身份证反面

### 名片ocr识别
`namecardocr(self, image_path, data_type = 0, retimage= 1, seq = '')`
- 参数
    - `image_path` 标识图片信息
    - `data_type` 用于表示image_path是图片还是url, 0代表图片，1代表url
    - `retimage` 0代表不需要返回识别后图像， 1代表需要返回识别后图像

```
```
更多详情和文档说明参见
[腾讯云智能优图服务](http://www.qcloud.com/product/fr.html)
[腾讯优图开放平台](http://open.youtu.qq.com)
