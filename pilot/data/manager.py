from pilot.data.control import Control
from pilot.data.figures import Figures
from pilot.role.user import User

class Manager:
  def __init__(self):
    self.control = Control()
    self.figures = Figures()
    self.ready = False

  def setup(self):
    figures = [
      User(),
    ]

    for figure in figures:
      self.figures.add_role(figure)

    self.control.set_role(figures[0])
    self.control.start()
    self.ready = True

  def start(self):
    if not self.ready:
      raise Exception("Manager is not ready.")

    while self.control.is_active():
      role = self.control.get_role()
      content = role.produce()
      target_name = content.target

      if target_name is None:
        self.control.stop()
        continue

      target = self.figures.get_role(target_name)
      target.consume(content)
      self.control.set_role(target)

