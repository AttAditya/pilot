from langex.core.classes import interface
from langex.core.functions import args_required, returns

from pilot.data.content import Content

@interface
class BaseFormatter:
  @args_required(Content)
  @returns(str)
  def format(self, __content__):
    ...

