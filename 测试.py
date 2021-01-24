import dash
import dash_core_components as dcc                 #交互式组件
import dash_html_components as html                #代码转html
from dash.dependencies import Input, Output        #回调
import pandas as pd
import os
import plotly.graph_objects as go


class 测试:
    def __init__(self):
        self.做图()
    def 读文件(self):
        路径 = os.path.split(os.path.realpath(__file__))[0]+'\\'
        本地电商2021 = pd.io.excel.ExcelFile(路径 + '全域汇总\本地电商总表_2021.xlsx')
        数据 = {}
        for name in 本地电商2021.sheet_names:
            df = pd.read_excel(本地电商2021, sheet_name=name)
            数据[name] = df
        self.饿了么 = 数据['饿了么']

    def 做图(self):
        self.读文件()
        # css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        self.app = dash.Dash(__name__)
        self.app.layout = html.Div(
            children=[
                html.H1(children="饿了么销量"),
                html.P(
                    children="这是一次测试"
                ),
                dcc.Graph(
                    figure={
                        "data": [
                            {
                                "x": self.饿了么['下单时间'],
                                "y": self.饿了么['实收'],
                                "type": "lines",
                            },
                        ],
                        "layout": {"title": "饿了么销量"},
                    },
                ),
                dcc.Graph(
                  figure={
                      "data": [
                          {
                              "x": self.饿了么['下单时间'],
                              "y": self.饿了么['优惠前单价'],
                              "type": "lines",
                          },
                      ],
                      "layout": {"title": "饿了么优惠前单价"},
                  },
                ),
            ]
        )

if __name__=='__main__':
    测试().app.run_server(debug=True)


