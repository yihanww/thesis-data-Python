import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_gender_demo(df, col):
    """
    Plot gender demographics from a DataFrame.

    Parameters:
    - df: DataFrame containing demographic data.
    - col: Column name for gender in the DataFrame.

    The function creates a bar plot showing the count of each gender category.
    """
    # Set the aesthetic style of the plots
    sns.set_style("whitegrid")

    # Create the bar plot
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(x=col, data=df, palette={'Female': 'blue', 'Male': 'red', 'Prefer not to say': 'black'})

    # Add text labels above the bars
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width() / 2., p.get_height(), '%d' % int(p.get_height()), 
                fontsize=12, ha='center', va='bottom')

    # Set plot labels and title
    ax.set_title('Participants Demographics-Gender')
    ax.set_xlabel('Sex')
    ax.set_ylabel('Number of Participants')

    # Show the plot
    plt.show()


def plot_gender_race_demo(df, col1, col2):
    """
    Plot gender and race demographics from a DataFrame.

    Parameters:
    - df: DataFrame containing demographic data.
    - col1: Column name for gender in the DataFrame.
    - col2: Column name for race in the DataFrame.

    The function creates a stacked bar plot showing the count of each race category within each gender category.
    """
    # Set the aesthetic style of the plots
    sns.set_style("whitegrid")

    # Create the stacked bar plot
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(x=col1, hue=col2, data=df, 
                       palette={'White': 'blue', 'East Asian': 'yellow', 'Black/African American': 'red'})

    # Add text labels for each bar
    for p in ax.patches:
        height = p.get_height()  # Get the height of each bar
        if not np.isnan(height) and height > 0:  
            ax.text(p.get_x() + p.get_width() / 2., p.get_y() + height / 2, '%d' % int(height), 
                    fontsize=10, ha='center', va='center', color='black')

    # Set plot labels and title
    ax.set_title('Participants Demographics-Gender and Race')
    ax.set_xlabel('Sex')
    ax.set_ylabel('Number of Participants')
    ax.legend(title='Race')

    # Show the plot
    plt.show()

