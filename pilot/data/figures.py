from langex.core.classes import langex_class
from langex.core.functions import autosig

from pilot.role.base import BaseRole

@langex_class
class Figures:
  def __init__(self):
    self.roles: dict[str, BaseRole] = {}

  @autosig
  def add_role(self, role: BaseRole):
    name = role.get_name()
    self.roles[name] = role

  @autosig
  def get_role(self, name) -> BaseRole | None:
    return self.roles.get(name, None)

  @autosig
  def get_roles(self):
    return list(self.roles.values())

