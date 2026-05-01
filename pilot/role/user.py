from langex.core.classes import extends

from pilot.data.content import Content
from pilot.data.context import Context
from pilot.formatter.penguin import PenguinFormatter
from pilot.io.console import ConsoleIO
from pilot.role.base import BaseRole
from pilot.role.registry import ROLES

@extends
class User(BaseRole):
  """
  User role represents the end user interacting with the system.
  It is responsible for producing content based on user input and
  consuming content to provide feedback or responses to the user.
  The User role uses a console-based IO for interaction and a
  formatter to structure the content in a specific format.
  """

  def __init__(self):
    super().__init__()
    self.name = ROLES.USER
    self.context = Context()
    self.io = ConsoleIO()
    self.formatter = PenguinFormatter()

  def produce(self) -> Content:
    content = self.io.get_input("User: ")
    target = ROLES.PERSONAS.CHAT

    if content[0] == "!":
      target = content[1:].split(" ")[0]

    if not self.has_tool(target):
      return Content(
        ROLES.SYSTEM,
        ROLES.USER,
        "Pass was invalid, please refer tools and personas available."
        f"\nTools: {', '.join(self.get_tools())}"
      )

    return Content(ROLES.USER, target, content)

  def consume(self, content: Content):
    self.context.add_content(content)
    context = self.context.get_context(self.formatter)
    self.io.push_output(context)

