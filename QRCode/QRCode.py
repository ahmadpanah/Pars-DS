import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        box_size = 10,
        border = 2
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="blue" , back_color="yellow")
    img.save("qr_code.png")

url = input("Please Enter URL: ")
generate_qrcode(url)

