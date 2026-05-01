from langex.core.classes import langex_class
from langex.core.functions import autosig

from pilot.data.content import Content
from pilot.formatter.base import BaseFormatter

@langex_class
class Context:
  def __init__(self):
    self.contents = []

  @autosig
  def add_content(self, content: Content):
    self.contents.append(content)

  @autosig
  def get_context(self, formatter: BaseFormatter) -> str:
    context = ""

    for content in self.contents:
      context += formatter.format(content)

    return context

