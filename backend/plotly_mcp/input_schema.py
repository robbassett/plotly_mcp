from typing import List, Dict, Any, Literal, Optional
from pydantic import BaseModel, Field

class OpenAiMessage(BaseModel):
    role: str
    content: str

class LineChartInput(BaseModel):
    x:List[List[float|int]] = Field(description="A nested list containing each set of x-values to include in the chart")
    y:List[List[float|int]] = Field(description="A nested list containing each set of y-values to include in the chart")
    custom_data:List[List[Any]] = Field(description="A nested list containing any custom data to be included with each data point, custom data can be used to include additional information when hovering over a datapoint.")
    labels:Optional[List[str]] = Field(description="The list of dataset label to associate with each pair of x and y arrays")
    title:Optional[str] = Field(description="Title to add to the chart")
    axes_labels: Optional[Dict[Literal['x','y'],str]] = Field(description="The labels to be added to the x and y axes")
