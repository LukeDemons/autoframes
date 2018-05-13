from PIL import Image
import numpy as np
import math


def roll_horizontal(image, num):
    width, height = image.size
    arr2 = np.zeros_like(image)
    for p in range(num + 1):
        width_left = round(p / num * width)
        arr1 = np.asarray(image)
        part1 = arr1[:, :width_left, :]
        part2 = arr2[:, width_left:, :]
        # part1 = np.concatenate((part1, part2), axis=1)
        part1 = np.hstack((part1, part2))
        img = Image.fromarray(part1)
        # img.show()
        img.save('tmp/%s-%s.jpg' % ('roll', p), 'JPEG')


def wipe_vertical(image1, num):
    for p in range(num + 1):  # 1-10
        percent1 = p / num
        percent2 = (p + 1) / num
        arr = np.array(image1.convert('RGBA'))
        alpha = arr[:, :, 3]
        n = len(alpha)
        alpha[:] = np.interp(np.arange(n), [0, percent1 * n, percent2 * n, n], [255, 255, 0, 0])[:, np.newaxis]
        img = Image.fromarray(arr, mode='RGBA')
        # img.show()
        img.save('tmp/%s-%s.png' % ('wipe', p), 'PNG')


def fade(image, num):
    for p1 in range(num):
        alpha = p1 / num * 255
        arr1 = np.array(image.convert('RGBA'))
        arr1[:, :, 3] = np.multiply(np.ones_like(arr1)[:, :, 0], alpha)
        img = Image.fromarray(arr1)
        # img.show()
        img.save('tmp/%s-%s.jpg' % ('fade', p1), 'PNG')


def panning(image, step=100):
    arr = np.asarray(image)
    res = np.zeros(arr.shape)
    vector = [[1, 0, 0], [0, 1, 0], [step, 0, 1]]
    for x in range(len(arr)):
        for y in range(len(arr[0, :])):
            point = np.dot(np.array([x, y, 1]), np.array(vector))
            new_x, new_y = point[:2]
            if new_x >= res.shape[0] or new_y >= res.shape[1]:
                continue
            res[point[0], point[1], :] = arr[x, y, :]

    img = Image.fromarray(np.uint8(res))
    img.show()
    img.save('tmp/%s-%s.png' % ('panning', step), 'PNG')


def hole(image, radius=100):
    width, height = image.size
    arr = np.array(image.convert('RGBA'))
    # 考虑使用zip?
    for x in range(len(arr)):
        for y in range(len(arr[0, :])):
            real_x = x - width / 2
            real_y = y - height / 2
            if real_x * real_x + real_y * real_y < radius * radius:
                # 将该坐标的RGB值保持不变，A值置空
                arr[y, x][3] = 0

    img = Image.fromarray(arr, mode='RGBA')
    img.save('tmp/%s-%s.png' % ('hole', radius), 'PNG')


def rotate(image, alpha=math.pi / 6):
    arr = np.asarray(image)
    res = np.zeros(arr.shape)
    vector = [[math.cos(alpha), -math.sin(alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]]
    for x in range(len(arr)):
        for y in range(len(arr[0, :])):
            point = np.dot(np.array([x, y, 1]), np.array(vector))
            new_x, new_y = point[:2]
            new_x = int(np.round(new_x))
            new_y = int(np.round(new_y))
            if new_x >= res.shape[0] or new_y >= res.shape[1]:
                continue
            res[new_x, new_y, :] = arr[x, y, :]

    img = Image.fromarray(np.uint8(res))
    img.show()
    img.save('tmp/%s-%s.jpg' % ('rotate', alpha), 'JPEG')


if __name__ == '__main__':
    # roll_horizontal(Image.open('img/light.jpg'), 10)
    # wipe_vertical(Image.open('img/light.jpg'), 10)
    # fade(Image.open('img/light.jpg'), 10)
    # panning(Image.open('img/light.jpg'))
    # hole(Image.open('img/light.jpg'))  # 还有一小点问题
    rotate(Image.open('img/light.jpg'))  # 还有很大点问题
