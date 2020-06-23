# Encephalo Investments Coding Pre-Test - Revised April 2020

import pandas as pd
import numpy as np
import math


def cleanse_data(df):
    # Your task here is to remove data from any ticker that isn't XXY, sort chronologically and return a dataframe
    # whose only column is 'Adj Close'
    dfclean = df
    return dfclean


def mc_sim(sims, days, df):
    # The code for a crude monte carlo simulation is given below. Your job is to extract the mean expected price
    # on the last day, as well as the 95% confidence interval.
    # Note that the z-score for a 95% confidence interval is 1.960
    returns = df.pct_change()
    last_price = df.iloc[-1]

    simulation_df = pd.DataFrame()

    for x in range(sims):
        count = 0
        daily_vol = returns.std()

        price_series = []

        price = last_price * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)

        for y in range(days):
            price = price_series[count] * (1 + np.random.normal(0, daily_vol))
            price_series.append(price)
            count += 1

        simulation_df[x] = price_series

    # FILL OUT THE REST OF THE CODE. The above code has given you 'sims' of simulations run 'days' days into the future.
    # Your task is to return the expected price on the last day +/- the 95% confidence interval.
    std = np.std(price_series)
    mean = np.mean(price_series)
    upper = mean + 1.96 * std / np.sqrt(days)
    lower = mean - 1.96 * std / np.sqrt(days)
    # :return: a tuple: (lower_bound, upper_bound)
    return lower, upper


def main():
    filename = '20192020histdata.csv'
    rawdata = pd.read_csv(filename)
    cleansed = cleanse_data(rawdata)
    simnum = 2500  # Somewhere between 2000-3000 simulations so that we got a tight and accurate range
    days = 25
    print(f'We are 95% confident that XXY price is between: {mc_sim(simnum, days, cleansed)}')
    
    'PART 3: The expected value of stock XXY is 154 +- 3'
    

if __name__ == '__main__':
    main()
