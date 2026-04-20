from langex.core.classes import implements

from pilot.formatter.base import BaseFormatter

@implements(BaseFormatter)
class PenguinFormatter:
  def format(self, content):
    output = f"[{content.role.name}:start]\n"
    output += content.data
    output += f"\n[{content.role.name}:end]\n"

    return output

