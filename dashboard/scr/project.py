"""
1- Adquirir a data inicial e final;
2- Adquirir a lista das ações do período;
"""



import pandas as pd
import math


def get_dates(stocks):
    stocks_dates = stocks["datetime"]
    dates = {}

    for date in stocks_dates:
        year = date[:4]
        month = date[5:7]
        day = date[8:]
        if year not in dates.keys():
            dates.update({year: {month: [day]}})
        else:
            if month not in dates[year].keys():
                dates[year].update({month: [day]})
            else:
                if day not in dates[year][month]:
                    dates[year][month].append(day)
                    dates[year][month].sort()

    return dates


def get_user_dates(dates):
    period = []
    for _ in range(2):
        print(list(dates.keys()))
        while True:
            year = input()
            if year in dates.keys():
                break

        print(list(dates[year].keys()))
        while True:
            month = input()
            if month in dates[year].keys():
                break

        print(dates[year][month])
        while True:
            day = input()
            if day in dates[year][month]:
                break

        date = "-".join([year,month,day])
        period.append(date)
    
    return period


def get_stocks_list(stocks, period):
    stock_list = []
    stocks_i = list(stocks[stocks['datetime'] == period[0]]['ticker'])
    stocks_f = list(stocks[stocks['datetime'] == period[1]]['ticker'])
    
    for i in range(len(stocks_i)):
        if stocks_i[i] in stocks_f:
            stock_list.append(stocks_i[i])

    return stock_list


stocks = pd.read_csv(r"C:\Users\guton\Desktop\FEMAT\semestre2\Programação2\trabalho_f\files\b3_stocks_1994_2020.csv")

# dates = get_dates(stocks)
# period = get_user_dates(dates)
period = ['1994-07-04','1995-07-04']
stock_list = get_stocks_list(stocks, period)
print(stock_list)


