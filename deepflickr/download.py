import flickrapi
import urllib.request
import os
import time
from keys import api_key, api_secret


flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

def make_download_dir(search_text):
    dir_name = search_text.replace(" ","_")
    dir_path = "/Users/manas/gdrive/work/project/foodnet/data/train/" + \
                dir_name

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path


def download_flickr_images_by_searchtext(search_text, n):

    # search_text = "mashed potatoes and gravy"
    download_dir = make_download_dir(search_text)
    return_json = flickr.photos.search(text=search_text, per_page=n)
    photos = return_json['photos']['photo']

    for i, pic in enumerate(photos):
        pid = pic['id']
        farm = pic['farm']
        server = pic['server']
        secret = pic['secret']
        size = 'm'

        img_url = "https://farm" + str(farm) + ".staticflickr.com/" + \
            str(server) + "/" + str(pid) + "_" + str(secret) + "_" + \
            size + ".jpg"
        print(i, img_url)

        img_name = download_dir + "/img-" + str(pid) + ".jpg"
        urllib.request.urlretrieve(img_url, img_name)
        time.sleep(0.2)


if __name__ == '__main__':
    download_flickr_images_by_searchtext("mashed potatoes and gravy", 1000)
