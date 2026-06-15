import qrcode

def get_qr_info():
    file_name = input("Enter QR code file name:")
    qr_data = input("Enter QR code data:")
    print(f"Generating file: {file_name} with {qr_data}")
    return {"file_name": file_name, "qr_data": qr_data}

def create_qr_code(file_name, qr_data):
    img = qrcode.make(qr_data)
    type(img)
    img.save(f"{file_name}.png")

if __name__ == "__main__":
    qr_info = get_qr_info()
    file_name = qr_info["file_name"]
    qr_data = qr_info["qr_data"]
    create_qr_code(file_name=file_name, qr_data=qr_data)
