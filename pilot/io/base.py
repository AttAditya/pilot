from langex.core.classes import interface
from langex.core.functions import autosig

@interface
class BaseIO:
  @autosig
  def get_input(self, __context__: str | None = None):
    ...

  @autosig
  def push_output(self, __content__: str):
    ...

