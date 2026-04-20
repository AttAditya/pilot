from decimal import Context

from langex.core.classes import implements
from langex.core.functions import args_required

from pilot.data.content import Content
from pilot.io.console import ConsoleIO
from pilot.role.base import BaseRole
from pilot.role.registry import ROLES

@implements(BaseRole)
class User:
  def __init__(self):
    self.name = ROLES.USER
    self.io = ConsoleIO()
    self.synced = 0

  @args_required(object)
  def sync_chat(self, context):
    if self.synced < len(context.contents):
      for content in context.contents[self.synced:]:
        if content.role.name == ROLES.USER:
          continue

        self.io.push_output(f"[{content.role.name}] {content.data}")

      self.synced = len(context.contents)

  def act(self, context, figures):
    self.sync_chat(context)
    data = self.io.get_input("[you] ")
    next_role = figures.get_role(ROLES.CHAT)

    if data[0] == "!":
      if data.startswith("!exit ") or data == "!exit":
        next_role = None

    return Content(self, data, next_role)

