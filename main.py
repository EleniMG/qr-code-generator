import qrcode

def get_qr_info():
    print("Enter QR code file name:")
    file_name = input()
    print("Enter QR code data:")
    qr_data = input()
    return {"file_name": file_name, "qr_data": qr_data}

def create_qr_code(qr_data):
    img = qrcode.make(qr_data)
    type(img)
    img.save("test_file.png")

if __name__ == "__main__":
    qr_data = get_qr_info()
    create_qr_code(qr_data=qr_data)
