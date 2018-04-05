from unittest import TestCase

# To import imread, we need install 'Pillow'
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

class test_scipy(TestCase):
    def test_image(self):
        img = imread('tests/data/cat.jpg')
        print(img.dtype, img.shape)

        # Tinting color by leaveing green and blue with 50% reduced
        img_tinted = img * [1, 0.5, 0.5]
        imsave('/tmp/cat_tinted.jpg', img_tinted)

        # resize image
        img_resized = imresize(img_tinted, (300, 300))
        imsave('/tmp/cat_resized.jpg', img_resized)
