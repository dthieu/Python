import urllib.request
from clint.textui import progress
import os
import sys
import requests
url = r"https://github.com/lingochamp/FileDownloader/archive/refs/heads/master.zip"
file_path = os.path.join(r"D:\HIEU", url.split(r'/')[-1])

def download(url, filename):
    with open(filename, 'wb') as f:
        try:
            response = requests.get(url, stream=True)
        except ConnectionError as err:
            print("Connection error! Detail: ", err)
            sys.exit()

        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total)
                sys.stdout.write('\r[{}{}] {} %'.format('#' * done, '.' * (50 - done), done * 2))
                sys.stdout.flush()
    sys.stdout.write('\n')

download(url, file_path)

def download_file(url, filename=None):
    """Download the file at url and store it at filename."""
    basename = os.path.basename(filename or url)
    msg = """Downloading {dest} (from {source})""".format(source=url,
                                                          dest=basename)
    #sys.stdout.write(str(colored.blue(msg, bold=True)))
    sys.stdout.write("\n")
    request = requests.get(url, stream=True)
    length = request.headers.get("content-length")
    
    with open(filename or os.path.basename(url), "wb") as downloaded_file:
        chunk_size = 1024
        length = int(length or 0)
        total = length / chunk_size + 1
        for chunk in progress.bar(request.iter_content(chunk_size=chunk_size),
                                  expected_size=total,
                                  label=basename):
            downloaded_file.write(chunk)
            downloaded_file.flush()

    return os.path.join(os.getcwd(), downloaded_file.name)

download_file(url, file_path)
# master.zip[################################] 32787/32787 - 00:00:05



# r = requests.get(url, stream=True)

# path = '/some/path/for/file.txt'
# with open(path, 'wb') as f:
#     total_length = int(r.headers.get('content-length'))
#     for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
#         if chunk:
#             f.write(chunk)
#             f.flush()



class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

def download(url: str, fname: str):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    # Can also replace 'file' with a io.BytesIO object
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

#download(url, os.path.join(r"D:", url.split(r'/')[-1]))
