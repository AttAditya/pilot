class Content:
  def __init__(self, target: str | None, data: str):
    self.target: str | None = target
    self.content: str = data
    self.meta: dict[str, str] = {}

  def __setitem__(self, key: str, value: str):
    self.meta[key] = value

  def __getitem__(self, key: str) -> str | None:
    if key not in self.meta:
      return None

    return self.meta[key]

