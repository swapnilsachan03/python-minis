""" Simple Version:

import qrcode as qr

img = qr.make("https://www.swapnilsachan.tech")
img.save("swapnil_portfolio.png") """

import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4)

qr.add_data("https://www.swapnilsachan.tech")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_clor="white")
img.save("swapnil_portfolio.png")
