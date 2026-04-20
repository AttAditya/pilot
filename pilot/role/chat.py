from langex.core.classes import implements

from pilot.data.content import Content
from pilot.io.pipe import CliIO
from pilot.role.base import BaseRole
from pilot.role.registry import ROLES

@implements(BaseRole)
class Chat:
  def __init__(self):
    self.name = ROLES.CHAT
    self.io = CliIO(["ollama", "run", "tili"])

  def act(self, context, figures):
    data = self.io.get_input(context.get_context())
    next_role = figures.get_role(ROLES.USER)

    return Content(self, data, next_role)

