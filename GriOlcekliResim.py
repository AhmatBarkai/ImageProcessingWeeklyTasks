from PIL import Image


def ChangingTheBit(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    image.show(title=str(pixel_size) + "Bit Image")


def GrayScaleToBit():
    bits = [8, 16, 24]
    # İki değişkeni değiştirip çalıştır
    imgPath = '/Users/ahmat/images/img1.jpeg'
    saveImgPath = '/Users/ahmat/images/img2.jpeg'

    Image.open(imgPath).convert('RGB').convert('L').save(saveImgPath)

    for index in range(3):
        ChangingTheBit(saveImgPath, bits[index])
    image = Image.open(saveImgPath)
    image.show()


GrayScaleToBit()

