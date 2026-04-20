from langex.core.classes import interface
from langex.core.functions import args_required, returns

from pilot.data.content import Content
from pilot.data.context import Context
from pilot.data.figures import Figures

@interface
class BaseRole:
  @args_required(Context, Figures)
  @returns(Content)
  def act(self, __context__, __figures__):
    ...

