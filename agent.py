import csv
import json
import os
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List

PRIORITY_MAP = {"low": 1, "medium":2, "high":3}
BUFFER_MINUTES = 10

@dataclass
class Event:
    title:str
    start:datetime
    end:datetime
    priority: int
    event_type: str
    flexible: bool
    
def read_calendar(path = "calendar.csv") -> List[Event]:
    events =[]
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            events.append(Event(
                
            ))
    
    
    return sorted

def detect_conflicts(events: List[Event]):
    conflicts =[]
    
def main():
    events = read_calendar()
    conflicts = detect_conflicts(events)
    
    with open("conflicts.json", "w", encoding="utf-8") as f:
        json.dump(conflicts,f ,indent=2)
    

if __name__ = "__main__":
    main()