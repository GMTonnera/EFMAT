from dash import html, dcc
import dash_bootstrap_components as dbc

import styles
import utils

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Info", href="/", active="exact"),
                dbc.NavLink("Criar", href="/criar", active="exact"),
                dbc.NavLink("Análise", href="/analise", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=styles.SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=styles.CONTENT_STYLE)


def info_page():
    return [
        html.Div(children=[
            html.Div(children=[
                html.H1("Trabalho Final")
            ]),
                
            html.Div(children=[
                html.H3("Descrição"),
                html.P("Este Dashboard foi criado como Projeto Final do curso de extensão EFMAT (Escola de Física e Matmática) da UNB (Universidade de Brasília)."
                    " O projeto consiste em um criador de carteiras de investimentos, no qual o usuário pode montar um portifólio com no máximo 5 ações, dentro"
                    " de um intervalo determinado pelo prórpio usuário. Para isso, foi utilizado o arquivo 'b3_stocks_1994_2020.csv', o qual possuí os valores"
                    " de fechamento, abertura, menor, maior e o volume de várias ações no período de 1994 a 2020, como fonte dos dados. O arquivo está disponível"
                    " para download na sessão downloads. Para criar uma carteira de investimentos, vá para a aba 'Criar' e preencha os campos com as informações"
                    " necessárias. Após a criação da carteira, é possível visualizar uma análise na aba de 'Análise'.")
            ]),
            
            html.Div(children=[
                html.H3("Autor"),
                html.P("Nome: Gustavo M. Tonnera"),
                html.P("Profissão: Estudante (Ciências da Computação - UNB)"),
                html.P("Email: gmtonnera@gmail.com")
            ]),

            html.Div(children=[
                html.H3("Downloads"),
                dbc.Button(id="download_dataset", children="b3_stocks_1994_2020.csv", color="info"),
                dcc.Download(id="download-component")
            ])
        ])
    ]


def criar_page(years):
    return [
        html.Div(children=[
            html.Div(children=[
                html.H1("Criar carteira")
            ]),
            html.Div(children=[
                dbc.Row([
                    dbc.Col([
                        dbc.Row([
                            html.H3("Passo 1")
                        ]),
                        
                        dbc.Row([
                            html.P("Escolha o ano, mês e dia, respectivamente, do início da análise.")
                        ]),
                        
                        dbc.Row([
                            dbc.Col([
                                html.P("Ano inicial:")
                            ], md=1),
                            dbc.Col([
                                dbc.Select(
                                    id="start-year-select",
                                    required=True,
                                    placeholder="Selecione um ano",
                                    options=years)
                            ], md=2)
                        ]),
                        
                        dbc.Row([
                            dbc.Col([
                                html.P("Mês inicial:")
                            ], md=1),
                            dbc.Col([
                                dbc.Select(
                                    id="start-month-select",
                                    disabled=True,
                                    placeholder="Selecione o mês inicial",
                                    options=[])
                            ], md=2),
                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.P("Dia inicial:")
                            ], md=1),
                            dbc.Col([
                                dbc.Select(
                                    id="start-day-select",
                                    disabled=True,
                                    placeholder="Selecione um dia",
                                    options=[])
                            ], md=2)
                        ])
                    ], md=6),
                    dbc.Col([
                        dbc.Row([
                            html.H3("Passo 2")
                        ]),
                        dbc.Row([
                            html.P("Escolha o ano, mês e dia, respectivamente, do final da análise.")
                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.P("Ano final:")
                            ], md=1),
                            dbc.Col([
                                dbc.Select(
                                    id="end-year-select",
                                    disabled=True,
                                    placeholder="",
                                    options=[])
                            ], md=2)
                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.P("Mês final:")
                            ], md=1),
                            dbc.Col([
                                dbc.Select(
                                    id="end-month-select",
                                    disabled=True,
                                    placeholder="",
                                    options=[])
                            ], md=2)
                        ]),

                        dbc.Row([
                            dbc.Col([
                                html.P("Dia final:")
                            ], md=1),
                            dbc.Col([
                                dbc.Select(
                                    id="end-day-select",
                                    disabled=True,
                                    placeholder="",
                                    options=[])
                            ], md=2)
                        ])
                    ], md=6)
                ])
            ]),

            html.Div(children=[
                dbc.Row([
                    html.H3("Passo 3")
                ]),
                dbc.Row([
                    html.P("Escolha até 5 ações para compor a carteira.")
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(),
                            dbc.CardBody([
                                html.H4("Ação 1"),
                                dbc.Select(
                                    id="stock1-select",
                                    disabled=True,
                                    options=[]),
                                dbc.Input(id="stock1-qtd-input", type="number", min=1, max=1000000000000000,step=1, required=True, disabled=True)
                            ])
                        ], style={"background-color": "#205072"})
                    ]),

                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(),
                            dbc.CardBody([
                                html.H4("Ação 2"),
                                dbc.Select(
                                    id="stock2-select",
                                    disabled=True,
                                    options=[]),
                                dbc.Input(id="stock2-qtd-input", type="number", min=1, max=1000000000000000,step=1, disabled=True)
                            ])
                        ], style={"background-color": "#329D9C"})
                    ]),

                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(),
                            dbc.CardBody([
                                html.H4("Ação 3"),
                                dbc.Select(
                                    id="stock3-select",
                                    disabled=True,
                                    options=[]),
                                dbc.Input(id="stock3-qtd-input", type="number", min=1, max=1000000000000000,step=1, disabled=True)
                            ])
                        ], style={"background-color": "#56C596"})
                    ]),

                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(),
                            dbc.CardBody([
                                html.H4("Ação 4"),
                                dbc.Select(
                                    id="stock4-select",
                                    disabled=True,
                                    options=[]),
                                dbc.Input(id="stock4-qtd-input", type="number", min=1, max=1000000000000000,step=1, disabled=True)
                            ])
                        ], style={"background-color": "#7BE495"})
                    ]),

                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(),
                            dbc.CardBody([
                                html.H4("Ação 5"),
                                dbc.Select(
                                    id="stock5-select",
                                    disabled=True,
                                    options=[]),
                                dbc.Input(id="stock5-qtd-input", type="number", min=1, max=1000000000000000,step=1, disabled=True)
                            ])
                        ], style={"background-color": "#CFF4D2"})
                    ])
                ]),

                dbc.Row([
                    dbc.Button(id="create-wallet-button",
                               children="Criar carteira",
                               color='primary',
                               style={"margin-top": "2rem"})
                ]),

                dbc.Row([
                    dbc.Alert(
                        "Sua carteira foi criada com sucesso! Acesse a aba 'Análise' para adquirir mais informações sobre ela.",
                        id="create-wallet-alert",
                        dismissable=True,
                        is_open=False,
                        style={"margin-top": "2rem"}
                    )
                ]) 
            ])
        ]) 
    ]


