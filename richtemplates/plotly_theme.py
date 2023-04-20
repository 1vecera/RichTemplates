# %%
from pathlib import Path
import plotly
import plotly.graph_objects as go
from plotly import graph_objs as go
import datetime
import pandas as pd

ytd_date_range = (datetime.datetime.now() - pd.offsets.YearBegin(), datetime.datetime.now())


def generate_RichView_plotly_theme():
    template = go.layout.Template()

    # Colors
    template.layout.plot_bgcolor = "#FAF9F6"
    template.layout.paper_bgcolor = "#FAF9F6"
    template.layout.xaxis.gridcolor = "#CCC1B7"
    template.layout.yaxis.gridcolor = "#CCC1B7"
    template.layout.xaxis.tickcolor = "#4D4845"
    template.layout.yaxis.tickcolor = "#4D4845"
    template.layout.xaxis.title.font.color = "#4D4845"
    template.layout.yaxis.title.font.color = "#4D4845"

    # Grid
    template.layout.xaxis.showgrid = False
    template.layout.yaxis.showgrid = True
    template.layout.xaxis.gridwidth = 0.2
    template.layout.yaxis.gridwidth = 0.2
    template.layout.xaxis.zeroline = False
    template.layout.yaxis.zeroline = False

    # Ticks
    template.layout.xaxis.tickmode = "auto"
    template.layout.yaxis.tickmode = "auto"
    template.layout.xaxis.ticklen = 3.5
    template.layout.yaxis.ticklen = 0
    template.layout.xaxis.tickwidth = 0.2
    template.layout.yaxis.tickwidth = 0.2

    # Lines
    template.layout.colorway = [
        "#186cac", "#81e7cc", "#eec8f1", "#dce475", "#86ec5a", "#eb70d5", "#829951", "#5a3386",
        "#a50fa9", "#4ba40b"
    ]

    # Fonts
    template.layout.font.family = "Lora, Palatino Linotype, Cambria, Century Gothic"
    template.layout.font.size = 12
    template.layout.xaxis.title.font.size = 10.8
    template.layout.yaxis.title.font.size = 10.8
    template.layout.xaxis.tickfont.size = 9.6
    template.layout.yaxis.tickfont.size = 9.6
    template.layout.legend.font.size = 9.6

    # Legend
    template.layout.legend.bgcolor = "rgba(0,0,0,0)"
    template.layout.legend.xanchor = "left"
    template.layout.legend.yanchor = "top"
    template.layout.legend.x = 0
    template.layout.legend.y = 1.05

    template.layout.legend.orientation = "h"
    template.layout.legend.xanchor = "left"
    template.layout.legend.valign = "top"
    template.layout.legend.title.text = ""

    # template.layout.legend.handletextpad = 0.8
    # template.layout.legend.handlelength = 2
    # template.layout.legend.labelspacing = 0.5

    # Figure
    template.layout.width = 600
    template.layout.height = 400
    template.layout.margin = dict(l=60, r=60, t=60, b=60)

    # Axes

    template.layout.xaxis.showspikes = False
    template.layout.yaxis.showspikes = False
    template.layout.xaxis.showline = True
    template.layout.yaxis.showline = False
    template.layout.xaxis.linewidth = 0.2
    template.layout.yaxis.linewidth = 0.2
    template.layout.xaxis.mirror = False
    template.layout.yaxis.mirror = False
    template.layout.xaxis.side = "bottom"
    template.layout.yaxis.side = "left"

    # Title and Suptitle
    template.layout.title.x = 0
    template.layout.title.font.size = 14.4
    template.layout.title.xanchor = "left"
    template.layout.title.xref = "paper"

    return template


def format_figure(fig: go.Figure):
    fig.update_layout(xaxis_title=None, yaxis_title=None, legend_title=None, hovermode='x')
    fig.update_xaxes(tickformat='%d %b %y')
    fig.update_traces(hovertemplate=None)
    return fig


def add_invasion_date_line(figure: go.Figure) -> go.Figure:
    date = '2022-02-24'
    comment = 'Invasion of Ukraine'
    color = '#000000'
    # noinspection PyTypeChecker
    figure = add_date_line(color, comment, date, figure)
    return figure


def add_date_line(color, comment, date, figure):
    figure.add_vline(x=date, line=go.layout.shape.Line(width=1, color=color))
    figure.add_annotation(x=date,
                          xanchor='left',
                          xshift=1,
                          text=comment,
                          font=go.layout.annotation.Font(color=color),
                          showarrow=False)
    return figure


def helper_range_selector():
    return go.layout.xaxis.Rangeselector(buttons=list([
        go.layout.xaxis.rangeselector.Button(count=1, label="1m", step="month",
                                             stepmode="backward"),
        go.layout.xaxis.rangeselector.Button(count=6, label="6m", step="month",
                                             stepmode="backward"),
        go.layout.xaxis.rangeselector.Button(count=1, label="YTD", step="year", stepmode="todate"),
        go.layout.xaxis.rangeselector.Button(count=1, label="1y", step="year", stepmode="backward"),
        go.layout.xaxis.rangeselector.Button(step="all")
    ]))


def create_timerange_selector(fig: go.Figure, date_range=ytd_date_range) -> go.Figure:
    # Add range slider

    fig.update_layout(xaxis=go.layout.XAxis(
        range=ytd_date_range, rangeselector=helper_range_selector(), type="date"))
    return fig


def export_chart(config: dict,
                 figure: go.Figure,
                 name: str,
                 source_df: pd.DataFrame,
                 save_dir='out'):
    save_dir = Path(save_dir)
    save_dir.mkdir(exist_ok=True)

    source_df.to_csv(Path(save_dir, f'{name}.csv'), index=False)
    figure.write_html(Path(save_dir, f'{name}.html'), config=config)
    figure.write_html(Path(save_dir, f'{name}_small.html'), config=config, include_plotlyjs=False)
    plotly.io.write_image(figure, Path(save_dir, f'{name}.png'))
    plotly.io.write_json(figure, Path(save_dir, f'{name}.json'), pretty=True)
