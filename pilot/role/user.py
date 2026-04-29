from langex.core.classes import extends

from pilot.data.content import Content
from pilot.data.context import Context
from pilot.role.base import BaseRole
from pilot.role.registry import ROLES

@extends
class User(BaseRole):
  def __init__(self):
    self.name = ROLES.USER
    self.context = Context()

  def get_name(self) -> str:
    return self.name

  def produce(self) -> Content:
    data: str = ""

    while not data.strip():
      data = input("User: ").strip()

    tool_name, updated_data = self.check_tool_call(data)
    content = Content(tool_name, updated_data)

    return content

  def consume(self, content: Content):
    self.context.add_content(content)

