import sqlparse

from flask import Blueprint
from flask_sqlalchemy import get_debug_queries

from pygments import highlight
from pygments.lexers.sql import SqlLexer
from pygments.formatters import HtmlFormatter

import jinja2

bp = Blueprint("sql", __name__)

LAST_SQL = []


FORMAT = jinja2.Template("{% for sql, params in formatted %}<p><code>{{ sql | safe }}</code></p>{% endfor %}")


def replace_all(s: str, replacements):
    if not replacements:
        return s

    return replace_all(s.replace("?", repr(replacements[0]), 1), replacements[1:])


@bp.route("/sql")
def sql():
    formatter = HtmlFormatter(style="default")

    if not LAST_SQL:
        return "No requests yet... make one."

    formatted = []

    for statement in LAST_SQL:
        format_sql = sqlparse.format(replace_all(statement.statement, statement.parameters), reindent_aligned=True)
        highlighted = highlight(format_sql, SqlLexer(), formatter)

        formatted.append(
            (highlighted,
             statement.parameters))

    style_tag = "<style>" + formatter.get_style_defs() + "</style>"

    return style_tag + FORMAT.render(formatted=formatted)


@bp.after_app_request
def store_sql_debug(rq):
    global LAST_SQL
    LAST_SQL = get_debug_queries()

    return rq
