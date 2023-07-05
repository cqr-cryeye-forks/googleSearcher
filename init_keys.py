import ast
import dataclasses
import json
import random
from typing import TypedDict, NamedTuple

from init_args import args

class AuthDataDict(TypedDict):
    api_key:str
    case_id:str

class AuthData(NamedTuple):
    api_key:str
    case_id:str


@dataclasses.dataclass
class AuthDataStorage:
    _items: list[AuthData]

    @classmethod
    def from_dicts(cls, data:list[AuthDataDict]):
        items = []
        count = 0
        for auth_data_as_dict in data:
            try:

                verified_item = AuthData(
                    api_key=auth_data_as_dict["api_key"],
                    case_id=auth_data_as_dict["case_id"]
                )

                # TODO ? Use better exception info?
                # raise ValueError("No API key provided")
                # raise ValueError("No search engine id provided")
            except KeyError:
                count+=1
                continue
            items.append(verified_item)

        if not items:
            raise ValueError(f'Auth data not provided. Candidates "{len(data)}. Failed: {count}"')

        return cls(_items=items)

    def get_random_auth_data(self)->AuthData:
        return random.choice(self._items)

def init_auth_data_storage()->AuthDataStorage:
    file_with_keys = args.api_keys_file
    keys_dict: list[AuthDataDict] = json.loads(file_with_keys.read_text())

    return AuthDataStorage.from_dicts(data=keys_dict)
