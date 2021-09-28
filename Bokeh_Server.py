# Import Library
import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure
# Creating a Sin graph
n = 200
X = np.linspace(0, 4*np.pi, n)
Y = np.sin(X)
source = ColumnDataSource(data = dict(x = X, y = Y))
plot = figure(plot_height = 400, plot_width = 400, title = "sine wave")
plot.line('x', 'y', source = source, line_width = 3, line_alpha = 0.6)
# Adding Slider to change Frequency of the graph
frequency = Slider(title = "Frequency", value = 1.0, start = 0.1, end = 5.1, step = 0.1)
# Creating a function for updation
def ud(attrname, old, new):
   k = frequency.value
   x = np.linspace(0, 4*np.pi, n)
   y = 1*np.sin(k*x + 0) + 0
   source.data = dict(x = x, y = y)
frequency.on_change('value', ud)
curdoc().add_root(row(frequency, plot, width = 500))
curdoc().title = "Server Example"
