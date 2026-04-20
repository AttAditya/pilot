from langex.core.classes import interface
from langex.core.functions import args_optional, args_required, returns

@interface
class BaseIO:
  @args_optional(str | None)
  @returns(str)
  def get_input(self, context=None):
    ...

  @args_required(str)
  @returns(None)
  def push_output(self, content):
    ...

