'''
Advanced Libraries
dataclasses for Structured Data
Simplify data class creation.

Example:
'''

from dataclasses import dataclass

@dataclass
class DataPoint:
    x: float
    y: float
    label: str

point = DataPoint(1.0, 2.0, 'positive')
print(point)