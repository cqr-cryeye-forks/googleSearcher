import ast
import dataclasses
import json
import random
from typing import TypedDict, NamedTuple, ClassVar

from init_args import args


class AuthDataDict(TypedDict):
    api_key: str
    case_id: str


class AuthData(NamedTuple):
    api_key: str
    case_id: str


@dataclasses.dataclass
class AuthDataStorage:
    _items: list[AuthData]

    _used_items: list[AuthData] = dataclasses.field(default_factory=list)
    _amount_of_rotations: int = dataclasses.field(default=0)
    MAX_AMOUNT_OF_ROTATIONS: ClassVar[int] = 1

    @classmethod
    def from_dicts(cls, data: list[AuthDataDict]):
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
                count += 1
                continue
            items.append(verified_item)

        if not items:
            raise ValueError(f'Auth data not provided. Candidates "{len(data)}. Failed: {count}"')

        return cls(_items=items)

    def _get_message_about_keys(self) -> str:
        return f"Keys remains: {len(self._items)}/{len(self._items) + len(self._used_items)}."

    def get_random_auth_data_or_none(self) -> AuthData | None:
        """
        Try to get auth_data.
        When get it, move it to "used".

        If we used all data, then check, if we can to try to use all this data again.
        If yes, then move all data from "used" to "items". And try to get data again.

        Return None, if we can't provide any auth data.
        """
        message__keys = self._get_message_about_keys()

        print(message__keys)

        if len(self._items) == 0:
            message__rotation = f"Rotation: {self._amount_of_rotations}/{self.MAX_AMOUNT_OF_ROTATIONS}."
            if self._amount_of_rotations >= self.MAX_AMOUNT_OF_ROTATIONS:
                print(f"All keys are used. Can't use them again. {message__rotation} {message__keys}")
                return None

            print(f"All keys are used. Try to use them again. {message__rotation} {message__keys}")
            self._items.extend(self._used_items)
            self._amount_of_rotations += 1

        max_index = len(self._items) - 1
        random_index = random.randint(0, max_index)
        used_auth_data = self._items.pop(random_index)
        self._used_items.append(used_auth_data)

        print(f'{self._get_message_about_keys()}')

        return used_auth_data


def init_auth_data_storage() -> AuthDataStorage:
    file_with_keys = args.api_keys_file
    keys_dict: list[AuthDataDict] = json.loads(file_with_keys.read_text())

    return AuthDataStorage.from_dicts(data=keys_dict)
