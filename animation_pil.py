from PIL import Image


# from left to right
def roll_horizontal(image1, image2, num):
    img_list = []
    width, height = max(image1.size, image2.size)
    for p in range(num):
        width_left = round(p / (num-1) * width)
        part2 = image2.crop((0, 0, width_left, height))
        image1.paste(part2)
        # image1.show()
        image1.save('tmp/%s-%s.jpg' % ('roll', p), 'JPEG')
        img_list.append(image1)

    return img_list


def fade(image1, image2, num):
    maxsize = max(image1.size, image2.size)
    half = round(num / 2)
    image1 = image1.convert('RGBA')
    image2 = image2.convert('RGBA')
    img_blender = Image.new('RGBA', maxsize, (0, 0, 0, 0))
    for p1 in range(half):
        factor = p1 / half
        print(factor)
        image1 = Image.blend(image1, img_blender, factor)
        image1.save('tmp/%s-%s.jpg' % ('fade', p1), 'PNG')
    for p2 in range(half, num):
        factor = p2 / half - 1
        print(factor)
        image2 = Image.blend(image2, img_blender, factor)
        image2.save('tmp/%s-%s.jpg' % ('fade', p2), 'PNG')


def rotate_right(image1, image2, num):
    width, height = image1.size
    for angle in range(0, num, 5):
        print(angle)
        res1 = image1.rotate(angle, center=(width, height))
        res2 = image2.rotate(angle, center=(width, 0))
        res1.save('tmp/%s-%s-1.jpg' % ('rotate', angle), 'JPEG')
        res2.save('tmp/%s-%s-2.jpg' % ('rotate', angle), 'JPEG')
        res1.show()


if __name__ == '__main__':
    roll_horizontal(Image.open('img/light.jpg'), Image.open('img/color.jpg'), 10)
    # fade(Image.open('img/light.jpg'), Image.open('img/color.jpg'), 10)
    # rotate_right(Image.open('img/light.jpg'), Image.open('img/color.jpg'), 30)
