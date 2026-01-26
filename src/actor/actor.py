from typing import Any, Dict, Type
from abc import ABC, abstractmethod

class Performable(ABC):
    def perform_as(self, actor: "Actor") -> None: ...

class Question(ABC):
    @abstractmethod
    def answered_by(self, actor: "Actor") -> Any:
        pass

class Actor:

    def __init__(self, name: str):
        self.name = name
        self._abilities: Dict[Type[Any], Any] = {}

    @classmethod
    def named(cls, name: str) -> "Actor":
        return cls(name)

    def who_can(self, *abilities: Any) -> "Actor":
        for ability in abilities:
            self._abilities[type(ability)] = ability
        return self

    def can(self, *abilities: Any) -> "Actor":
        return self.who_can(*abilities)

    def attempts_to(self, *performables: Performable) -> None:
        for p in performables:
            p.perform_as(self)

    def ask(self, question: Question):
        return question.answered_by(self)

    def using(self, ability_type: Type[Any]) -> Any:
        return self.ability_to(ability_type)

    def ability_to(self, ability_type: Type[Any]) -> Any:
        if ability_type in self._abilities:
            return self._abilities[ability_type]
        # búsqueda flexible por herencia/instancia
        for t, ability in self._abilities.items():
            if issubclass(t, ability_type) or isinstance(ability, ability_type):
                return ability
        raise AttributeError(
            f"Actor '{self.name}' no tiene la habilidad {ability_type.__name__}."
        )
