from langex.core.classes import implements

from pilot.io.base import BaseIO

@implements(BaseIO)
class ConsoleIO:
  def get_input(self, prompt=""):
    data = ""

    while not data:
      data = input(prompt).strip()

    return data

  def push_output(self, content):
    print(content)

