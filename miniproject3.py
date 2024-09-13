import qrcode
import image

qr=qrcode.QRCode(

    version=13,
    box_size=10,
    border=3
)

data=(input("enter those data to genrate qr code : "))

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="Orange")
img.save("qrcode.png")