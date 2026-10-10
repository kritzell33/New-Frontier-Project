from dataclasses import dataclass
import mesa

class Hardware:
    name: str
    size: int
    location: int
    classification: int
    repair_knowledge_type: int