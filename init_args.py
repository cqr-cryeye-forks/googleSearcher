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
    # [ARGS_FOR_SEARCH_TYPE]-[START]
    parser.add_argument(
        "--dir-listing-vulns", "-dlv",
        help="Use dorks for search potentially vulnerability. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--config-files-exposed", "-cfe",
        help="Use dorks for search config files exposed. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--db-files-exposed", "-dfe",
        help="Use dorks for search db files exposed. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--log-files-exposed", "-lfe",
        help="Use dorks for search log files exposed. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--backup-or-old-files-exposed", "-bfe",
        help="Use dorks for search backup or old files exposed. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--login-page", "-lp",
        help="Use dorks for search login pages. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--sql-errors", "-se",
        help="Use dorks for search SQL errors. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--publicity-exposed-docs", "-ped",
        help="Use dorks for search publicity exposed docs. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--php-info", "-pi",
        help="Use dorks for search php info. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--sgi-files", "-sf",
        help="Use dorks for search sgi files. Only for domain or ip address",
        action="store_true"
    )

    parser.add_argument(
        "--admin-panel", "-ap",
        help="Use dorks for search admin panel. Only for domain or ip address",
        action="store_true"
    )
    # [ARGS_FOR_SEARCH_TYPE]-[END]
    return parser.parse_args()


# "site:<your_site> "

args: argparse.Namespace = init_args()