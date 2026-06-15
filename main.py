import qrcode

img = qrcode.make("Test")
type(img)
img.save("test_file.png")