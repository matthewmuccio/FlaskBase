#!/usr/bin/env python3


from core.models import mapper
from core.models import wrapper


# Creates an account in users database table.
def create_account(username, password):
	return mapper.create_account(username, password)

# Logs in to account in users database table.
def login(username, password):
	return mapper.login(username, password)