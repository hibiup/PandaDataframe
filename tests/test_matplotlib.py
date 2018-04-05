from unittest import TestCase

import numpy as np

# run 'yum install python36-tkinter' first
import matplotlib.pyplot as plt

class testMatplotlib(TestCase):
    def test_2d_graphy(self):
        # Compute the x and y coordinates for points on a sine and cosine curve
        x = np.arange(0, 3 * np.pi, 0.1)
        y_sin = np.sin(x)
        y_cos = np.cos(x)

        # Plot the points using matplotlib
        plt.plot(x, y_sin)
        plt.plot(x, y_cos)
        plt.xlabel('x axis label')
        plt.ylabel('y axis label')
        plt.title('Sine and Cosine')
        plt.legend(['Sine', 'Cosine'])

        plt.savefig("/tmp/2d.png", format="png")  # If save(), must called before show()
        plt.show()  # Must call plt.show() to make graphics appear.

    def test_show_picture(self):
        from scipy.misc import imread

        img = imread('tests/data/cat.jpg')

        # Add a sub plot for original image
        # subplot(row, col, index): col >= index%row
        # metrix is '2 x 2', and index is:
        #  [1, 2
        #   3, 4]
        plt.subplot(2, 2, 1)
        plt.imshow(img)

        img_tinted = img * [1, 0.5, 0.5]
        # Add a new sub plot for tinted image
        plt.subplot(2, 2, 4)
        # A slight gotcha with imshow is that it might give strange results
        # if presented with data that is not uint8. To work around this, we
        # explicitly cast the image to uint8 before displaying it.
        plt.imshow(np.uint8(img_tinted))

        plt.show()
    

    def test_vsv_to_figure(self):
        import pandas as pd
        from matplotlib import pyplot

        # Generate figure base on CSV
        df1 = pd.read_csv("tests/data/dashboard_data.csv")
        ax1 = df1.plot(x='fpr', y='tpr')  # set axis

        # Overlap a line
        df2 = pd.DataFrame([[0,0],[1,1]])
        ax2 = df2.plot(ax=ax1)

        fig = ax2.get_figure()
        fig.savefig('/tmp/dashboard.png')
        # Show out
        pyplot.show()
