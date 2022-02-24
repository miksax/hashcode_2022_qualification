from dataclasses import dataclass
from typing import List


@dataclass
class Role:
    name: str
    level: int


@dataclass
class Person:
    name: str
    roles: List[Role]


class Project:
    name: str
    duration: int
    best_before: int
    roles: List[Role]


class Progress:
    people: List[Person]
    project: Project
    start: int


@dataclass
class Solver:
    step: int
    people: List[Person]

    projects: List[Project]
    progress: List[Progress]

    solvable: bool
    score: int
    day: int

    def __init__(self, people: List[Person], projects: List[Project]):
        pass

    def copy(self):
        Solver(
            step=self.step,
            projects=self.projects,
            people=[
                Person(
                    name=person.name,
                    roles=[
                        Role(name=role.name, level=role.level)
                        for role in person.roles
                    ]
                )
                for person in self.people
            ],
            progress=self.progress,
            solvable=self.solvable,
            score=self.score,
            day=self.day,
        )

    def run(self) -> Solver:

        best = None
        for solving in self.next():
            result = solving.run()
            if best is None or result.score > best and result.solvable:
                best = result

        if best is not None:
            return best

        self.solvable = False
        return self

    def next_day(self) -> Solver:
        """ Probalbly obsolete """

        return self.copy()

    def next(self,) -> Solver:
        """ will pick up project and pepople """
        # project: Project, people: List[Person]
        solving = self.copy()
        solving.step += 1 #etc.
        return solving

    def get_projects(self) -> Generator[Project]:
        """
        Return projects what is possible to work on
        """

    def get_solvers(self, project: Project) -> Generator[List[Person]]:
        """
        Get sovlers what can work on project
        """
        for person in self.get_free_people():
            person

        return []

    def get_free_people(self):
        pass
