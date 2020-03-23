import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import modules.global_vars as gv     # load user-defined variables

def hide_borders(ax, borders):
    for b in borders:
        ax.spines[b].set_visible(False)  # hide plot's border

def annotate_plot(ax):
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', 
                    xytext = (0, 10), textcoords = 'offset points')

def annotate_plot2(ax, n=0):
    # annotate bar
    for p in ax.patches:
        # annotate frequency
        if n == 0: h_adj = 1
        else: h_adj = 2
        ax.annotate(format(p.get_height(), '.0f'),
            (p.get_x() + p.get_width() / 2., p.get_height()/h_adj), ha = 'center', va = 'center', 
             xytext = (0, 10), textcoords = 'offset points')
        
        if n > 0:# annotate relative frequency
            ax.annotate(format(p.get_height()*100 / n, '.0f') + '%', 
               (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', 
                xytext = (0, 10), textcoords = 'offset points')  