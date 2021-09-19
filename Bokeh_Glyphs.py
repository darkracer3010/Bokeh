# importing various methods from the packages
from bokeh.plotting import figure,show
# giving inputs for day-1 demand vs price for a product
Demand1=[6,9,3,1]
Price1=[10,5,9,0]
# giving labels to our graph 
plot=figure(x_axis_label='Demand', y_axis_label='Price')
# adding line to the dataset-1
plot.line(Demand1,Price1)
# adding glyphs for dataset-1
plot.square(Demand1,Price1,color='blue')
# giving inputs for day-2 demand vs price for the same product
Demand2=[3,6,7,8]
Price2=[7,3,6,1]
# adding line to the dataset-2
plot.line(Demand2,Price2)
# adding glyphs for dataset-2
plot.circle(Demand2,Price2,color='red')
# giving inputs for day-3 demand vs price for the same product
Demand3=[10,8,9,0]
Price3=[2,20,12,15]
# adding line to the dataset-2
plot.line(Demand3,Price3)
# adding glyphs for dataset-3
plot.x(Demand3,Price3,color='green',size=10)
show(plot)