def review_pag(wallet):
    if len(wallet.stocks.keys()) > 0:
        return [html.Div(children=[
            html.Div(children=[
                dbc.Row([
                    html.H1("Análise da carteira")
                ])
            ]),

            html.Div(children=[
                dbc.Row([
                    dbc.Col([
                        dbc.Card(
                            dbc.CardBody([
                                html.H5("Retorno da carteira: "),
                                html.P("R$ %5.2f" %(wallet.wallet_info['Return']))
                            ]),
                        style={"background-color": "#329D9C"})
                    ], md=3),
                
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Rentabilidade real da carteira: "),
                                html.P("%3.2f"%(wallet.wallet_info['Rentability'])+ "%")
                            ])
                        ], style={"background-color": "#56C596"})
                    ], md=3),

                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Volatividade média da carteira: "),
                                html.P("%3.2f"%(wallet.wallet_info['Volatility']))
                            ])
                        ], style={"background-color": "#7BE495"})
                    ], md=3),

                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Período: "),
                                html.P(f"Início: {wallet.get_start_date()}"),
                                html.P(f"Fim: {wallet.get_end_date()}")
                            ])
                        ], style={"background-color": "#CFF4D2"})
                    ], md=3),
                ])
            ]),

            html.Div(children=[
                dbc.Row([
                    html.P("Selecione uma ação abaixo para obter informações específicas sobre ela.")
                ]),

                dbc.Row([
                    dbc.Select(
                        id="stock-select-review",
                        placeholder="Selecione uma ação da carteira",
                        options=utils.make_select_list(list(wallet.stocks.keys())),
                        style={"margin-bottom": "2rem"}
                    )
                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.Card(
                            dbc.CardBody([
                                html.H6("Variação do preço: "),
                                html.P(id="stock-price-variation", children="Número")
                            ]), style={"background-color": "#CFF4D2"}
                        )
                    ], md=3),
                    
                    dbc.Col([
                        dbc.Card(
                            dbc.CardBody([
                                html.H6("Retorno: "),
                                html.P(id="stock-return", children="Número")
                            ]), style={"background-color": "#7BE495"}
                        )   
                    ], md=3),
                    
                    dbc.Col([
                        dbc.Card(
                            dbc.CardBody([
                                html.H6("Volatilidade: "),
                                html.P(id="stock-volatility", children="Número")
                            ]), style={"background-color": "#56C596"}
                        )
                    ], md=3),

                    dbc.Col([
                        dbc.Card(
                            dbc.CardBody([
                                html.H6("Rentabilidade real: "),
                                html.P(id="stock-rentability", children="Número")
                            ]), style={"background-color": "#329D9C"}
                        )
                    ], md=3)
                ]),

                dbc.Row([
                    dbc.Col([
                        dcc.Graph(
                            id="candlestick",
                            style={"background-color": "rgb(240,240,240)"}
                    )], md=6),

                    dbc.Col([
                        dcc.Graph(
                            id="volatility-graph", 
                            style={"background-color": "rgb(240,240,240)"}
                            )
                    ], md=6)
                ])
            ])
        ])
    ]

    return [html.Div(children=[
        html.P("Primeiramente, crie uma carteira para poder analisá-la.")
        ])
    ]