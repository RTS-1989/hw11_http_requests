import requests, os, hashlib
import translator


def get_hash_md5(file_path) -> hex:
    hash_object = hashlib.md5(file_path.encode())
    return hash_object.hexdigest()

def get_hash_sha256(file_path) -> hex:
    hash_object = hashlib.sha256(file_path.encode())
    return hash_object.hexdigest()

yd_api_token = 'OAuth AgAAAAAZ3topAAZhgHSSom8Du0bkmVuOANJ8g0I'
YD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

def get_upload_url(file_path):
    
    headers = {
               'Accept': 'application/json',
               'Authorization': yd_api_token
               }

    params = {
             'path': file_path,
             'overwrite': 'True'
             }

    response = requests.get(YD_URL, params=params, headers=headers).json()

    return response['href']

def yd_file_upload(upload_url, file_path):
    
    headers = {
               'Accept': 'application/json',
               'Authorization': yd_api_token,
               'Etag': get_hash_md5(file_path),
               'Sha256': get_hash_sha256(file_path),
               'Transfer - Encoding': 'chunked',
               'Content-Type': 'text/html; charset=utf8'
               }

    params = {
             'path': file_path
             }

    with open(file_path, encoding='utf-8') as upload_file:
        data = upload_file.read().encode('utf-8')
        requests.put(upload_url, data, params=params, headers=headers)

yd_file_upload(get_upload_url('translate.txt'), translator.translate_it('DE.txt', 'translate.txt', 'de', 'ru'))