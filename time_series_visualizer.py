import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv'  , parse_dates=['date'], index_col=['date'] )

# Clean data
df =  df.loc[(df["value"] >= df["value"].quantile(0.025))& (df["value"] <= df["value"].quantile(0.975))]
 

def draw_line_plot():
    # Draw line plot
    dates = pd.to_datetime(df.index)
    fig , ax = plt.subplots()
    ax = sns.lineplot(data=df, x="date", y="value")

    ax.set(
        xlabel="Date",
        ylabel="Page Views",
    )

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df['Date']= df.index.month
    df['Years'] =df.index.year
    df['Months'] = df.index.month_name()
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([ 'Date' ,'Years' , 'Months'  ])['value'].agg(['mean']).reset_index()
    # Draw bar plot
    fig, ax = plt.subplots()
    ax = sns.barplot(x="Years", y="mean", hue= 'Months' , data=df_bar )
    ax.set(
        xlabel="Years",
        ylabel="Average Page Views",
        title ='Months'
    )





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
