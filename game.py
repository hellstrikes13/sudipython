class Scene(object):
 def enter(self):
  pass

class Engine(object):
 def __init__(self,scene_map):
  pass
 def play(self):
  pass

class Death(scene):
 def enter(self):
  pass
class central_corridor(scene):
 def enter(self):
  pass
class LaserWeaponArmory(scene):
 def enter(self):
  pass
class TheBridge(scene):
 def enter(self):
  pass
class EscapePod(scene):
 def enter(self):
  pass

class Map(object):
 def __init__(self,start_scene):
  pass
 def __init__(self,scene_name):
  pass
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
