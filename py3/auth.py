'''
Authorization flow:
1. Start local web server to await redirect
2. Spawn web browser redirecting to auth server
3. Get auth code from URL query param after auth server redirects to local web server
4. Exchange auth code for access and refresh token
5. Save refresh token to keep user logged in
6. Kill local web server
7. Kill web browser window
'''

from authlib.integrations.requests_client import OAuth2Session
from flask import Flask, request
from authlib.oauth2.rfc7636 import create_s256_code_challenge
import threading
import webbrowser
import time
import secrets
import os
import sys

flask_app = Flask(__name__)
try:
    client_id = os.environ["OW4_SSO_CLIENT_ID"]
except KeyError:
    print("ERROR: Missing environment variable OW4_SSO_CLIENT_ID")
    sys.exit(1)
oauth_access_token = None
scope = "openid profile onlineweb4"
code_verifier = secrets.token_urlsafe()
code_challenge = create_s256_code_challenge(code_verifier)
authorize_url = "https://online.ntnu.no/openid/authorize"
session = OAuth2Session(
    client_id,
    scope=scope,
    redirect_uri="http://127.0.0.1:7777",
    response_type="code")


def getAuthorizedUser():
    global oauth_access_token
    thread = ServerThread()
    thread.daemon = True
    thread.start()
    uri, state = session.create_authorization_url(
        authorize_url,
        code_challenge=code_challenge,
        code_challenge_method="S256")
    webbrowser.open_new(uri)
    while oauth_access_token is None:
        time.sleep(0.2)
    return oauth_access_token


@flask_app.route("/")
def recieveAccessToken():
    global oauth_access_token
    global client_id
    access_url = "https://online.ntnu.no/openid/token"
    token = session.fetch_access_token(
        access_url,
        authorization_response=request.url,
        code_verifier=code_verifier)
    oauth_access_token = token
    return "{}"


class ServerThread(threading.Thread):
    def init(self):
        threading.Thread.__init__(self)

    def run(self):
        flask_app.run(
            port=7777,
            host="localhost"
        )
