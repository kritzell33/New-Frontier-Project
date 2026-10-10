from dataclasses import dataclass
import mesa

@dataclass
class Mission:
    designation: str
    length: int
    crewmodule: str
    onboard_science_experiments_per_mission: int
    eva_experiments_per_mission: int
    landing_zone: str
    space_station_workdays: int
    surface_experiments: int

class Experiment:
    name: str
    knowledge_type: int
    deadline_day: int
    hardware: Hardware
    assigned_to: str