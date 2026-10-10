

import simpy
import mesa
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from .Agents import ACTIONS, CrewAgent
from .events import EventDirector
from .social import RelationshipGraph
from .Mission import Mission


#Programmable by users

class MissionModel(mesa.Model):
    def __init__(self, agents: list[CrewAgent], env: simpy.Environment):
        super().__init__()
        self.grid = mesa.discrete_space.HexGrid((5, 4), torus=False)
        self.env = env 
        self.schedule = mesa.time.RandomActivation(self)
        
        # Instantiate and add agents to the Mesa scheduler
        for i, agent_info in enumerate(agents_data):
            agent = CrewAgent(unique_id=i, model=self, role=agent_info)
            self.schedule.add(agent)

    def step(self):
        """Advance the Mesa model by one step."""
        self.schedule.step()
         
class Simulation:
    def __init__(self, mission: Mission, agents: list[CrewAgent]):
        self.mission = mission

        self.agents = agents

        self.env = simpy.Enviroment

        self.model = MissionModel(agents , self.env)

        self.env.process(self.clock_mesa_model())

        def clock_mesa_model(self):
            while True:
                self.model.step()
                yield self.env.timeout(1)

        def run(self):
            print(f"Starting Mission: {self.mission.name}")
            self.env.run(until=self.mission.duration)
            print("Mission Complete.")
