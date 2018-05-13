from PIL import Image
import numpy as np


# from left to right
def roll_horizontal(image1, image2, num):
    img_list = []
    width, height = max(image1.size, image2.size)
    for p in range(num + 1):
        width_left = round(p / num * width)
        # arr2 = np.asarray(image2, dtype="int32")
        arr1 = np.asarray(image1)  # np.array(image1, copy=False)
        arr2 = np.asarray(image2)  # np.array(image2, copy=False)
        part1 = arr1[:, :width_left, :]
        part2 = arr2[:, width_left:, :]
        # part1 = np.concatenate((part1, part2), axis=1)
        part1 = np.hstack((part1, part2))
        merged_img = Image.fromarray(part1)
        merged_img.show()
        merged_img.save('tmp/%s-%s.jpg' % ('roll', p), 'JPEG')
        img_list.append(merged_img)

    return img_list


def fade(image1, image2, num):
    half = round(num / 2)
    for p1 in range(half):
        alpha = p1 / half * 255
        arr1 = np.array(image1.convert('RGBA'))
        arr1[:, :, 3] = np.multiply(np.ones_like(arr1)[:, :, 0], alpha)
        img = Image.fromarray(arr1)
        # img.show()
        img.save('tmp/%s-%s.jpg' % ('fade', p1), 'PNG')
    for p2 in range(half, num):
        alpha = (p2 / half - 1) * 255
        arr2 = np.array(image2.convert('RGBA'))
        arr2[:, :, 3] = np.multiply(np.ones_like(arr2)[:, :, 0], alpha)
        img = Image.fromarray(arr2)
        # img.show()
        img.save('tmp/%s-%s.jpg' % ('fade', (num + half - p2 - 1)), 'PNG')


if __name__ == '__main__':
    # roll_horizontal(Image.open('img/light.jpg'), Image.open('img/color.jpg'), 10)
    fade(Image.open('img/light.jpg'), Image.open('img/color.jpg'), 10)
