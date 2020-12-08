# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

from dataclasses import dataclass

@dataclass
class User(object):
    name: str
    user_id: int
    just_join: bool = True

    def get(self, name):
        self.name = name
        print(self.name)


user = User('Bob', 56)
user.get('Fox')
