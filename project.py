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
    score: int
    best_before: int
    roles: List[Role]


class Progress:
    people: List[Person]
    project: Project
    start: int


class History:
    project: str
    people: List[str]


@dataclass
class Solver:
    step: int
    people: List[Person]

    projects: List[Project]
    progress: List[Progress]

    solvable: bool
    score: int
    day: int
    history: List[History]

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
            prev=self
        )

    def run(self) -> True:

        number = 0
        best = None
        for project in self.get_projects():
            for people in self.get_solvers(project):
                result = self.solve(project, people)

                if result.solvable and (best is None or result.score > best.score):
                    best = result

        if best is None:
            return self.next_day().run()

        return best

    def solve(self, project: Project, people: List[Person]):
        solver = self.copy()
        solver.projects.remove(project)
        solver.progress.append(Progress(project=project, people=people, day=self.day))
        solver.history.append(History(project=project.name, people=[person.name for person in people]))

        return solver.run()

    def next_day(self) -> Solver:
        """ Probalbly obsolete """

        solving = self.copy()
        solving.step += 1
        solving.day += 1
        remove = [
            progress for progress in solving.progress
            if progress.project.duration + progress.start >= solving.day
        ]

        # Todo: calcaulation is not acurate
        for progress in remove:
            solving.score += progress.project.score
            # todo skill people

        solving.progress = [progress for progress in solving.progress if progress not in remove]
        return solving

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


"""
A -> B -> C -> D -> E

E.D.C.B.A
"""
