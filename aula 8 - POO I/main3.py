class User:
  def __init__(self, login: str, passwd: str) -> None:
    self.__login = login
    self.__password = passwd

  @property
  def login(self) -> str:
    return self.__login

  @login.setter
  def login(self, new_login: str) -> None:
    self.__login = new_login

  @property
  def password(self) -> str:
    return self.__password

  @password.setter
  def password(self, new_pass: str) -> bool:
    if len(new_pass) < 4:
      print('your password must be at least 4 digits long')
      return False
    self.__password = new_pass
    print('your password has been changed successfully')
    return True
