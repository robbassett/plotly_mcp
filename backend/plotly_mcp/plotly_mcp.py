"""The MCP Server Containing Tools for Plotly Charts"""
from typing import List

from fastmcp import FastMCP
import plotly.graph_objects as go

from .input_schema import LineChartInput

plotly_mcp = FastMCP(name="Plotly MCP")

@plotly_mcp.tool
def line_plot(props:LineChartInput) -> str:
    """
    Generate a line chart containing one or more traces of data.

    A line chart is ideal for visualizing data that changes continuously over time. It's used to show trends, patterns, and rate of change for one or more variables. 
    This chart type is particularly effective when you have a series of data points collected at regular intervals, such as daily stock prices, monthly sales figures, 
    or hourly temperature readings.

    When to Use a Line Chart
    -Tracking Trends Over Time: A key use is to see how a value, like website traffic or sales, has changed over weeks, months, or years. The connected data points 
    make it easy to spot upward or downward trends.

    -Comparing Multiple Variables: You can plot multiple lines on the same chart to compare the trends of different groups. For example, comparing the sales 
    performance of two different products over the same time period.

    -Identifying Patterns: Line charts help reveal patterns such as seasonality (e.g., sales spiking every December) or cyclical behavior.

    -Showing Volatility: The steepness of the lines indicates the rate of change or volatility. A steep line shows rapid change, while a flatter line indicates 
    slower, more stable change. This is often used in finance to visualize stock market fluctuations.

    -Forecasting: By extending the trend of a line chart, you can make predictions about future values
    """
    figure = go.Figure()
    x,y = props.x,props.y

    custom = props.custom_data
    label = props.labels
    axes_labels = props.axes_labels or {}

    for data_index,(_x,_y) in enumerate(zip(x,y)):
        _custom = custom[data_index] if custom else None
        _label = label[data_index] if label else None

        figure.add_trace(go.Scatter(
            x=_x,
            y=_y,
            customdata=_custom,
            name=_label
        ))

    figure.update_layout(
        yaxis_title=axes_labels.get("y"),
        xaxis_title=axes_labels.get("x"),
        title=props.title or ""
    )

    return figure.to_json()

@plotly_mcp.tool
def bar_chart(x:List[str], y:List[int | float]) -> str:
    """
    This tool takes in categories as "x" and the counts or values of a given category as "y". A bar 
    chart's general purpose is to compare values of discrete categories or show changes over time using 
    rectangular bars of varying heights or lengths, where each bar represents a distinct category 
    and its height/length corresponds to the value being measured.

    Params
    ------
    x : list
        The list of categories for the x-axis of the chart
    y : list
        The list of values associated with each category describing the bar height
    """
    figure = go.Figure(
        data=go.Bar(
            x=x,
            y=y
        )
    )

    return figure.to_json()

@plotly_mcp.tool
def heat_map(x:List[int | float | str], y:List[int | float | str], z: List[List[int | float]]) -> str:
    """
    This tool takes in x, y, and z values to produce a heatmap. A heat map's general purpose is to 
    visualize the intensity or density of data points across a two-dimensional space, using a 
    spectrum of colors to represent varying values. This allows for quick identification of patterns, 
    hotspots, and areas of high or low activity within complex datasets.

    Params
    ------
    x : list
        The list of x values for the x-axis, can be numerical or categorical
    y : list
        The list of y values for the y-axis, can be numerical or categorical
    z : list
        The list of numerical values associated with each x/y location on the 2D grid, will translate
        into the heatmap intensity at that position
    """
    figure = go.Figure(
        data = go.Heatmap(
            z=z,
            x=x,
            y=y
        )
    )    

    return figure.to_json()
