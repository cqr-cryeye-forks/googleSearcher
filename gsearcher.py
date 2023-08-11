# !/usr/bin/env python3
import json
import pathlib
from typing import Final

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from constants import START_PAGE
from dork_storage import DORK_FOR_DIR_LIST_VULN, DORK_FOR_CONFIG_FILE_SEARCH, DORK_FOR_DB_FIES_EXPOSED, \
    DORK_FOR_LOG_FIES_EXPOSED, DORK_FOR_BACKUP_FIES_EXPOSED, DORK_FOR_SEARCH_LOGEN_PAGES, DORK_FOR_SEARCH_SQL_ERRORS, \
    DORK_FOR_SEARCH_PUBLICITY_EXPOSED_DOCS, DORK_FOR_SEARCH_PHP_INFO, DORK_FOR_SEARCH_CGI_FILES, DORK_FOR_ADMIN_PANEL, \
    DORK_FOR_SEARCH_PASSWORDS
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

        service = build(
            "customsearch",
            "v1",
            developerKey=auth_data.api_key,
        )

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
        except KeyError:
            print("No results")
            return


def main():
    searchTerm = args.searchTerm

    if args.dir_listing_vulns:
        searchTerm = f"site:{searchTerm} {DORK_FOR_DIR_LIST_VULN}"

    elif args.config_files_exposed:
        searchTerm = f"site:{searchTerm} {DORK_FOR_CONFIG_FILE_SEARCH}"

    elif args.db_files_exposed:
        searchTerm = f"site:{searchTerm} {DORK_FOR_DB_FIES_EXPOSED}"

    elif args.log_files_exposed:
        searchTerm = f"site:{searchTerm} {DORK_FOR_LOG_FIES_EXPOSED}"

    elif args.backup_or_old_files_exposed:
        searchTerm = f"site:{searchTerm} {DORK_FOR_BACKUP_FIES_EXPOSED}"

    elif args.login_page:
        searchTerm = f"site:{searchTerm} {DORK_FOR_SEARCH_LOGEN_PAGES}"

    elif args.sql_errors:
        searchTerm = f"site:{searchTerm} {DORK_FOR_SEARCH_SQL_ERRORS}"

    elif args.publicity_exposed_docs:
        searchTerm = f"site:{searchTerm} {DORK_FOR_SEARCH_PUBLICITY_EXPOSED_DOCS}"

    elif args.php_info:
        searchTerm = f"site:{searchTerm} {DORK_FOR_SEARCH_PHP_INFO}"

    elif args.sgi_files:
        searchTerm = f"site:{searchTerm} {DORK_FOR_SEARCH_CGI_FILES}"

    elif args.admin_panel:
        searchTerm = f"site:{searchTerm} {DORK_FOR_ADMIN_PANEL}"

    elif args.search_passwords:
        searchTerm = f"site:{searchTerm} {DORK_FOR_SEARCH_PASSWORDS}"

    numResults = min(args.numResults, 100)  # Ensure the number of results is capped at 100

    # Find results for the specified page
    results = google_search(
        search_term=searchTerm,
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
                    "snippet": result.get("snippet"),
                    "search_term": searchTerm,
                }
            )

    ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parent
    path_to_write_output: pathlib.Path = ROOT_PATH.joinpath(args.output)
    path_to_write_output.write_text(json.dumps(result_to_write))


if __name__ == "__main__":
    main()
