from matplotlib import pyplot as plt
from matplotlib import dates
from tkinter import messagebox
from pyowm_helper import get_temperature

degree_sign= u'\N{DEGREE SIGN}'

# Create empty window with the given dimensions and labeling
def init_plot():
    plt.figure('PyOWM Weather', figsize=(5,4))
    plt.xlabel('Day')
    plt.ylabel(f'Temperature({degree_sign})C')
    plt.title('Weekly Forecast')

def plot_temperatures(days, temp_min, temp_max):
    #Convert datetime objects to matplotlib date objects
    days = dates.date2num(days)
    #Two bar charts on the same plot with a little offset
    bar_min = plt.bar(days-0.25, temp_min, width=0.5, color='#4286f4')
    bar_max = plt.bar(days+0.25, temp_max, width=0.5, color='#f4b042')
    return (bar_min, bar_max)

def label_xaxis(days):
    #Use datetime objects to use as labels
    plt.xticks(days)
    #Formatting
    axes = plt.gca()
    xaxis_format = dates.DateFormatter('%d/%m')
    axes.xaxis.set_major_formatter(xaxis_format)

def write_temperatures_on_bar_chart(bar_min, bar_max):
    #Adding labels of the value of temperature
    axes = plt.gca()
    y_axis_max = axes.get_ylim()[1]
    label_offset = y_axis_max*0.1
    #Positioning at the top
    for bar_chart in [bar_min, bar_max]:
        for index, bar in enumerate(bar_chart):
            height = bar.get_height()
            xpos = bar.get_x() + bar.get_width()/2.0
            ypos = height-label_offset
            label_text = str(int(height))+degree_sign
            plt.text(xpos, ypos, label_text, horizontalalignment='center', verticalalignment='bottom', color='white')

if __name__ == '__main__':
    init_plot()
    days, temp_min, temp_max = get_temperature()
    bar_min, bar_max = plot_temperatures(days, temp_min, temp_max)
    label_xaxis(days)
    write_temperatures_on_bar_chart(bar_min, bar_max)
    
    plt.show()