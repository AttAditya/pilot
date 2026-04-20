from langex.core.classes import langex_class
from langex.core.functions import args_required, returns

from pilot.data.content import Content

@langex_class
class Context:
  def __init__(self, formatter):
    self.contents = []
    self.formatter = formatter

  @args_required(Content)
  def add_content(self, content):
    self.contents.append(content)

  @returns(str)
  def get_context(self):
    context = ""

    for content in self.contents:
      context += self.formatter.format(content)

    return context

