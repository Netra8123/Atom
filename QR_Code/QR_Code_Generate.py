import qrcode
import image
Qr=qrcode.QRCode(version=15,box_size=10,border=5)
#version->15means version of the qrcode
#box_size -Size of the box where qr code will be displayed.
#border->it's white part of the image
data='https://github.com/Netra8123/Atom'
Qr.add_data(data)
Qr.make(fit=True)
image=Qr.make_image(fill='black',back_color='white')
image.save('test.jpg')
