class ROLES:
  SYSTEM = "system"
  USER = "user"

  class PERSONAS:
    CHAT = "chat"

  class TOOLS:
    EXIT = "exit"

  @staticmethod
  def get_initial():
    return ROLES.USER

