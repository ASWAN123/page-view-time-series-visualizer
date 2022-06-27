import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')
# Clean data
df =  df.loc[(df["value"] >= df["value"].quantile(0.025))& (df["value"] <= df["value"].quantile(0.975))].astype(int)

def draw_line_plot():
    # Draw line plot

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
    df_b = df.copy()
    df_b['Date']= df_b.index.month
    df_b['Years'] =df_b.index.year
    df_b['Months'] = df_b.index.month_name()
    # Copy and modify data for monthly bar plot
    df_bar = df_b.groupby([ 'Date' ,'Years' , 'Months'  ])['value'].agg(['mean']).reset_index()
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
    df_box['month_num'] = [d.month for d in df_box.date]
    df_box.sort_values(['month_num'], inplace=True)
    
    fig, ax = plt.subplots(1,2, figsize=(12,4))
    ax = sns.boxplot(x="year", y="value", data=df_box ,ax=ax[0])
    ax.set(xlabel="Year",ylabel="Page Views",title ='Year-wise Box Plot (Trend)')
    ax = sns.boxplot(x="month", y="value", data=df_box )
    ax.set(xlabel="Month",ylabel="Page Views",title ='Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

