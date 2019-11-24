# hirez_connect.py is for establishing a session with the
# Smite/Paladins/Realm Royale API and determining how much utilization
# is left
# Could create a function which returns a list of the parameters needed for each call. Each dictionary key is a API call name, such as 'createsession'
# { 'createsession' : ['dev_id','sig','timestamp']} which is used to construct the url for the createsession API call
# here are the functions
# Alternatively, I could just return a link to the API documentation, and people can look it up on their own.


# Also, perhaps this all needs to be remodeled as an object with getters and setters for game, platform, response_format, etc.


from urllib.request import urlopen
import urllib.error
import json
import hashlib
import time

dev_id = '2424'
auth_key = 'CC2DB36A40E9483D9EDD13AAC5CE566A'

HIREZ_API_DOCUMENTATION='https://www.hirezstudios.com/wp-content/themes/hi-rez-studios/pdf/smite-api-developer-guide.pdf'
HIREZ_API_VERSION = {'SMITE': '3.24.0.29040', 'Paladins':'0.0.41.19562'} # PC API Versions, PS4 and XBOX end differently
PACKAGE_NAME = 'Hirez Connect for Python'
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

QUEUES = {
			"SMITE": {
				"Ranked":
				{
					"Duel" : "440",
					"Joust": "450",
					"Conquest": "451",
				},
				"Casual":
				{
					"Assault": "445",
				},
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


def construct_api_url(api_call, api_params, game='SMITE', platform='PC', response_format='json'):
	# api_params_list is all the values needed for the call, starting with the api_name, which are simply put together in order,
	# I think I just wrote the whole function
	url = base_url(game, platform)
	api_params = [api_call + response_format] + api_params
	if 'developerId' in api_params:
		api_params[api_params.index('developerId')] = dev_id
	if 'signature' in api_params:
		api_params[api_params.index('signature')] = get_signature(api_call, get_timestamp())
	if 'timestamp' in api_params:
		api_params[api_params.index('timestamp')] = get_timestamp()

	for param in api_params:
		url = url + '/' + param
	return url

def get_signature(method_name, timestamp):
	# returns a signature hash
	signature = hashlib.md5()
	hash_string = dev_id + method_name + auth_key + timestamp
	signature.update(hash_string.encode())
	# print(signature.hexdigest())
	return signature.hexdigest()

def  make_api_call(api_call, api_params = [], game='SMITE', platform='PC', response_format='json'):
	if validate_endpoint_settings(game, platform, response_format) is not True:
		return None # perhaps an error is more appropriate, but None will do for now

	url = construct_api_url(api_call, api_params, game, platform, response_format)
	print('make_api_call url', url)
	try:
		doc = urlopen(url)
	except: # I should catch the http response error here
		return None
	response = doc.read()
	return response

def get_timestamp():
	#returns timestamp formatted for Hi-Rez API, yyyyMMddHHmmss
	return time.strftime("%Y%m%d%H%M%S", time.gmtime())

def ping (game, platform='PC', response_format='json'):
	# A quick way of validating access to the Hi-Rez API
	response = make_api_call('ping', [], game, platform, response_format)
	return response

def createsession(game, platform='PC', response_format='json'):
	# A required step to Authenticate the developerId/signature for further API use
	params_list = ['developerId', 'signature', 'timestamp']
	result = make_api_call('createsession', params_list, game, platform, response_format)
	if response_format.lower() == 'json':
		session = json.loads(result)['session_id']
	else:
		session = None
	return session # will return a session or None

def testsession(session, game, platform='PC', response_format='json'):
	# A means of validating that a session is established
	params_list = ['developerId', 'signature', session, 'timestamp']
	response = make_api_call('testsession', params_list, game, platform, response_format)
	return response


def gethirezserverstatus(session, game, platform='PC', response_format='json'):
	# Function returns UP/DOWN status for the primary game/platform environments. Data is cached once a minute
	params_list = ['developerId', 'signature', session, 'timestamp']
	response = make_api_call('gethirezserverstatus', params_list, game, platform, response_format)
	if response_format.lower() == 'json':
		status = json.loads(response)[0]['status']
	else:
		status = None
	return status

def getdataused(session, game, platform='PC', response_format='json'):
	params_list = ['developerId', 'signature', session, 'timestamp']
	response = make_api_call('getdataused', params_list, game, platform, response_format)
	return response

#===================================
# Data retrieval methods follow
#===================================

def getgods(session, game, platform='PC', response_format='json', language='1'):
	# Returns all Gods and their various attributes
	params_list = ['developerId', 'signature', session, 'timestamp', language]
	response = make_api_call('getgods', params_list, game, platform, response_format)
	return response

def getitems(session, game, platform='PC', response_format='json', language='1'):
	# Returns all Items and their various attributes
	params_list = ['developerId', 'signature', session, 'timestamp', language]
	response = make_api_call('getitems', params_list, game, platform, response_format)
	return response

def getmatchdetails(session, game, match_id, platform='PC', response_format='json'):
	# Returns the statistics for a particular completed match
	params_list = ['developerId', 'signature', session, 'timestamp', match_id]
	response = make_api_call('getmatchdetails', params_list, game, platform, response_format)
	return response

def getleagueleaderboard(session, game, platform='PC', response_format='json', queue=QUEUES['SMITE']['Ranked']['Duel'], tier='27', season='5'):
	# Returns the top players for a particular league (as indicated by the queue/tier/season parameters)
	params_list = ['developerId', 'signature', session, 'timestamp', queue, tier, season]
	response = make_api_call('getleagueleaderboard', params_list, game, platform, response_format)
	return response

def getmatchidsbyqueue(session, game, platform='PC', response_format='json', queue=QUEUES['SMITE']['Ranked']['Duel'], date='20180831', hour='0'):
	# Lists all Match IDs for a particular match queue for the given time period as indicated by date and hour.
	# If hour is -1 it returns the entire day's Match IDs
	params_list = ['developerId', 'signature', session, 'timestamp', queue, date, hour]
	response = make_api_call('getmatchidsbyqueue', params_list, game, platform, response_format)
	return response



print(ping('SMITE'))
print("")
session = createsession('SMITE', 'PC', 'json')
print(session)
# session = '12F465A042F24FA0B525787352E508B3'
session_active = testsession(session, 'SMITE', 'PC', 'json')
print(session_active)
print("")

data_used = getdataused(session, 'SMITE', 'PC', 'json')
print(data_used)
print("")

server_status = gethirezserverstatus(session, 'SMITE', 'PC', 'json')
print(server_status)
print("")

gods = getgods(session, 'SMITE', 'PC', 'json')
# print(gods)
print("")

items = getitems(session, 'SMITE', 'PC', 'json')
# print(items)
print("")

leaderboard = getleagueleaderboard(session, 'SMITE', 'PC', 'json', QUEUES['SMITE']['Ranked']['Duel'], '26', '5')
# print(items)
print("")

#matchids = getmatchidsbyqueue(session, 'SMITE', 'PC', 'json', QUEUES['SMITE']['Ranked']['Duel'], '20191114', '-1')
#print(matchids)
#print("")

match_id = '980611053'
match = getmatchdetails(session, 'SMITE', match_id)
# print(match)
#print("")
