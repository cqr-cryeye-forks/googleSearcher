# !/usr/bin/env python3
import json

from googleapiclient.discovery import build
import pathlib
from typing import Final

from constants import START_PAGE
from init_args import args
from init_keys import init_keys

my_keys = init_keys()
my_api_key = my_keys.get("api_key")
my_cse_id = my_keys.get("case_id")

if not my_api_key:
    raise ValueError("No API key provided")

if not my_cse_id:
    raise ValueError("No search engine id provided")


def google_search(search_term, api_key, cse_id, num_results, start_page=1, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    try:
        res = service.cse().list(q=search_term, cx=cse_id, num=num_results, start=start_page, **kwargs).execute()
        return res['items']
    except Exception as e:
        print("An error occurred during the search:", e)
        return []


searchTerm = args.searchTerm
numResults = min(args.numResults, 100)  # Ensure the number of results is capped at 100

# Find results for the specified page
results = google_search(
    searchTerm, my_api_key, my_cse_id, num_results=min(numResults, 10), start_page=START_PAGE)
result_to_write = []
if len(results) == 0:
    result_to_write.append(
        {
            "title": "Nothing found",
            "source": "Nothing found",
            "snippet": "Nothing found",
        }
    )
else:
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
