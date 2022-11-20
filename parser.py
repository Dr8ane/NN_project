import requests
import os
from bs4 import BeautifulSoup as bs

def get_all_images(url):
    urls = []
    soup = bs(requests.get(url).content, "html.parser")
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue
        urls.append(img_url)
    for a in soup.find_all("a"):
        a_url = a.attrs.get("href")
        if not a_url:
            continue
        urls.append(a_url)
    return urls

def download(img_url, url, pathname):
    'https://' in img_url
    'https://' not in img_url
    '.png' in img_url
    '.png' not in img_url
    '.jpg' in img_url
    '.jpg' not in img_url
    '.PNG' in img_url
    '.PNG' not in img_url
    '.JPG' in img_url
    '.JPG' not in img_url
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    filename = os.path.join(pathname, img_url.split("/")[-1])
    if (((img_url.find('.jpg')!=-1) or (img_url.find('.png')!=-1) or (img_url.find('.JPG')!=-1) or (img_url.find('.PNG')!=-1)) and (img_url.find('https://')==-1)):
        image_bytes = requests.get(f'{url}{img_url}').content
        with open(filename, "wb") as f:
            f.write(image_bytes)
    else:
        print(img_url)

def main(url, url2, path):
    imgs = get_all_images(url2)
    get_all_texts(url2)
    for img in imgs:
       download(img, url, path)

main("https://www.gwd.ru", "https://www.gwd.ru/projects/populyarnye-proekty/proekt-tk-2/", "gwd.ru")
main("https://www.tamak.ru", "https://www.tamak.ru/proektyi/seriya-magdeburg/magdeburg-133/", "tamak.ru")
main("https://www.plans.ru", "https://www.plans.ru/project/4714", "plans.ru")
main("https://www.ytong.ru", "https://www.ytong.ru/koeln_1838.php", "ytong.ru")
