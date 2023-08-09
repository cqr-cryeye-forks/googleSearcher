DORK_FOR_DIR_LIST_VULN = "intitle:index.of"

DORK_FOR_CONFIG_FILE_SEARCH = "ext:xml |" \
                             " ext:conf |" \
                             " ext:cnf |" \
                             " ext:reg |" \
                             " ext:inf |" \
                             " ext:rdp |" \
                             " ext:cfg |" \
                             " ext:txt |" \
                             " ext:ora |" \
                             " ext:ini"


DORK_FOR_DB_FIES_EXPOSED = "ext:sql | ext:dbf | ext:mdb"

DORK_FOR_LOG_FIES_EXPOSED = "ext:log"

DORK_FOR_BACKUP_FIES_EXPOSED = "ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"

DORK_FOR_SEARCH_LOGEN_PAGES = "inurl:login"

DORK_FOR_SEARCH_CGI_FILES = "ext:cgi"

DORK_FOR_SEARCH_PHP_INFO = 'ext:php intitle:phpinfo "published by the PHP Group"'

DORK_FOR_SEARCH_PUBLICITY_EXPOSED_DOCS = "ext:doc |" \
                              " ext:docx |" \
                              " ext:odt |" \
                              " ext:pdf |" \
                              " ext:rtf |" \
                              " ext:sxw |" \
                              " ext:psw |" \
                              " ext:ppt |" \
                              " ext:pptx |" \
                              " ext:pps |" \
                              " ext:csv"

DORK_FOR_SEARCH_SQL_ERRORS = 'intext:"sql syntax near" |' \
                             ' intext:"syntax error has occurred" |' \
                             ' intext:"incorrect syntax near" |' \
                             ' intext:"unexpected end of SQL command" |' \
                             ' intext:"Warning: mysql_connect()" |' \
                             ' intext:"Warning: mysql_query()" |' \
                             ' intext:"Warning: pg_connect()"'