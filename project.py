from dataclasses import dataclass
from typing import List


@dataclass
class Role:
    name: str
    level: int


@dataclass
class Person:
    name: str
    role: List[Role]


class Project:
    name: str
    duration: int
    best_before: int
    roles: List[Role]


@dataclass
class Solver:
    step: int
    projects: List[Project]
    people: List[Person]
    solvable: bool

    def __init__(self, people: List[Person], projects: List[Project]):
        pass

    def next(self) -> Solver:
        pass

    def next_day(self) -> Solver:
        pass

    def run(self, project: Project, people: List[Person]) -> Solver:

        return Solver()

    def get_project(self):
        pass
