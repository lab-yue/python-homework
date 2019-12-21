from . import const

class Math:

  @staticmethod
  def circleArea(r: float):
    return const.τ * r ** r / 2

if __name__ == '__main__':
  print(Math.circleArea(2))