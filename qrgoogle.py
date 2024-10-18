# Qr Code
#pip install qrcode
#pip install pillow

import qrcode
qrcode.make("https://www.google.com").save("qr.png")