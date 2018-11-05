# -*- coding: utf-8 -*-

from qiniu import Auth, put_file, etag, urlsafe_base64_encode, put_data
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = 'vTczFU0ewkDy9nlYN1ikjM0vHD5YI4-3zOLeJQoV'
secret_key = 'JR5zaZygKGvdscCuX_jr22JqaRX8_Pr9nw_4hzqq'

def storage(file_data):
    """上传图片到七牛，file_data是文件的二进制数据"""
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'mihanglaoban'

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    # ret, info = put_file(token, key, localfile)
    ret, info = put_data(token, None, file_data)
    # print(info.status_code)
    # print(type(info.status_code))
    # print(ret)

    if info.status_code == 200:
        #表示上传成功，返回文件名
        print("success")
        return ret.get("key")
    else:
        #表示上传失败
        raise Exception("上传失败")

if __name__ == '__main__':
    with open("/home/tar/Desktop/python_/flask_project_github/info/static/news/images/cat.jpg", "rb") as f:
        file_data = f.read()
        storage(file_data)
