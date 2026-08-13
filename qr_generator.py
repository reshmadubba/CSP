import qrcode

# Main website URL
website_url = "https://reshmadubba.github.io/CSP/"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(website_url)
qr.make(fit=True)

# Generate image
img = qr.make_image()

# Save QR code
img.save("qr_local_info.png")

print("QR code generated successfully!")
print("Website:", website_url)
print("Saved as: qr_local_info.png")
