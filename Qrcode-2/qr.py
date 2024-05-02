import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        box_size=8,
        border=3
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red",back_color="white")
    img.save("pars2.png")

generate_qrcode("https://pu.ac.ir")