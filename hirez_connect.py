# hirez_connect.py is for establishing a session with the
# Smite/Paladins/Realm Royale API and determining how much utilization
# is left

from urllib.request import urlopen
import urllib.error
import json
import hashlib

dev_id = '2424'
auth_key = 'CC2DB36A40E9483D9EDD13AAC5CE566A'

PACKAGE_NAME = 'SMITE Duel Helper'
REPOSITORY_HOME = 'http://github.com/djmartz77/SMITEDuelHelper'
DEFAULT_RESPONSE_FORMAT = 'json'
DEBUG_MODE = True

ENDPOINTS = {
				"SMITE":
				{
					'PC' : 'http://api.smitegame.com/smiteapi.svc',
					'XBOX' : 'http://api.xbox.smitegame.com/smiteapi.svc',
					'PS4': 'http://api.ps4.smitegame.com/smiteapi.svc'
				},
				"PALADINS":
				{
					'PC' : 'http://api.paladins.com/paladinsapi.svc',
					'XBOX' : 'http://api.xbox.paladins.com/paladinsapi.svc',
					'PS4' : 'http://api.ps4.paladins.com/paladinsapi.svc'
				}
			}

def validate_endpoint_settings(game, platform, response_format):
	if response_format.lower() == 'xml' :
		print('xml is not supported by',PACKAGE_NAME,'yet')
		print('Of course, a pull request for xml support would be quite welcome!')
		print(REPOSITORY_HOME)
		return False
	elif response_format.lower() == 'json':
		# placeholder to allow else
		pass
	else:
		print('the Hirez Studios API currently supports only xml and json')
		print('If you believe this is in error, please submit an issue or pull request')
		print(REPOSITORY_HOME)
		return False

	if game.upper() != 'SMITE' and game.upper() != 'PALADINS':
		print(game.upper(), 'is not supported')
		print('only SMITE and PALADINS are supported by',PACKAGE_NAME + "'s ping() method")
		print('Of course, a pull request is always welcome!')
		print(REPOSITORY_HOME)
		return False

	return True

def base_url(game, platform):
	# should I validate here?
	url = ENDPOINTS[game.upper()][platform.upper()]
	return url


def ping (game, platform='PC', response_format='json'):
	if validate_endpoint_settings(game, platform, response_format):
		url = base_url(game, platform) + '/ping' + response_format.lower() 
		doc = urlopen(url)
		html = doc.read()
		return html
	else:
		return None

def testsession(session):
	# A means of validating that a session is established
	return None #placeholder

def createsession(game, platform='PC', response_format='json'):
	# A required step to Authenticate the developerId/signature for further API use
	return None # will return a session or None

def gethirezserverstatus(session):
	# Function returns UP/DOWN status for the primary gmae/platform environments. Data is cached once a minute
	return None # will return status object 

print(ping('SMITE','PC','json'))

