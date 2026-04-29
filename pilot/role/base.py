from langex.core.classes import abstract
from langex.core.functions import abstracted, autosig

from pilot.data.content import Content

@abstract
class BaseRole:
  def add_tool(self, tool_name: str, tool_desc: str):
    if not hasattr(self, "tools"):
      self.tools: dict[str, str] = {}

    self.tools[tool_name] = tool_desc

  def check_tool_call(self, data: str) -> tuple[str | None, str]:
    if not data.startswith("!"):
      return None, data
    
    if not hasattr(self, "tools"):
      self.tools: dict[str, str] = {}

    lines = data.splitlines()
    tool_name = lines.pop(0)[1:]

    if tool_name not in self.tools:
      return None, data

    updated_data = "\n".join(lines).strip()

    return tool_name, updated_data

  @abstracted
  @autosig
  def get_name(self) -> str:
    ...

  @abstracted
  @autosig
  def consume(self, __content__: Content) -> None:
    ...

  @abstracted
  @autosig
  def produce(self) -> Content:
    ...

