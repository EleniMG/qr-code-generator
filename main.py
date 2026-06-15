import qrcode

def get_qr_data():
    print("Enter QR code data:")
    data = input()
    print(data)

# img = qrcode.make("Test")
# type(img)
# img.save("test_file.png")

if __name__ == "__main__":
    get_qr_data()