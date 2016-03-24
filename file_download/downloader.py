import requests


class FileDownloader:
    def __init__(self):
        pass

    """
    Method copied straight from here
        http://stackoverflow.com/a/16696317
    """
    @staticmethod
    def download_file(local_filename, url):
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)