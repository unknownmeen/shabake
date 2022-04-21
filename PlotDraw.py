
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure.get_plot(), canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

plot_price = PlotPrice()
window = psg.Window('parin_group', make_and_get_layout(plot_price), resizable=True, force_toplevel=True, finalize=True)
fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, plot_price)