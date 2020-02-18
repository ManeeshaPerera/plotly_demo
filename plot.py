import plotly.graph_objs as go
from plotly.subplots import make_subplots


def plot_data(x_axis_data, y_axis_data, trace_name, x_axis_title, y_axis_title, mode='lines', title=None):
    """
    :param x_axis_data: <array>, array of data for the x axis
    :param y_axis_data: <array>, array of data for the y axis
    :param trace_name: <string>, name of the trace of the figure
    :param x_axis_title: <string>, x axis title of the graph
    :param y_axis_title: <string>, y axis title of the graph
    :return: <plotly figure object>, returns a plolty figure
    """
    trace = go.Scatter(
        x=x_axis_data,
        y=y_axis_data,
        name=trace_name,
        mode=mode
    )

    # Custom layout
    layout = go.Layout(
        title=title,
        yaxis=dict(
            title=y_axis_title,
        ),
        xaxis=dict(
            title=x_axis_title,
        ),
    )

    return go.Figure(data=trace, layout=layout)


def plot_two_time_series(x_axis_data1, y_axis_data1, trace_name1, x_axis_title, y_axis_title1, x_axis_data2,
                         y_axis_data2, trace_name2, y_axis_title2, mode='lines', title=None):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=x_axis_data1,
                   y=y_axis_data1,
                   name=trace_name1,
                   mode=mode),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=x_axis_data2,
                   y=y_axis_data2,
                   name=trace_name2,
                   mode=mode),
        secondary_y=True,
    )

    fig.update_layout(
        title_text=title
    )

    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text=y_axis_title1, secondary_y=False)
    fig.update_yaxes(title_text=y_axis_title2, secondary_y=True)

    return fig


def plot_time_series_graphs(data_array, x_axis_title, trace_names, mode='lines', title=None):
    fig = make_subplots(rows=len(data_array), cols=1, shared_xaxes=True)

    data_num = 0
    for data in data_array:
        fig.add_trace(
            go.Scatter(x=data.index,
                       y=data['Value'],
                       name=trace_names[data_num],
                       mode=mode), row=data_num + 1, col=1
        )
        data_num = data_num + 1

    layout = go.Layout(
        xaxis2=dict(
            title=x_axis_title,
        ),
        title_text=title
    )
    fig.update_layout(layout)

    return fig


def plot_time_series_graphs_2(data_array, x_axis_title, trace_names, mode='lines', title=None):
    fig = make_subplots(rows=len(data_array) - 1, cols=1, shared_xaxes=True,
                        specs=[[{"secondary_y": True}], [{"secondary_y": False}]])

    for data in range(len(data_array) - 1):
        fig.add_trace(
            go.Scatter(x=data_array[data].index,
                       y=data_array[data]['Value'],
                       name=trace_names[data],
                       mode=mode), row=data + 1, col=1
        )

    next_data = data_array[-1]
    fig.add_trace(
        go.Scatter(x=next_data.index,
                   y=next_data['Value'],
                   name=trace_names[-1],
                   mode=mode), row=1, col=1,
        secondary_y=True
    )
    layout = go.Layout(
        xaxis2=dict(
            title=x_axis_title,
        ),
        title_text=title
    )
    fig.update_layout(layout)

    return fig


def plot_all_time_series(data_array, trace_names, x_axis_title, mode='lines', title=None):
    fig = make_subplots(shared_xaxes=True,
                        specs=[[{"secondary_y": True}]])
    for data in range(0, len(data_array)):
        secondary_y = False
        if data > 0:
            secondary_y = True
        fig.add_trace(
            go.Scatter(x=data_array[data].index,
                       y=data_array[data]['Value'],
                       name=trace_names[data],
                       mode=mode),
            secondary_y=secondary_y
        )
    layout = go.Layout(
        xaxis2=dict(
            title=x_axis_title,
        ),
        title_text=title
    )
    fig.update_layout(layout)

    return fig
