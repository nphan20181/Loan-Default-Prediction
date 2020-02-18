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

def plot_timeseries(df_group, p_title, rows=2, cols=2):
    fig, axes = plt.subplots(figsize=(20, 10), nrows=rows, ncols=cols)
    list_of_cols = list(df_group.columns)
    total = df_group.sum(axis=0).sum()    # total number of loans in the dataset
    
    X = list(df_group.index)
    for r in range(rows):
        for c in range(cols):
            if len(list_of_cols) > 0:
                variable = list_of_cols.pop()
                temp_df = df_group[variable]
                color = gv.STATUS_FLAG_COLORS.get(variable)
                
                axes[r, c].plot(list(temp_df), '-', c=color, label=variable)
                axes[r, c].scatter(X, temp_df, c=color, label=None)
                
                hide_borders(axes[r, c], ['top', 'right'])   # hide top and right borders
                legend = axes[r, c].legend(loc='best', frameon=False)
                
                if c < 1:  # show y-label only for plots in the first column
                    if r == 0:
                        axes[r, c].set_ylabel('Number of Loans', fontsize=14)
                    else:
                        axes[r, c].set_ylabel('Loan Percentage', fontsize=14)
                else:
                    axes[r, c].set_ylabel('')
    plt.suptitle(p_title, fontsize=16)
    plt.show()