import os
import pprint
from urllib.parse import urlencode

import requests

BEARER = os.getenv('BEARER_KEY')

# query = input('What is your question today')
query = 'what is the total sales for last year'


def get_url():
    print(BEARER)
    params = urlencode(dict(v=20170712, query=query, lang='en', sessionId=1))
    url = 'https://api.dialogflow.com/v1/query?{0}'.format(params)
    return requests.get(url, headers={'Authorization': BEARER}).json()['result']


def extract_parameter():
    response = get_url()
    pprint.pprint(response)
    aggregate = response['parameters']['aggregate']
    command = response['parameters']['command']
    # date = response['parameters']['date']
    date = str(response['parameters']['date-period'])
    fields = response['parameters']['fields']
    sql_command = 'select ' + aggregate + ' ' + command + ' of ' + ' from ' + fields + ' where ' + str(date)
    print(sql_command)


# $command $aggregate $ fields from table
# where period < [resu]
# sql_list
#
# sql_list.append()

# def operations():
#     session_client = dialogflow.SessionsClient()


extract_parameter()
