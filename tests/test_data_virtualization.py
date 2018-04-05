from unittest import TestCase

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

class testMatplotAnimation(TestCase):
    '''
    * Matplotlib Animation Tutorial: 
      https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
    '''

    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [], lw=2)

    # initialization function: plot the background of each frame
    def init(self):
        self.line.set_data([], [])
        return self.line,

    def animate(self, i):
        ''' animation function.  This is called sequentially '''
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        self.line.set_data(x, y)
        return self.line,

    def test_animation(self):
        # call the animator.  blit=True means only re-draw the parts that have changed.
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init,
                                    frames=200, interval=20, blit=True)

        # save the animation as an mp4.  This requires ffmpeg or mencoder to be
        # installed.  The extra_args ensure that the x264 codec is used, so that
        # the video can be embedded in html5.  You may need to adjust this for
        # your system: for more information, see
        # http://matplotlib.sourceforge.net/api/animation_api.html
        anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

        plt.show()

