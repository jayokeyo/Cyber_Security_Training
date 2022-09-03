import pyqrcode
#import sys
from PIL import Image

link = input('Link for which to generate a QR code: ')
QRCode = pyqrcode.create(link)
#QRCode.svg(sys.stdout,scale=1)
#QRCode.svg('masenoschool.svg',scale=4)
pyqrcode.QRCode.png(QRCode,scale=5)
Image.open('QRCode.png')
