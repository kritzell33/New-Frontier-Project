from dataclasses import dataclass
import mesa

class Task:
    name: str
    kind: str
    effort_remaining: float
    created_0015: float
    deadline_0015: float | None = None   
    urgency = int
    completed_0015: float | None = None
    multi = bool
    claimed_by: str | None = None
    also_claimed_by: str | None = None  
