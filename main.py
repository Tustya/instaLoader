import os
import random

from PIL import Image, ImageFilter

path_to_photo = 'Начальные'
path_to_mask = 'текстуры'


def photo_in_gray(image, name):
    gray = image.convert('L')
    gray.save(f'gray/{name}.jpg')
    return gray


def photo_in_blur(gray, name):
    blur_photo = gray.filter(ImageFilter.GaussianBlur(random.choice(range(0, 5))))
    blur_photo.save(f'blur/{name}.jpg')
    return blur_photo


def photo_in_old(img1, name):
    count_texture = len(os.listdir(path_to_mask))
    texture_dir = os.listdir(path_to_mask)
    theta = random.choice([0, 180])

    texture_img = Image.open(path_to_mask + "/" + texture_dir[random.choice(range(count_texture))]) \
        .rotate(angle=theta).resize(img1.size).convert('L')

    mask = Image.new("L", img1.size, random.choice(range(128, 168)))

    old_img = Image.composite(img1, texture_img, mask)
    old_img.save(f'old/{name}.jpg')
    return old_img


if __name__ == '__main__':

    count_photo = len(os.listdir(path_to_photo))
    for i in range(count_photo):
        print(i)
        img_dir = os.listdir(path_to_photo)
        # random_img = random.choice(range(count_photo))
        img = Image.open(path_to_photo + "/" + img_dir[i])
        img_gray = photo_in_gray(img, img_dir[i])
        blur_photo = photo_in_blur(img_gray, img_dir[i])
        old_img = photo_in_old(blur_photo, img_dir[i])


