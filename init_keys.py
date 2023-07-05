import ast
import json

from init_args import args


def init_keys():
    file_with_keys = args.api_keys_file
    keys_dict: list[dict[str, str]] = json.loads(file_with_keys.read_text())
    keys_set = {str(item) for item in keys_dict}
    random_keys = keys_set.pop()
    return ast.literal_eval(random_keys)
