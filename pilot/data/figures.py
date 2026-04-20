class Figures:
  def __init__(self):
    self.roles = {}

  def add_role(self, role):
    self.roles[role.name] = role

  def get_role(self, name):
    return self.roles.get(name, None)

  def get_roles(self):
    return list(self.roles.values())

