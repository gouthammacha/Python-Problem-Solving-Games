import qrcode

# Input data for the QR code
data = input("Enter the text or URL: ").strip()  # Strip whitespace from input
filename = input("Enter the filename (without extension): ").strip()

# Generate the QR code
qr = qrcode.QRCode(box_size=20, border=2)
qr.add_data(data)
qr.make(fit=True)  # Ensure it fits within the QR Code

# Create the image
image = qr.make_image(fill_color="black", back_color="white")

# Save the image as JPEG
filename = f"{filename}.jpeg"
image.save(filename, format="JPEG")

print(f"QR Code Generated and saved as {filename}")
