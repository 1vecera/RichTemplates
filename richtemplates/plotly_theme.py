
# %%
from pathlib import Path
import plotly
import plotly.graph_objects as go
from plotly import graph_objs as go
import datetime
import pandas as pd

ytd_date_range = (datetime.datetime.now() - pd.offsets.YearBegin(), datetime.datetime.now())


def generate_RichView_plotly_theme():
    color_gridlines = 'rgba(238,238,238,0.9)'
    color_ticks = 'rgba(0,0,0,0.9)'

    color_discrete_sequence = ["#9e2b25", "#223843", "#f9e784", "#a1b5d8", "#697a21", "#ff7f51",
                               "#2191fb", "#dc7f9b", "#9cfffa", "#ece5f0"]


    annotation_template = go.layout.Template()
    annotation_template.data.scatter = [go.Scatter(hovertemplate=None, connectgaps=True)]
    annotation_template.data.scattergl = [go.Scattergl(hovertemplate=None, connectgaps=True)]

    annotation_template.layout.legend = go.layout.Legend(orientation='h',
                                                         yanchor='top',
                                                         xanchor='center',
                                                         y=0.9,
                                                         x=0.5,
                                                         title=None)

    annotation_template.layout.font = go.layout.Font(family='Segoe UI',
                                                     size=14)
    annotation_template.layout.yaxis = go.layout.YAxis(showgrid=True,
                                                       ##
                                                       gridwidth=1,
                                                       gridcolor=color_gridlines,
                                                       ticks='outside',
                                                       ##
                                                       tickwidth=1,
                                                       tickcolor=color_ticks,
                                                       ticklen=5,
                                                       ##
                                                       zeroline=False,
                                                       title=go.layout.yaxis.Title(text=None))
    annotation_template.layout.xaxis = go.layout.XAxis(showgrid=True,
                                                       gridwidth=1,
                                                       gridcolor=color_gridlines,
                                                       ##
                                                       title=go.layout.xaxis.Title(text=None),
                                                       ticks='outside',
                                                       ##
                                                       tickwidth=1,
                                                       tickcolor=color_ticks,
                                                       ticklen=10,
                                                       ##
                                                       showline=True,
                                                       linewidth=1,
                                                       linecolor='black',
                                                       ##
                                                       zeroline=False)
    annotation_template.layout.hovermode = 'x'
    annotation_template.layout.colorway = color_discrete_sequence

    config = dict({'scrollZoom': True})

    return annotation_template


def format_figure(fig: go.Figure):
    fig.update_layout(xaxis_title=None,
                      yaxis_title=None,
                      legend_title=None,
                      hovermode='x')
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


def add_date_line(color,
                  comment,
                  date,
                  figure):
    figure.add_vline(x=date, line=go.layout.shape.Line(width=1, color=color))
    figure.add_annotation(x=date, xanchor='left', xshift=1, text=comment,
                          font=go.layout.annotation.Font(color=color),
                          showarrow=False)
    return figure


def helper_range_selector():
    return go.layout.xaxis.Rangeselector(

        buttons=list([
            go.layout.xaxis.rangeselector.Button(count=1,
                                                 label="1m",
                                                 step="month",
                                                 stepmode="backward"),
            go.layout.xaxis.rangeselector.Button(count=6,
                                                 label="6m",
                                                 step="month",
                                                 stepmode="backward"),
            go.layout.xaxis.rangeselector.Button(count=1,
                                                 label="YTD",
                                                 step="year",
                                                 stepmode="todate"),
            go.layout.xaxis.rangeselector.Button(count=1,
                                                 label="1y",
                                                 step="year",
                                                 stepmode="backward"),
            go.layout.xaxis.rangeselector.Button(step="all")
        ]))


def create_timerange_selector(fig: go.Figure,
                              date_range=ytd_date_range) -> go.Figure:
    # Add range slider

    fig.update_layout(
        xaxis=go.layout.XAxis(
            range=ytd_date_range,
            rangeselector=helper_range_selector(),
            type="date"
        )
    )
    return fig

def export_chart(config:dict, figure:go.Figure, name:str, source_df:pd.DataFrame,  save_dir='out'):
    save_dir = Path(save_dir)
    save_dir.mkdir(exist_ok=True)

    source_df.to_csv(Path(save_dir, f'{name}.csv'), index=False)
    figure.write_html(Path(save_dir, f'{name}.html'), config=config)
    figure.write_html(Path(save_dir, f'{name}_small.html'), config=config, include_plotlyjs=False)
    plotly.io.write_image(figure, Path(save_dir, f'{name}.png'))
    plotly.io.write_json(figure, Path(save_dir, f'{name}.json'), pretty=True)
