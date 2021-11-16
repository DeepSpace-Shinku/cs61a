
"""
>>> import ants, importlib
>>> importlib.reload(ants)
>>> beehive = ants.Hive(ants.AssaultPlan())
>>> dimensions = (2, 9)
>>> gamestate = ants.GameState(None, beehive, ants.ant_types(),
...         ants.dry_layout, dimensions)
>>> ants.bees_win = lambda: None
>>> # QueenAnt Placement
>>> queen = ants.QueenAnt()
>>> impostor = ants.QueenAnt()
>>> front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
>>> tunnel = [gamestate.places['tunnel_0_{0}'.format(i)]
...         for i in range(9)]
>>> tunnel[1].add_insect(back_ant)
>>> tunnel[7].add_insect(front_ant)
>>> tunnel[4].add_insect(impostor)
>>> impostor.action(gamestate)
>>> impostor.armor            # Impostors must die!
0
>>> tunnel[4].ant is None
True
>>> back_ant.damage           # Ants should not be buffed
1
>>> front_ant.damage
1
>>> tunnel[4].add_insect(queen)
>>> queen.action(gamestate)
"""
