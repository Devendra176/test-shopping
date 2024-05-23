from flask import Blueprint, current_app
from flask.cli import with_appcontext

from simple_flask.core.db_conf import get_db, parse_sql_script

admin_command_bp = Blueprint('admin-command',
                             __name__, cli_group='db-cmd')


@admin_command_bp.cli.command('init_db')
@with_appcontext
def run_sql():
    parse_sql_script()
    print(f"DB Created")
