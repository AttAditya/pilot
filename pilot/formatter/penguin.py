from langex.core.classes import implements

from pilot.formatter.base import BaseFormatter

@implements(BaseFormatter)
class PenguinFormatter:
  def format(self, content):
    name = content.source
    output = f"[{name}:start]\n"
    output += content.content
    output += f"\n[{name}:end]\n"

    return output

