"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

import mod_wsgi.server

mod_wsgi.server.start(
  '--log-to-terminal',
  '--log-level', 'info',
  '--access-log',
  '--port', '8080',
  '--trust-proxy-header', 'X-Forwarded-For',
  '--trust-proxy-header', 'X-Forwarded-Port',
  '--trust-proxy-header', 'X-Forwarded-Proto',
  '--application-type', 'module',
  '--entry-point', 'wsgi',
  '--inactivity-timeout', '60',
  '--url-alias', '/ws/healthz/', '/opt/app-root/src/LICENSE'
)
