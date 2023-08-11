DORK_FOR_DIR_LIST_VULN = "intitle:index.of"


DORK_FOR_ADMIN_PANEL = "intitle:login | intext:login | inbody:login inurl:*admin* | inurl:*administrator*"

DORK_FOR_SEARCH_PASSWORDS = "ext:env |" \
                            " ext:json |" \
                            " ext:txt |" \
                            " ext:cfg |" \
                            " ext:yaml |" \
                            " ext:yml |" \
                            " ext:php |" \
                            " ext:doc |" \
                            " ext:pcf |" \
                            " ext:pwd |" \
                            " ext:pem |" \
                            " ext:log |" \
                            " ext:xml |" \
                            " ext:pdf |" \
                            " ext:bashrc |" \
                            " ext:pgpass |" \
                            " ext:htpasswd |" \
                            " ext:exs" \
                            " inurl:*pass* |" \
                            " inurl:*pwd*"

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


DORK_FOR_DB_FIES_EXPOSED = "ext:sql | ext:db | ext:dbf | ext:mdb | ext:sql.gz | ext:sql.gz | ext:db.gz | ext:db.gz"

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

DORK_FOR_SEARCH_ADMIN_PANEL = 'inurl:/admin.aspx |' \
                              ' inurl:adminhome.asp |' \
                              ' inurl:admin/login.asp |' \
                              ' inurl:admin_login.asp |' \
                              ' inurl:administrator_login.asp |' \
                              ' inurl:administratorlogin.asp |' \
                              ' inurl:adminlogin.asp |' \
                              ' inurl:login/admin.asp |' \
                              ' inurl:login/administrator.asp |' \
                              ' inurl:*admin_login.php |'
x=1