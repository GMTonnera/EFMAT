import utils
import plotly.graph_objects as go
import math



class Carteira:
    def __init__(self, dataframe, ipca, period) -> None:
        self.df = dataframe
        self.ipca = ipca
        self.start_dates = {}
        self.end_dates = {}
        self.start_date = {}
        self.end_date = {}
        # self.stocks = {"ticker1": [amount, dataframe, candlestick, volatility_graph, volatility, return, price_variation, rentability]}
        self.stocks = {}
        self.min_period = period
        self.wallet_info = {"Return": 0, "Rentability":0, "Volatility": 0, "Period": 0, "Amount": 0}

        self.make_start_dates()


    def make_start_dates(self):
        stocks_dates = self.df["datetime"]

        for date in stocks_dates:
            year = date[:4]
            month = date[5:7]
            day = date[8:]
            if year not in self.start_dates.keys():
                self.start_dates.update({year: {month: [day]}})
            else:
                if month not in self.start_dates[year].keys():
                    self.start_dates[year].update({month: [day]})
                else:
                    if day not in self.start_dates[year][month]:
                        self.start_dates[year][month].append(day)
                        self.start_dates[year][month].sort()


    def make_end_dates(self):
        stocks_dates = self.df["datetime"]
        new_date = utils.calculte_date("-".join(list(self.start_date.values())), self.min_period)
        new_date = utils.find_date(self, new_date)
        for date in stocks_dates:
            if int(date[:4]) < int(new_date[:4]):
                continue

            elif int(date[:4]) == int(new_date[:4]):
                if int(date[5:7]) < int(new_date[5:7]):
                    continue

                elif int(date[5:7]) == int(new_date[5:7]):
                    if int(date[8:]) < int(new_date[8:]):
                        continue
            year = date[:4]
            month = date[5:7]
            day = date[8:]
            if year not in self.end_dates.keys():
                self.end_dates.update({year: {month: [day]}})
            else:
                if month not in self.end_dates[year].keys():
                    self.end_dates[year].update({month: [day]})
                else:
                    if day not in self.end_dates[year][month]:
                        self.end_dates[year][month].append(day)
                        self.end_dates[year][month].sort()


    def set_start_year(self, year):
        self.start_date['year'] = year


    def set_start_month(self, month):
        self.start_date['month'] = month


    def set_start_day(self, day):
        self.start_date['day'] = day

    
    def set_end_year(self, year):
        self.end_date['year'] = year


    def set_end_month(self, month):
        self.end_date['month'] = month


    def set_end_day(self, day):
        self.end_date['day'] = day


    def get_start_years(self):
        return list(self.start_dates.keys())

    
    def get_start_months(self, year):
        return list(self.start_dates[year].keys())
    

    def get_start_days(self, year, month):
        return self.start_dates[year][month]


    def get_end_years(self):
        return list(self.end_dates.keys())

    
    def get_end_months(self, year):
        return list(self.end_dates[year].keys())
    

    def get_end_days(self, year, month):
        return self.end_dates[year][month]


    def get_tickers_list(self):
        stock_list = []
        stocks_i = list(self.df[self.df['datetime'] == "-".join(list(self.start_date.values()))]['ticker'])
        stocks_f = list(self.df[self.df['datetime'] == "-".join(list(self.end_date.values()))]['ticker'])
        
        for i in range(len(stocks_i)):
            if stocks_i[i] in stocks_f:
                stock_list.append(stocks_i[i])

        return stock_list


    def get_start_date(self):
        return f"{self.start_date['year']}-{self.start_date['month']}-{self.start_date['day']}"


    def get_end_date(self):
        return f"{self.end_date['year']}-{self.end_date['month']}-{self.end_date['day']}"


    def check_date(self, date):
        if date in list(self.df['datetime']):
            return True
        
        return False

    
    def set_stocks(self, stocks):
        c1 = self.df['datetime'] == self.get_start_date()
        index1 = c1.index
        c1_index = index1[c1]
        index_start = c1_index.tolist()[0]
        c2 = self.df['datetime'] == self.get_end_date()
        index2 = c2.index
        c2_index = index2[c2]
        index_end = c2_index.tolist()[-1]
        df = self.df.loc[index_start:index_end]
        
        for stock in stocks:
            if stock[0] is None or stock[1] is None:
                continue
            self.stocks.update({stock[0]: [stock[1], df[df["ticker"] == stock[0]]]})
        
        self.make_candlesticks()
        self.make_daily_volatility_graphs()
        self.calculate_stocks_return()
        self.calculate_stocks_rentability()

        
    def make_candlesticks(self):
        for ticker in self.stocks.keys():
            df = self.stocks[ticker][1]
            fig = go.Figure(data=[go.Candlestick(
                x=df["datetime"],
                open=df["open"],
                high=df["high"],
                low=df["low"],
                close=df["close"]
                )],
                layout={"title":{"text": "Preço da ação ao longo do período"}})
            self.stocks[ticker].append(fig)


    def get_daily_profitability(self, stock):
        """Retorna a retabilidade diária de uma ação em um período."""
        daily_profitability = []
        
        for i in range(len(stock)): 
            if i != 0:            
                today_price = float(stock.iloc[i,3])
                yesterday_price = float(stock.iloc[i-1,3])
                daily_profitability.append((today_price - yesterday_price) / yesterday_price)
        
        return daily_profitability


    def get_daily_volatility(self, stock):
        """Retorna a volatividade diária de uma ação."""
        daily_volatilities = []
        d_profitability = self.get_daily_profitability(stock)
        d_profitability_avg = sum(d_profitability)/len(d_profitability)

        for i in range(len(d_profitability)):
            daily_volatility = 0
            for x in range(0,i+1):
                daily_volatility += (d_profitability[x]-d_profitability_avg)**2

            daily_volatility = math.sqrt(daily_volatility/(i+1))
            daily_volatilities.append(daily_volatility)

        return daily_volatilities


    def make_daily_volatility_graphs(self):
        avg_volatility = 0
        for ticker in self.stocks.keys():
            df = self.stocks[ticker][1]
            d_volatility = self.get_daily_volatility(df)
            fig = go.Figure(data=[go.Scatter(x=list(df["datetime"]), y=d_volatility)], layout={"title":{"text": "Volatividade diária da ação"}})
            self.stocks[ticker].append(fig)
            self.stocks[ticker].append(d_volatility[-1])
            avg_volatility += d_volatility[-1]

        self.wallet_info["Volatility"] = avg_volatility / len(self.stocks.keys())


    def calculate_stocks_return(self):
        money_i = 0
        total_ret = 0
        for ticker in self.stocks.keys():
            qtd = self.stocks[ticker][0]
            df = self.stocks[ticker][1]
            price_i = float(df[(df["datetime"] == self.get_start_date()) & (df["ticker"] == ticker)]["close"])
            price_f = float(df[(df["datetime"] == self.get_end_date()) & (df["ticker"] == ticker)]["close"])
            ret = price_f * qtd - price_i * qtd
            total_ret += ret
            money_i += price_i
            self.stocks[ticker].append(ret)
            self.stocks[ticker].append(((price_f * qtd - price_i * qtd)/(price_i * qtd))*100)

        self.wallet_info["Return"] = total_ret
        self.wallet_info["Amount"] = price_i


    def calculate_stocks_rentability(self):
        inflation_i = float(self.ipca[self.ipca["data"] == self.get_start_date()[:7]]["indice"])
        inflation_f = float(self.ipca[self.ipca["data"] == self.get_end_date()[:7]]["indice"])
        inflation_var = (inflation_f / inflation_i) % 1
        for ticker in self.stocks.keys():
            price = self.stocks[ticker][-1]
            rentability = (((1+price/100) / (1+inflation_var)) - 1) * 100
            self.stocks[ticker].append(rentability)

        self.wallet_info["Rentability"] = (((1+((self.wallet_info["Return"] - self.wallet_info["Amount"]) / self.wallet_info["Amount"])/100) / (1+inflation_var)) - 1) * 100