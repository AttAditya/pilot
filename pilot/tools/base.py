from langex.core.classes import interface
from langex.core.functions import args_dynamic

@interface
class BaseTool:
  @args_dynamic(str)
  def use(self, **_):
    ...

