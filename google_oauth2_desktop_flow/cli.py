import os
import click
from google_oauth2_desktop_flow.tokens import get_tokens

DEFAULT_CLIENT_SECRET_PATH = os.path.expanduser('~/.goauth/oauth_client_secret.json')


@click.command()
@click.option('-s', '--scopes', required=True, multiple=True, type=str)
@click.option('-c', '--client-secret-path', default=DEFAULT_CLIENT_SECRET_PATH)
def main(scopes, client_secret_path):
    return get_tokens(scopes, client_secret_path)
