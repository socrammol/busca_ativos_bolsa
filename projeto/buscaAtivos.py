from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt


def busca_ativos(ticker, start, end):
    cotacao_b3 = web.DataReader(ticker, data_source='yahoo', start=start, end=end)
    print(cotacao_b3)
