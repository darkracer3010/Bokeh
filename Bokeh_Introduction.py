# Importing the library
from bokeh.plotting import figure, show
# Giving points for X-axis and Y-axis respectively
X=[1,2,3,4,5]
Y=[6,7,8,9,10]
# Giving labels to the graph
plot= figure(title="Line Graph", x_axis_label='x', y_axis_label='y')
# Plotting the graph and giving name and thickness to the line
plot.line(X, Y, legend_label="Income", line_width=5)
# for displaying the graph
show(plot)
