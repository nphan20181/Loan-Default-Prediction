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
                legend_texts = legend.get_texts()
                
                n_loans = df_group[variable].sum()
                pct = round(n_loans*100/total, 2)
                legend_texts[0].set_text(variable + ' \n(' + str(n_loans) + ' Loans, ' + str(pct) + '%)')
                
                if c < 1:  # show y-label only for plots in the first column
                    axes[r, c].set_ylabel('Number of Loans')
                else:
                    axes[r, c].set_ylabel('')
    plt.suptitle(p_title, fontsize=14)
    plt.savefig('out/issued_loans_2018')
    plt.show()

def plot_stacked_bar(df_in, title, ylabel='Issued Loans %', fsize=(11, 6), color=['blue', 'orange', 'yellow', 'red']):
    fig, ax = plt.subplots(figsize=fsize)
    
    # plot stacked bar
    df_in.plot.bar(stacked=True, color=color, ax=ax)
    
    # set cell's text for data table
    cell_text = []
    df_index = list(df_in.T.index)
    for index in df_index:
        cell_text.append(list(df_in.T.loc[index]))
    
    # add a data table at the bottom of the axes
    data_table = plt.table(cellText=cell_text,
                      rowLabels=df_index,
                      rowColours=color,
                      colLabels=list(df_in.T.columns),
                      loc='bottom')
    data_table.scale(1, 3)
    
    # format plot
    hide_borders(ax, ['top', 'right'])   # hide top and right borders
    ax.legend(bbox_to_anchor=(1, 0.95), frameon=False, title=gv.VARS_DESC.get('loan_status_flag'))
    ax.set_xlabel('')
    ax.get_xaxis().set_ticks([])
    ax.get_xaxis().set_ticklabels([])
    plt.ylabel(ylabel)
    plt.title('LendingClub\n' + title, fontsize=14)
    plt.show()

def frequency_plot(df_in, list_cols, cols=1, w=8, h=6, hue=True, xlabel=False, title='', orientation='x'):
    rows = int(len(list_cols) / cols)
    fig, axes = plt.subplots(figsize=(w, h), nrows=rows, ncols=cols)
    index = -1
    
    for r in range(rows):
        for c in range(cols):
            if rows > 1 and cols > 1:
                ax = axes[r, c]
            elif rows == 1 and cols == 1:
                ax = axes
            elif rows > 1 and cols == 1:
                ax = axes[r]
            else:
                ax = axes[c]
            
            index += 1
           # if hue == True:
            sns.countplot(x='loan_status_flag', data=df_in, hue=list_cols[index], ax=ax)
            ax.legend(loc='best', title=gv.VARS_DESC.get(list_cols[index]), frameon=False)
           # else:
           #     sns.countplot(x=list_cols[index], data=df_in, ax=ax)
           #     plt.xticks(rotation=90)
            
            if xlabel == False:
                ax.set_xlabel('')
            ax.set_ylabel('')
            ax.get_yaxis().set_ticks([])
            ax.get_yaxis().set_ticklabels([])
            annotate_plot(ax)
            hide_borders(ax, ['top', 'right', 'left'])   # hide top and right borders
    plt.suptitle('LendingClub\n2018 Loan Data\nIssued Loans Frequency Distribution' + title, 
                 fontsize=14)
    plt.subplots_adjust(left=None, bottom=None, right=0.9, top=0.9, wspace=0.2, hspace=0.2)