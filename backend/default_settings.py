# -*- coding: utf-8 -*-

"""
Flask environment configuration
"""

from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = True

# For local development purposes
SESSION_TYPE = "filesystem"

# 'Application (client) ID' of app registration in Azure portal - this value is a GUID
CLIENT_ID = "b0de9fe0-217a-4abb-a793-6be3d0776aab"

# Client secret 'Value' (not its ID) from 'Client secrets' in app registration in Azure portal
CLIENT_CREDENTIAL = "ukU7Q~pS3EEBmxjhOX_7.dx0mQlCHceoyPR0E"

# 'Tenant ID' of your Azure AD instance - this value is a GUID
TENANT_ID = "8ceee26d-f3f2-42a5-8491-a4a7f2fe01f2"
