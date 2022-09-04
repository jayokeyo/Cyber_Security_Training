''' Given some data the code generates a QR Code
for the data.'''

import pyqrcode

link = input('Link for which to generate a QR code: ')
QRCode = pyqrcode.create(link)
QRCode.svg('QR_Code.svg',scale=4)
