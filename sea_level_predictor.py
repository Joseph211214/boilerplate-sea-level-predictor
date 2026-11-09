import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    ajuste_total = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    anios_total = pd.Series(range(1880, 2051))
    ax.plot(
        anios_total,
        ajuste_total.intercept + ajuste_total.slope * anios_total,
        'r'
    )

    # Create second line of best fit
    df_reciente = df[df['Year'] >= 2000]
    ajuste_reciente = linregress(df_reciente['Year'], df_reciente['CSIRO Adjusted Sea Level'])
    anios_reciente = pd.Series(range(2000, 2051))
    ax.plot(
        anios_reciente,
        ajuste_reciente.intercept + ajuste_reciente.slope * anios_reciente,
        'green'
    )

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()