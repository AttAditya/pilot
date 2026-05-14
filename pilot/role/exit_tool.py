from langex.core.classes import extends

from pilot.data.content import Content
from pilot.data.context import Context
from pilot.io.console import ConsoleIO
from pilot.role.base import BaseRole
from pilot.role.registry import ROLES

@extends
class ExitTool(BaseRole):
  """
  Exit tool role represents a tool for exiting the application.
  It is responsible for handling exit commands and terminating
  the application.
  """

  def __init__(self):
    super().__init__()
    self.name = ROLES.TOOLS.EXIT
    self.io = ConsoleIO()

  def produce(self) -> Content:
    return Content(ROLES.TOOLS.EXIT, None, "")

  def consume(self, __content__: Content):
    self.io.push_output("Exiting the application...")

    return None

