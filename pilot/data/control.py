from langex.core.classes import langex_class
from langex.core.functions import autosig

from pilot.role.base import BaseRole

@langex_class
class Control:
  def __init__(self):
    self.role: BaseRole = None
    self.started: bool = False

  @autosig
  def set_role(self, role: BaseRole) -> None:
    self.role = role

  @autosig
  def get_role(self) -> BaseRole:
    return self.role

  @autosig
  def is_active(self) -> bool:
    return self.started

  @autosig
  def start(self) -> None:
    self.started = True

  @autosig
  def stop(self) -> None:
    self.started = False

