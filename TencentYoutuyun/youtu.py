# -*- coding: utf-8 -*-

import os.path
import time
import requests
import base64
import json
from TencentYoutuyun import conf
from .auth import Auth

class YouTu(object):

    def __init__(self, appid, secret_id, secret_key, userid='0'):
        self.IMAGE_FILE_NOT_EXISTS = -1
        self.IMAGE_NETWORK_ERROR = -2
        self.IMAGE_PARAMS_ERROR = -3
        self.PERSON_ID_EMPTY = -4
        self.GROUP_ID_EMPTY  = -5
        self.GROUP_IDS_EMPTY = -6
        self.IMAGES_EMPTY    = -7
        self.FACE_IDS_EMPTY  = -8
        self.FACE_ID_EMPTY   = -9
        self.LIST_TYPE_INVALID = -10
        
        self.EXPIRED_SECONDS = 2592000
        self._secret_id  = secret_id
        self._secret_key = secret_key
        self._appid      = appid
        self._userid     = userid
        
        conf.set_app_info(appid, secret_id, secret_key)
        
    def FaceCompare(self, imageA, imageB):
        filepathA = os.path.abspath(imageA)
        filepathB = os.path.abspath(imageB)
        if not os.path.exists(filepathA):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', 'session_id':'', 'eye_sim':0, 'mouth_sim':0, 'nose_sim':0, 'eyebrow_sim':0, 'similarity':0}
        if not os.path.exists(filepathB):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', 'session_id':'', 'eye_sim':0, 'mouth_sim':0, 'nose_sim':0, 'eyebrow_sim':0, 'similarity':0}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('facecompare')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "imageA": base64.b64encode(open(filepathA, 'rb').read()).rstrip(),
            "imageB": base64.b64encode(open(filepathB, 'rb').read()).rstrip()
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200:
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':'', 'session_id':'', 'eye_sim':0, 'mouth_sim':0, 'nose_sim':0, 'eyebrow_sim':0, 'similarity':0}
            ret = r.json()
            
        except Exception as e:
            return {'httpcode':0,  'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), 'session_id':'', 'eye_sim':0, 'mouth_sim':0, 'nose_sim':0, 'eyebrow_sim':0, 'similarity':0}
                
        return ret            
    
    def FaceVerify(self, person_id, image):
        filepath = os.path.abspath(image)
        if not os.path.exists(filepath):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "confidence":0, "ismatch":0, "session_id":''}
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY', "confidence":0, "ismatch":0, "session_id":''}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('faceverify')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "person_id": person_id,
            "image": base64.b64encode(open(filepath, 'rb').read()).rstrip()
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200:  
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'', "confidence":0, "ismatch":0, "session_id":''}
            ret = r.json()
            
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "confidence":0, "ismatch":0, "session_id":''}
                
        return ret 
        
    def FaceIdentify(self, group_id, image):
        filepath = os.path.abspath(image)
        if not os.path.exists(filepath):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "session_id":'', "candidates":[{}]}
        
        if len(group_id) == 0:
            return {'httpcode':0, 'errorcode':self.GROUP_ID_EMPTY, 'errormsg':'GROUP_ID_EMPTY', "session_id":'', "candidates":[{}]}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('faceidentify')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "group_id": group_id,
            "image": base64.b64encode(open(filepath, 'rb').read()).rstrip()
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200:  
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'', "session_id":'', "candidates":[{}]}
            ret = r.json()
            
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "session_id":'', "candidates":[{}]}
                
        return ret 
        
    def DetectFace(self, image):
        filepath = os.path.abspath(image)
        if not os.path.exists(filepath):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "session_id":'', "image_id":'', "image_height":0, "image_width":0, "face":[{}]}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('detectface')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "image": base64.b64encode(open(filepath, 'rb').read()).rstrip()
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200: 
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'', "session_id":'', "image_id":'', "image_height":0, "image_width":0, "face":[{}]}
            ret = r.json()
            
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "session_id":'', "image_id":'', "image_height":0, "image_width":0, "face":[{}]}
                
        return ret 
   
    
    def NewPerson(self, person_id, image, group_ids, person_name= '', tag=''):
        filepath = os.path.abspath(image)
        if not os.path.exists(filepath):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
        
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY', "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
        
        if len(group_ids) == 0:
            return {'httpcode':0, 'errorcode':self.GROUP_IDS_EMPTY, 'errormsg':'GROUP_IDS_EMPTY', "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
        
        if type(group_ids) != list:
            return {'httpcode':0, 'errorcode': self.LIST_TYPE_INVALID, 'errormsg':'LIST_TYPE_INVALID', "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
            
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('newperson')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "person_id" : person_id,
            "person_name": person_name,
            "image": base64.b64encode(open(filepath, 'rb').read()).rstrip(),
            "group_ids": group_ids,
            "tag": tag
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200: 
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'', "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
                
            ret = r.json()
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
                       
        return ret 
        
    def DelPerson(self, person_id) :   
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY', "deleted":0, "session_id":''}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('delperson')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "person_id" : person_id 
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200: 
                 return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'', "deleted":0, "session_id":''}
                 
            ret = r.json()
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "deleted":0, "session_id":''}
                 
        return ret 
    
    def AddFace(self, person_id, images, tag=''): 
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY', "face_ids":[], "session_id":'', "added": 0}
        
        if len(images) == 0:
            return {'httpcode':0, 'errorcode':self.IMAGES_EMPTY, 'errormsg':'IMAGES_EMPTY', "face_ids":[], "session_id":'', "added": 0}
        
        if type(images) != list:
            return {'httpcode':0, 'errorcode':self.LIST_TYPE_INVALID, 'errormsg':'LIST_TYPE_INVALID', "face_ids":[], "session_id":'', "added": 0}
            
        images_content = []
        for image in images:
            filepath = os.path.abspath(image)
            if not os.path.exists(filepath):
                return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "face_ids":[], "session_id":'', "added": 0}
            
            images_content.append(base64.b64encode(open(filepath, 'rb').read()).rstrip())
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('addface')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "person_id" : person_id,   
            "images": images_content,
            "tag" : tag,
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200: 
                  return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'', "face_ids":[], "session_id":'', "added": 0}
                  
            ret = r.json()
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "face_ids":[], "session_id":'', "added": 0}
                 
        return ret 
    
    def DelFace(self, person_id, face_ids):
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY',  "session_id":'', "deleted ": 0}
        
        if len(face_ids) == 0:
            return {'httpcode':0, 'errorcode':self.FACE_IDS_IMPTY, 'errormsg':'FACE_IDS_IMPTY',  "session_id":'', "deleted ": 0}
        
        if type(face_ids) != list:
            return {'httpcode':0, 'errorcode':self.LIST_TYPE_INVALID, 'errormsg':'LIST_TYPE_INVALID',  "session_id":'', "deleted ": 0} 
            
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('delface')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "person_id":person_id,
            "face_ids":face_ids
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200: 
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'',  "session_id":'', "deleted ": 0}
                 
            ret = r.json()
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "session_id":'', "deleted ": 0}
                 
        return ret        
    
    
    def SetInfo(self, person_id, person_name='', tag=''):
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY',  "person_id":'', "session_id ": ''}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('setinfo')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "person_id": person_id,
            "person_name": person_name,
            "tag":tag
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200: 
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'',  "person_id":'', "session_id ": ''}
                
            ret = r.json()
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "person_id":'', "session_id ": ''}
                 
        return ret 
        
    def GetInfo(self, person_id):
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY',  "person_id":'', "person_name ": '', "face_ids":[], "tag":'', "secret_id":''}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getinfo')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "person_id": person_id
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200: 
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'',  "person_id":'', "person_name ": '', "face_ids":[], "tag":'', "secret_id":''}
            ret = r.json()
            
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "person_id":'', "person_name ": '', "face_ids":[], "tag":'', "secret_id":''}
                
        return ret 
    
    def GetGroupIds(self):
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getgroupids')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200:
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'',  "group_ids":[]}
                
            ret = r.json()
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "group_ids":[]}
                
        return ret
        
    def GetPersonIds(self, group_id) :
        if len(group_id) == 0:
            return {'httpcode':0, 'errorcode':self.GROUP_ID_EMPTY, 'errormsg':'GROUP_ID_EMPTY', "person_ids":[]}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getpersonids')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "group_id": group_id
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200:
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'', "person_ids":[]}    
                
            ret = r.json()
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "person_ids":[]}
                
        return ret
    
    def GetFaceIds(self, person_id):
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY',  "face_ids":[]}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getfaceids')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "person_id": person_id
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200:
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'',  "face_ids":[]}  
                
            ret = r.json()
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "face_ids":[]}  
                
        return ret    
    
    def GetFaceInfo(self, face_id):
        if len(face_id) == 0:
            return {'httpcode':0, 'errorcode':self.FACE_ID_EMPTY, 'errormsg':'FACE_ID_EMPTY',  "face_info":[]}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getfaceinfo')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "face_id": face_id 
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200:
                 return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'',  "face_info":[]}   
                 
            ret = r.json()
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "face_info":[]}  
                
        return ret 
    
    def FaceShape(self, image):
        filepath = os.path.abspath(image)
        if not os.path.exists(filepath):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "face_shape":[{}], "image_height":0, "image_width":0, "session_id":''}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('faceshape')
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, self._userid)
        sign = auth.app_sign(expired)
        
        headers = {
            'Authorization': sign
        }
        
        data = {
            "app_id": self._appid,
            "image": base64.b64encode(open(filepath, 'rb').read()).rstrip()
        }
        
        r = {}
        try:
            r = requests.post(url, headers=headers, data = json.dumps(data))
            if r.status_code != 200: 
                return {'httpcode':r.status_code, 'errorcode':'', 'errormsg':'', "face_shape":[{}], "image_height":0, "image_width":0, "session_id":''}
  
            ret = r.json()          
        except Exception as e:
            return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "face_shape":[{}], "image_height":0, "image_width":0, "session_id":''}
                
        return ret
        
    def generate_res_url(self, req_type):
        app_info = conf.get_app_info()
        return app_info['end_point'] + str(req_type);
    
   
