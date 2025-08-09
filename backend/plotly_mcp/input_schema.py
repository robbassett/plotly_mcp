from typing import List, Dict, Any, Literal, Optional
from pydantic import BaseModel, Field

class OpenAiMessage(BaseModel):
    role: str
    content: str

class LineChartInput(BaseModel):
    x:List[List[float|int]] = Field(description="A nested list containing each set of x-values to include in the chart")
    y:List[List[float|int]] = Field(description="A nested list containing each set of y-values to include in the chart")
    hover_values:Optional[List[List[List[float|int|str]]]] = Field(description="An OPTIONAL nested list containing values that should be shown when hovering over points in the chart. The innermost list would contain the list of each custom data value associated with a single data point, can by any length but it must have the same number as the associated variable names are in hover_labels", default=None)
    hover_labels:Optional[List[str]] = Field(description="An OPTIONAL list containing the labels to be used with hover_values when displaying hover data in the chart, must have the same length as the innermost list in hover_values", default=None)
    labels:Optional[List[str]] = Field(description="The OPTIONAL list of dataset label to associate with each pair of x and y arrays", default=None)
    title:Optional[str] = Field(description="OPTIONAL title to add to the chart", default=None)
    axes_labels: Optional[Dict[Literal['x','y'],str]] = Field(description="The OPTIONAL labels to be added to the x and y axes", default=None)
    spline: bool = Field(description="If true this will smooth the line chart using a spline, this should only be applied if the x/y relationship is smooth (e.g. low/no noise!)",  default=False)