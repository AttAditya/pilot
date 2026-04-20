from langex.core.functions import returns

class ROLES:
  USER = "user"
  CHAT = "chat"

  @staticmethod
  def get_initial():
    return ROLES.USER

