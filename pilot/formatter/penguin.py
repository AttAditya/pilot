from langex.core.classes import implements

from pilot.formatter.base import BaseFormatter

@implements(BaseFormatter)
class PenguinFormatter:
  def format(self, content):
    name = content.role.get_name()
    output = f"[{name}:start]\n"
    output += content.data
    output += f"\n[{name}:end]\n"

    return output

