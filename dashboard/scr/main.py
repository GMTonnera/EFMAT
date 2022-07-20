from dis import dis
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
import pandas as pd
import plotly.graph_objects as go

import utils
import layout
from  carteira import Carteira



stocks = pd.read_csv(r"C:\Users\guton\Desktop\FEMAT\semestre2\Programação2\trabalho_f\files\b3_stocks_1994_2020.csv")
ipca = pd.read_csv(r"C:\Users\guton\Desktop\FEMAT\semestre2\Programação2\trabalho_f\files\ipca.csv")
wallet = Carteira(stocks, ipca, 4)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.layout = html.Div([dcc.Location(id="url"), layout.sidebar, layout.content])


@app.callback([Output("page-content", "children")],
              [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return layout.info_page()
    elif pathname == "/criar":
        return layout.criar_page(utils.make_select_list(wallet.get_start_years()))
    elif pathname == "/analise":
        return layout.review_pag(wallet)
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(Output("download-component", "data"),
              Input("download_dataset", "n_clicks"),
              prevent_initial_call=True)
def download_dataset(n_clicks):
    return dcc.send_file(r"C:\Users\guton\Desktop\FEMAT\semestre2\Programação2\trabalho_f\files\b3_stocks_1994_2020.csv")


@app.callback([Output("start-month-select", "disabled"), Output("start-month-select", "options"), Output("start-month-select", "placeholder")],
              [Input("start-year-select", "value")]
)
def enable_start_month_selection(year):
    if year:
        wallet.set_start_year(year)
        return False, utils.make_select_list(wallet.get_start_months(year)), "Selecione o mês inicial"
    return True, [], ''


@app.callback([Output("start-day-select", "disabled"), Output("start-day-select", "options"), Output("start-day-select", "placeholder")],
              [Input("start-month-select", "value"), Input("start-year-select", "value")]
)
def enable_start_day_selection(month, year):
    if month:
        wallet.set_start_month(month)
        return False, utils.make_select_list(wallet.get_start_days(year, month)), "Selecione o dia inicial"
    return True, [], ''


@app.callback([Output("end-year-select", "disabled"), Output("end-year-select", "options"), Output("end-year-select", "placeholder")],
              [Input("start-day-select", "value")]
)
def enable_end_year_selection(day):
    if day:
        wallet.set_start_day(day)
        wallet.make_end_dates()
        return False, utils.make_select_list(wallet.get_end_years()), "Selecione o ano final"
    
    return True, [], ""


@app.callback([Output("end-month-select", "disabled"), Output("end-month-select", "options"), Output("end-month-select", "placeholder")],
              [Input("end-year-select", "value")]
)
def enable_month_selection(end_year):
    if end_year:
        wallet.set_end_year(end_year)
        return False, utils.make_select_list(wallet.get_end_months(end_year)), "Selecione o mês final"
    
    return True, [], ""


@app.callback([Output("end-day-select", "disabled"), Output("end-day-select", "options"), Output("end-day-select", "placeholder"),],
              [Input("end-year-select", "value"), Input("end-month-select", "value")]
)
def enable_end_day_selection(end_year, end_month):
    if end_month:
        wallet.set_end_month(end_month)
        return False, utils.make_select_list(wallet.get_end_days(end_year, end_month)), "Selecione o dia final"

    return True, [], ""
 

@app.callback(
              [Output("stock1-select", "disabled"), Output("stock1-select", "placeholder"), Output("stock1-select", "options"),
               Output("stock1-qtd-input", "disabled"), Output("stock1-qtd-input", "placeholder")],
              [Input("end-day-select", "value")]
)
def enable_stock1(end_day):
    if end_day:
        wallet.set_end_day(end_day)
        return False, "Selecione uma ação", utils.make_select_list(wallet.get_tickers_list()), False, "Digite a quantidade de ações"

    return True, "", [], True, ""


@app.callback(
    [Output("stock2-select", "disabled"), Output("stock2-select", "placeholder"), Output("stock2-select", "options"),
     Output("stock2-qtd-input", "disabled"), Output("stock2-qtd-input", "placeholder")],
    [Input("stock1-select", "value"), Input("stock1-qtd-input", "value")]
)
def enable_stock2(ticker1, qtd1):
    if ticker1 and qtd1:
        ticker_list =wallet.get_tickers_list()
        ticker_list.remove(ticker1)
        return False, "Selecione uma ação", utils.make_select_list(ticker_list), False, "Digite a quantidade de ações"
    
    return True, "", [], True, ""


@app.callback(
    [Output("stock3-select", "disabled"), Output("stock3-select", "placeholder"), Output("stock3-select", "options"),
     Output("stock3-qtd-input", "disabled"), Output("stock3-qtd-input", "placeholder")],
    [Input("stock2-select", "value"), Input("stock2-qtd-input", "value"), Input("stock1-select", "value")]
)
def enable_stock3(ticker2, qtd2, ticker1):
    if ticker2 and qtd2:
        ticker_list =wallet.get_tickers_list()
        ticker_list.remove(ticker1)
        ticker_list.remove(ticker2)
        return False, "Selecione uma ação", utils.make_select_list(ticker_list), False, "Digite a quantidade de ações"
    
    return True, "", [], True, ""


@app.callback(
    [Output("stock4-select", "disabled"), Output("stock4-select", "placeholder"), Output("stock4-select", "options"),
     Output("stock4-qtd-input", "disabled"), Output("stock4-qtd-input", "placeholder")],
    [Input("stock3-select", "value"), Input("stock3-qtd-input", "value"), Input("stock2-select", "value"), Input("stock1-select", "value")]
)
def enable_stock4(ticker3, qtd3, ticker2, ticker1):
    if ticker3 and qtd3:
        ticker_list =wallet.get_tickers_list()
        ticker_list.remove(ticker1)
        ticker_list.remove(ticker2)
        ticker_list.remove(ticker3)
        return False, "Selecione uma ação", utils.make_select_list(ticker_list), False, "Digite a quantidade de ações"
    
    return True, "", [], True, ""


@app.callback(
    [Output("stock5-select", "disabled"), Output("stock5-select", "placeholder"), Output("stock5-select", "options"),
     Output("stock5-qtd-input", "disabled"), Output("stock5-qtd-input", "placeholder")],
    [Input("stock4-select", "value"), Input("stock4-qtd-input", "value"), Input("stock3-select", "value"), Input("stock2-select", "value"), Input("stock1-select", "value"),]
)
def enable_stock5(ticker4, qtd4, ticker3, ticker2, ticker1):
    if ticker4 and qtd4:
        ticker_list =wallet.get_tickers_list()
        ticker_list.remove(ticker1)     
        ticker_list.remove(ticker2)
        ticker_list.remove(ticker3)
        ticker_list.remove(ticker4)
        return False, "Selecione uma ação", utils.make_select_list(ticker_list), False, "Digite a quantidade de ações"
    
    return True, "", [], True, ""


@app.callback(
    [Output("create-wallet-alert","is_open"), Output("create-wallet-button", "n_clicks")],
    [Input("create-wallet-button", "n_clicks"), Input("stock1-select", "value"), Input("stock1-qtd-input", "value"),
     Input("stock2-select", "value"), Input("stock2-qtd-input", "value"),Input("stock3-select", "value"), 
     Input("stock3-qtd-input", "value"),Input("stock4-select", "value"), Input("stock4-qtd-input", "value"),
     Input("stock5-select", "value"), Input("stock5-qtd-input", "value")],
    [State("create-wallet-alert", "is_open")]
)
def create_wallet(n, ticker1, qtd1, ticker2, qtd2, ticker3, qtd3, ticker4, qtd4, ticker5, qtd5, is_open):
    if n:
        if ticker1 and qtd1:
            wallet.set_stocks([(ticker1, qtd1), (ticker2, qtd2), (ticker3, qtd3), (ticker4, qtd4), (ticker5, qtd5)])
            return not is_open, 0
    return is_open, 0


@app.callback(
    [Output("candlestick", "figure"),
    #  Output("volatility-graph", "figure")],
    ],
    [Input("stock-select-review", "value")]
)
def change_candlestick(stock):
    if stock:
        return [go.Figure(data=wallet.stocks[stock][2])]
    return [go.Figure()]


@app.callback(
    [Output("volatility-graph", "figure")],
    [Input("stock-select-review","value")]
)
def change_volatility_graph(stock):
    if stock:
        return [go.Figure(data=wallet.stocks[stock][3])]
    return [go.Figure()]

@app.callback(
    [Output("stock-price-variation", "children"), Output("stock-return", "children"),
     Output("stock-volatility", "children"), Output("stock-rentability", "children")],
    [Input("stock-select-review","value")]
)
def change_stock_info(stock):
    if stock:
        return "%1.2f" %(wallet.stocks[stock][6])+"%", "R$ %1.2f" %(wallet.stocks[stock][5]), "%1.2f" %(wallet.stocks[stock][4]), "%1.2f" %(wallet.stocks[stock][-1]) + "%"

    return "", "", "", "" 


if __name__ == "__main__":
    app.run_server(debug=True)