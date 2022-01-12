import matplotlib.pyplot as plt
import pandas as pd


def plot_stacked_bars(dataframe, title_, size_=(18, 10), rot_=0, legend_="upper right"):
    """
    Plot stacked bars with annotations
    """
    ax = dataframe.plot(
        kind="bar",
        stacked=True,
        figsize=size_,
        rot=rot_,
        title=title_,
    )

    # Annotate bars
    annotate_stacked_bars(ax, textsize=14)
    # Rename legend
    plt.legend(["Retention", "Churn"], loc=legend_)
    # Labels
    plt.ylabel("Company base (%)")
    plt.show()


def annotate_stacked_bars(ax, pad=0.99, colour="white", textsize=13):
    """
    Add value annotations to the bars
    """

    # Iterate over the plotted rectanges/bars
    for p in ax.patches:

        # Calculate annotation
        value = str(round(p.get_height(), 1))
        # If value is 0 do not annotate
        if value == '0.0':
            continue
        ax.annotate(
            value,
            ((p.get_x() + p.get_width()/2)*pad-0.05, (p.get_y()+p.get_height()/2)*pad),
            color=colour,
            size=textsize,
        )


def plot_distribution(dataframe, column, ax, bins_=50):
    """
    Plot variable distirbution in a stacked histogram of churned or retained company
    """
    # Create a temporal dataframe with the data to be plot
    temp = pd.DataFrame(
        {"Retention": dataframe[dataframe["churn"] == 0][column],
         "Churn": dataframe[dataframe["churn"] == 1][column]},
    )
    # Plot the histogram
    temp[["Retention", "Churn"]].plot(kind='hist', bins=bins_, ax=ax, stacked=True)
    # X-axis label
    ax.set_xlabel(column)
    # Change the x-axis to plain style
    ax.ticklabel_format(style='plain', axis='x')


def plot_variable_distribution(dataframe):

    for col in dataframe.columns:
        if col == 'churn':
            continue
        if not pd.api.types.is_numeric_dtype(dataframe[col]):
            continue

        fig, axs = plt.subplots(nrows=1, figsize=(18, 3))
        plot_distribution(dataframe, col, axs)
        plt.show()


def churn_by_category(dataframe, size_=(18, 6), rot_=90, legend_="upper right"):
    """
    Plot stacked bars with annotations
    """

    for col in dataframe.columns:
        if col == 'churn':
            continue
        # for normalize in ['index', False]:
        for normalize in ['index']:
            churn_by_category = pd.crosstab(
                index=dataframe[col],
                columns=dataframe['churn'],
                normalize=normalize
            ).rename(columns={0: 'Retention', 1: 'Churn'})
            ax = churn_by_category.plot(kind="bar", stacked=True, figsize=size_)

            # Annotate bars
            annotate_stacked_bars(ax, textsize=10)
            # Rename legend
            plt.legend(["Retention", "Churn"], loc=legend_)
            # Labels
            plt.ylabel("Company base (%)")
            plt.show()
