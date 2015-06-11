# -*- coding: utf-8 -*-

import os.path
import time
import requests
import base64
import json
from TencentYoutuyun import conf
from .auth import Auth

class YouTu(object):

    def __init__(self, appid, secret_id, secret_key):
        self.IMAGE_FILE_NOT_EXISTS = -1
        self.IMAGE_NETWORK_ERROR = -2
        self.IMAGE_PARAMS_ERROR = -3
        self.PERSON_ID_EMPTY = -4
        self.GROUP_ID_EMPTY  = -5
        self.GROUP_IDS_EMPTY = -6
        self.IMAGES_EMPTY    = -7
        self.FACE_IDS_EMPTY  = -8
        self.FACE_ID_ETPTY   = -9
        
        self.EXPIRED_SECONDS = 2592000
        self._secret_id  = secret_id
        self._secret_key = secret_key
        self._appid      = appid

        conf.set_app_info(appid, secret_id, secret_key)
        
    def FaceCompare(self, imageA, imageB, userid = '0'):
        filepathA = os.path.abspath(imageA)
        filepathB = os.path.abspath(imageB)
        if not os.path.exists(filepathA):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', 'session_id':'', 'eye_sim':0, 'mouth_sim':0, 'nose_sim':0, 'eyebrow_sim':0, 'similarity':0}
        if not os.path.exists(filepathB):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', 'session_id':'', 'eye_sim':0, 'mouth_sim':0, 'nose_sim':0, 'eyebrow_sim':0, 'similarity':0}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('facecompare', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), 'session_id':'', 'eye_sim':0, 'mouth_sim':0, 'nose_sim':0, 'eyebrow_sim':0, 'similarity':0}
            else :
                return {'httpcode':0,  'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), 'session_id':'', 'eye_sim':0, 'mouth_sim':0, 'nose_sim':0, 'eyebrow_sim':0, 'similarity':0}
                
        return ret            
    
    def FaceVerify(self, person_id, image, userid = '0'):
        filepath = os.path.abspath(image)
        if not os.path.exists(filepath):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "confidence":0, "ismatch":0, "session_id":''}
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY', "confidence":0, "ismatch":0, "session_id":''}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('faceverify', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "confidence":0, "ismatch":0, "session_id":''}
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "confidence":0, "ismatch":0, "session_id":''}
                
        return ret 
        
    def FaceIdentify(self, group_id, image, userid = '0'):
        filepath = os.path.abspath(image)
        if not os.path.exists(filepath):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "session_id":'', "person_id":'', "face_id":'', "confidence":0}
        
        if len(group_id) == 0:
            return {'httpcode':0, 'errorcode':self.GROUP_ID_EMPTY, 'errormsg':'GROUP_ID_EMPTY', "session_id":'', "person_id":'', "face_id":'', "confidence":0}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('faceidentify', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "session_id":'', "person_id":'', "face_id":'', "confidence":0}
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "session_id":'', "person_id":'', "face_id":'', "confidence":0}
                
        return ret 
        
    def DetectFace(self, image, userid = '0'):
        filepath = os.path.abspath(image)
        if not os.path.exists(filepath):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "session_id":'', "image_id":'', "image_height":0, "image_width":0, "face":[{}]}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('detectface', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "session_id":'', "image_id":'', "image_height":0, "image_width":0, "face":[{}]}
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "session_id":'', "image_id":'', "image_height":0, "image_width":0, "face":[{}]}
                
        return ret 
   
    
    def NewPerson(self, person_id, image, group_ids, person_name= '', tag='', userid = '0'):
        filepath = os.path.abspath(image)
        if not os.path.exists(filepath):
            return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
        
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY', "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
        
        if len(group_ids) == 0:
            return {'httpcode':0, 'errorcode':self.GROUP_IDS_EMPTY, 'errormsg':'GROUP_IDS_EMPTY', "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
           
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('newperson', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "person_id":'', "suc_group":'', "suc_face":0, "session_id":0, "face_id":'', "person_name":''}
                       
        return ret 
        
    def DelPerson(self, person_id, userid = '0') :   
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY', "deleted":0, "session_id":''}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('delperson', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "deleted":0, "session_id":''}
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "deleted":0, "session_id":''}
                 
        return ret 
    
    def AddFace(self, person_id, images, tag='', userid = '0'): 
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY', "face_ids":[], "session_id":'', "added": 0}
        
        if len(images) == 0:
            return {'httpcode':0, 'errorcode':self.IMAGES_EMPTY, 'errormsg':'IMAGES_EMPTY', "face_ids":[], "session_id":'', "added": 0}
        
        images_content = []
        for image in images:
            filepath = os.path.abspath(image)
            if not os.path.exists(filepath):
                return {'httpcode':0, 'errorcode':self.IMAGE_FILE_NOT_EXISTS, 'errormsg':'IMAGE_FILE_NOT_EXISTS', "face_ids":[], "session_id":'', "added": 0}
            
            images_content.append(base64.b64encode(open(filepath, 'rb').read()).rstrip())
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('addface', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "face_ids":[], "session_id":'', "added": 0}
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "face_ids":[], "session_id":'', "added": 0}
                 
        return ret 
    
    def DelFace(self, person_id, face_ids, userid = '0'):
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY',  "session_id":'', "deleted ": 0}
        
        if len(face_ids) == 0:
            return {'httpcode':0, 'errorcode':self.FACE_IDS_IMPTY, 'errormsg':'FACE_IDS_IMPTY',  "session_id":'', "deleted ": 0}
         
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('delface', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "session_id":'', "deleted ": 0}
            else :
                 return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "session_id":'', "deleted ": 0}
                 
        return ret        
    
    
    def SetInfo(self, person_id, person_name='', tag='',userid = '0'):
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY',  "person_id":'', "session_id ": ''}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('setinfo', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "person_id":'', "session_id ": ''}
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "person_id":'', "session_id ": ''}
                 
        return ret 
        
    def GetInfo(self, person_id, userid = '0'):
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY',  "person_id":'', "person_name ": '', "face_ids":[], "tag":'', "secret_id":''}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getinfo', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "person_id":'', "person_name ": '', "face_ids":[], "tag":'', "secret_id":''}
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "person_id":'', "person_name ": '', "face_ids":[], "tag":'', "secret_id":''}
                
        return ret 
    
    def GetGroupIds(self, userid = '0'):
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getgroupids', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "group_ids":[]}
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "group_ids":[]}
                
        return ret
        
    def GetPersonIds(self, group_id, userid = '0') :
        if len(group_id) == 0:
            return {'httpcode':0, 'errorcode':self.GROUP_ID_EMPTY, 'errormsg':'GROUP_ID_EMPTY', "person_ids":[]}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getpersonids', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "person_ids":[]}              
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e), "person_ids":[]}
                
        return ret
    
    def GetFaceIds(self, person_id, userid = '0'):
        if len(person_id) == 0:
            return {'httpcode':0, 'errorcode':self.PERSON_ID_EMPTY, 'errormsg':'PERSON_ID_EMPTY',  "face_ids":[]}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getfaceids', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "face_ids":[]}          
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "face_ids":[]}  
                
        return ret    
    
    def GetFaceInfo(self, face_id, userid = '0'):
        if len(face_id) == 0:
            return {'httpcode':0, 'errorcode':self.FACE_ID_ETPTY, 'errormsg':'FACE_ID_ETPTY',  "face_info":[]}
        
        expired = int(time.time()) + self.EXPIRED_SECONDS
        url = self.generate_res_url('getfaceinfo', userid)
        
        auth = Auth(self._secret_id, self._secret_key, self._appid, userid)
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
            ret = r.json()
        except Exception as e:
            if r :    
                return {'httpcode':r.status_code, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "face_info":[]}         
            else :
                return {'httpcode':0, 'errorcode':self.IMAGE_NETWORK_ERROR, 'errormsg':str(e),  "face_info":[]}  
                
        return ret 
        
    def generate_res_url(self, req_type, userid = '0'):
        app_info = conf.get_app_info()
        return app_info['end_point'] + str(req_type);
    
   
