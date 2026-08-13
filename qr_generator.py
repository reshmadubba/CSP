import qrcode

# ONE QR CODE FOR THE ENTIRE LOCAL INFORMATION SYSTEM
website_url = "https://reshmadubba.github.io/CSP/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(website_url)
qr.make(fit=True)

img = qr.make_image()

img.save("qr_local_information_system.png")

print("QR code generated successfully!")
print("Website:", website_url)
print("Saved as: qr_local_information_system.png")
