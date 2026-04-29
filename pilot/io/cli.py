from subprocess import run

from langex.core.classes import implements

from pilot.io.base import BaseIO

@implements(BaseIO)
class CliIO:
  def __init__(self, command):
    self.command = command

  def get_input(self, context=None):
    result = run(
      self.command + ([context] if context else []),
      capture_output=True,
      text=True
    )

    return result.stdout.strip()

  def push_output(self, content):
    if not self.proc.stdin:
      return

    self.proc.stdin.write(content + "\n")
    self.proc.stdin.flush()

