from langex.core.classes import abstract
from langex.core.functions import abstracted, autosig

from pilot.data.content import Content

@abstract
class BaseRole:
  def __init__(self):
    self.name: str = "BaseRole"
    self.tools: dict[str, str] = {}

  @autosig
  def get_name(self) -> str:
    return self.name

  @autosig
  def add_tool(self, tool_name: str, tool_desc: str):
    self.tools[tool_name] = tool_desc

  @autosig
  def get_tools(self) -> list:
    result: list[str] = list(self.tools.keys())

    return result

  @autosig
  def has_tool(self, tool_name: str) -> bool:
    return tool_name in self.tools

  @abstracted
  @autosig
  def consume(self, __content__: Content) -> None:
    ...

  @abstracted
  @autosig
  def produce(self) -> Content:
    ...

