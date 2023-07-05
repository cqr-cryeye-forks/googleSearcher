import argparse
import pathlib


def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--searchTerm", help="Enter a search term!")
    parser.add_argument("-n", "--numResults", type=int, default=10,
                        help="Enter the number of results to fetch (max 100)")
    parser.add_argument("-p", "--page", type=int, default=1, help="Enter the page number")
    parser.add_argument(
        "--api-keys-file",
        type=pathlib.Path,
        help="Path to json file with api keys and case IDs. {'api_key': <some_key>, 'case_id': <some_case_id>}"
    )
    parser.add_argument("--output", type=pathlib.Path, help="Path to write output in json format")

    return parser.parse_args()


args: argparse.Namespace = init_args()