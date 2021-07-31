import qrcode
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=4,
)
qr.add_data('maxpython')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
# save img to a file
img.save("testfile.png")