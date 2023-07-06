# !/usr/bin/env python3
import json

from googleapiclient.discovery import build
import pathlib
from typing import Final

from googleapiclient.errors import HttpError

from constants import START_PAGE
from init_args import args
from init_keys import init_auth_data_storage


def google_search(search_term, num_results, start_page=1, **kwargs):
    auth_data_storage = init_auth_data_storage()
    amount_of_try = 20
    while amount_of_try:
        auth_data = auth_data_storage.get_random_auth_data_or_none()

        if auth_data is None:
            # TODO: think about smarter way to message about invalid api keys to des
            raise ValueError("All provided keys are invalid!")

        service = build("customsearch", "v1", developerKey=auth_data.api_key)
        try:
            res = service.cse().list(
                q=search_term,
                cx=auth_data.case_id,
                num=num_results,
                start=start_page,
                **kwargs
            ).execute()
            return res['items']

        except HttpError as e:
            print("An error occurred during the search:", e)
            amount_of_try -= 1
            continue


def main():
    searchTerm = args.searchTerm
    numResults = min(args.numResults, 100)  # Ensure the number of results is capped at 100

    # Find results for the specified page
    results = google_search(
        searchTerm,
        num_results=min(numResults, 10),
        start_page=START_PAGE,
    )
    result_to_write = []
    if results:
        for result in results:
            print(result['link'])
            result_to_write.append(
                {
                    "title": result["title"],
                    "source": result["link"],
                    "snippet": result["snippet"],
                }
            )

    ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parent
    path_to_write_output: pathlib.Path = ROOT_PATH.joinpath(args.output)
    path_to_write_output.write_text(json.dumps(result_to_write))


if __name__ == "__main__":
    main()
