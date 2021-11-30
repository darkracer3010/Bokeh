# from bokeh.io import show
# from bokeh.models import CheckboxButtonGroup, CustomJS

# LABELS = ["Welcome", "to", "cppsecrets"]

# checkbox_button_group = CheckboxButtonGroup(labels=LABELS, active=[0])
# checkbox_button_group.js_on_click(CustomJS(code="""
#     console.log('checkbox_button_group: active=' + this.active, this.toString())
# """))

# show(checkbox_button_group)
# from bokeh.io import show
# from bokeh.models import Button, CustomJS

# button = Button(label="Click Me", button_type="success")
# button.js_on_click(CustomJS(code="alert('ok')"))

# show(button)
import numpy as np
from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColorPicker
from bokeh.plotting import Figure
# Creating a Sin graph
n = 200
X = np.linspace(0, 4*np.pi, n)
Y = np.sin(X)
plot = Figure(x_range=(0, 1), y_range=(0, 1), width=350, height=350)
p = plot.line(x=X, y=Y, color="black", line_width=4)
picker = ColorPicker(title="Line Color")
picker.js_link('color', p.glyph, 'line_color')
# display plot
show(column(plot, picker))