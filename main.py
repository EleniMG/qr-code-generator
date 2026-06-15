import qrcode

def get_qr_info():
    print("Enter QR code file name:")
    file_name = input()
    print("Enter QR code data:")
    qr_data = input()
    return {"file_name": file_name, "qr_data": qr_data}

def create_qr_code(file_name, qr_data):
    img = qrcode.make(qr_data)
    type(img)
    img.save(f"{file_name}.png")

if __name__ == "__main__":
    file_name = get_qr_info()["file_name"]
    qr_data = get_qr_info()["qr_data"]
    create_qr_code(file_name=file_name, qr_data=qr_data)
