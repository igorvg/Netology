import requests


class Yandex:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content_Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def get_upload_link(self, disk_file_path: str):
        ya_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Content_Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {'path': disk_file_path}
        folder = requests.put(url=ya_url, headers=headers, params=params)
        return folder.status_code

    def upload_file_to_disk(self, disk_file_path, file_name, file_link):
        ya_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {
            'path': f'{disk_file_path}/{file_name}',
            'url': file_link,
            'overwrite': 'false'
        }
        response = requests.post(url=ya_url, headers=headers, params=params)
        return response.status_code
