import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path)
        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": file_name,
                    "overwrite": "True"},
            headers={"Authorization": f"OAuth {self.token}"},
        )
        href_upload = response.json()['href']
        with open(file_path, 'rb') as f:
            requests.put(href_upload, files={"file": f})
        return print("Файл успешно загружен")


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    uploader.upload(r"c:\my_folder\file.txt")
