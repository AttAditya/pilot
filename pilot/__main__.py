from pilot.data.context import Context
from pilot.data.control import Control
from pilot.data.figures import Figures
from pilot.formatter.penguin import PenguinFormatter
from pilot.role.chat import Chat
from pilot.role.registry import ROLES
from pilot.role.user import User

def main():
  formatter = PenguinFormatter()
  context = Context(formatter)
  figures = Figures()
  figures.add_role(User())
  figures.add_role(Chat())
  initial_role = figures.get_role(ROLES.get_initial())
  control = Control(initial_role)

  while control.role is not None:
    content = control.role.act(context, figures)
    context.add_content(content)
    control.role = content.next_role

if __name__ == "__main__":
  main()

