from langex.core.classes import langex_class
from langex.core.functions import args_required, returns

from pilot.data.content import Content
from pilot.formatter.base import BaseFormatter

@langex_class
class Context:
  def __init__(self):
    self.contents = []
    self.formatter = None

  @args_required(BaseFormatter)
  def attach_formatter(self, formatter):
    self.formatter = formatter

  @args_required(Content)
  def add_content(self, content):
    self.contents.append(content)

  @returns(str)
  def get_context(self):
    if self.formatter is None:
      raise Exception("Formatter is not attached.")

    context = ""

    for content in self.contents:
      context += self.formatter.format(content)

    return context

