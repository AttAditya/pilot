from langex.core.classes import singleton

from pilot.role.base import BaseRole
from pilot.role.registry import ROLES
from pilot.role.user import User

@singleton
class RoleFactory:
  def __init__(self):
    self.roles = {
      ROLES.USER: {
        "class": User,
        "tools": [ROLES.USER],
      }
    }

  def create_role(self, role_name: str) -> BaseRole:
    if role_name not in self.roles:
      raise ValueError(f"Unknown role: {role_name}")

    role = self.roles[role_name]
    role_class = role["class"]
    tools: list[str] = role["tools"]
    instance: BaseRole = role_class()

    for tool_name in tools:
      if tool_name not in self.roles:
        continue

      tool = self.roles[tool_name]["class"]
      tool_desc = tool.__doc__ or "No description available."
      instance.add_tool(tool_name, tool_desc)

    return instance

