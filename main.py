import time_series_visualizer
import unittest
import test_module

unittest.main(module='test_module', exit=False, verbosity=2)

time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()
