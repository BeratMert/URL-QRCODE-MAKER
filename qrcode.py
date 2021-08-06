import qrcode

qr = qrcode.QRCode(version=15, box_size=10, border=5)

link = str(input("Link = "))
name = str(input("Name = "))
path = str(input("Path = "))

qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save(f"{path}/{name}.png")