from dataclasses import dataclass
from src.exceptions import (
    UserAlreadyInSubject,
    UserNotInSubject,
)


@dataclass
class Subject:
    name: str
    description: str
    users_registered: list

    def add_user(self, user):
        if user in self.users_registered:
            raise UserAlreadyInSubject
        self.users_registered.append(user)
        return self

    def delete_user(self, user):
        if user not in self.users_registered:
            raise UserNotInSubject
        self.users_registered.remove(user)
        return self

    def add_description(self, description):
        self.description = description
        return self
