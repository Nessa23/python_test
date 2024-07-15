import unittest
from draw_plots import PlotDrawer

class TestPlotDrawer(unittest.TestCase):
    def setUp(self):
        self.plot_drawer = PlotDrawer('deviation.json')

    def test_draw_plots(self):
        plot_paths = self.plot_drawer.draw_plots()
        self.assertTrue(len(plot_paths) > 0)
        for path in plot_paths:
            self.assertTrue(path.exists())

if __name__ == '__main__':
    unittest.main()

