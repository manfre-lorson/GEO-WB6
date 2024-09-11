import PIL.Image as pili
import os
from glob import glob


def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'W' or direction == 'S':
        dd *= -1
    return dd

def get_coord(path):
    img = pili.open(path)
    exif = img._getexif()

    lat_dir = exif[34853][1]
    lat_deg, lat_min, lat_sec = exif[34853][2]
    latitude = dms2dd(lat_deg, lat_min, lat_sec, lat_dir)

    lon_dir = exif[34853][3]
    lon_deg, lon_min, lon_sec = exif[34853][4]
    longitude = dms2dd(lon_deg, lon_min, lon_sec, lon_dir)

    return latitude, longitude



folder = ""
outfile = open(folder + os.sep + 'img_coods.csv', 'w')
outfile.write('latitude,longitude,image\n')
files = glob(folder + os.sep + '*.jpg')


for f in files:
    try:
        name = f.split(os.sep)[-1]
        lat, lon = get_coord(f)
        outfile.write(f'{lat},{lon},{name}\n')
    except: pass
outfile.close()

