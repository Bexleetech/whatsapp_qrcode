import qrcode
phone_number = "+25678018329"
link =f"https://wa.me/+256780168329"
qr =qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)
img =qr.make_image(fillcolor="black",
backcolor="white")
img.save("whatsapp_qr.png")
print("success!!!!!!")