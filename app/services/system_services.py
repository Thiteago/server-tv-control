import os

class SystemController:
  @staticmethod
  def shutdown():
    os.system('shutdown /s /t 1')

  @staticmethod
  def schedule_shutdown(minutes):
    os.system(f'shutdown /s /t {minutes * 60}')

  @staticmethod
  def cancel_shutdown():
    os.system('shutdown /a')