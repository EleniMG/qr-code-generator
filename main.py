import qrcode

def get_qr_data():
    print("Enter QR code data:")
    qr_data = input()
    return qr_data

def create_qr_code(qr_data):
    # img = qrcode.make("Test")
    # type(img)
    # img.save("test_file.png")

if __name__ == "__main__":
    qr_data = get_qr_data()
    create_qr_code(qr_data=qr_data)
