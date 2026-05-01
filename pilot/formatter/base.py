from langex.core.classes import interface
from langex.core.functions import autosig

from pilot.data.content import Content

@interface
class BaseFormatter:
  @autosig
  def format(self, __content__: Content) -> str:
    ...

