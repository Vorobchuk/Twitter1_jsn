import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl


def json_crt(acct):
    """
    Function creates json file
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    print('')

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '10'})
    connection = urllib.request.urlopen(url, context=ctx)
    return connection


def json_read(connection, info):
    """
    (str,str) -> lst
    Returns lst with certain information
    """
    lst = []
    data = connection.read().decode()
    js = json.loads(data)
    for u in js['users']:
        if (info not in u) or (info == ""):
            lst.append([u['name'], '* No such info'])
            continue
        lst.append([u['name'], u[info]])
    return lst


def main():
    """
    This is the main function
    """
    acct = input('Enter Twitter Account: ')
    info = input('What do you want to see? ')
    connection = json_crt(acct)
    lst = json_read(connection, info)
    for el in lst:
        print(el[0], "->", el[1])


main()