
#!/bin/bash

from subprocess import PIPE, Popen
from sys import exit
import json

# Regular
txtblk='\033[30m' # Black
txtred='\033[31m' # Red
txtgrn='\033[32m' # Green
txtylw='\033[33m' # Yellow
txtblu='\033[34m' # Blue
txtpur='\033[35m' # Purple
txtcyn='\033[36m' # Cyan
txtwht='\033[0m' # White

endpnts = ['Teams','News','Standings','Scores','Schedule',
           'Videos','Stats','AllGames','FAQ','Terms_and_Info','Home']

base_url='https://audl-stat-server.herokuapp.com/aa/'

def print_test(url):
        print txtylw + "Testing endpoint "+ url + txtwht

def print_test_outcome(err_val):
        if err_val:
            print txtred + "ERROR" + txtwht
        else:
            print txtgrn + "SUCCESS" + txtwht

def invalid_data(response):
    if len(response) <= 0:
        return 1
    elif response.lower().find("not a valid path") is not -1:
        return 1
    elif response.lower().find("N/A") is not -1:
        return 1
    elif response.lower().find("N/A") is not -1:
        return 1
    else:
        return 0

    
# makes sure the endpoint can be read and the response interpreted as json
def test_url(url):
    print_test(url)
    p = Popen(['curl',url], stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    if p.returncode != 0:
        return 1, None
    if invalid_data(output):
        return 1, None
    
    #parse whatever came out of the request (should be json)
    try:
        data = json.loads(output)
    except:
        return 1

    return 0, data

def main():
    ret_val = 0
    #check each of the main endpoints of the server
    for pnt in endpnts:
        url=base_url+pnt
        result, data = test_url(url)
        print_test_outcome(result)
        ret_val += result

        # TEAMS Endpiont Testing
        if None is not data:
            if "Teams" == pnt:
                for team in data:
                    team_id = str(team[1])
                    team_url = base_url+pnt+'/'+team_id
                    #test main team page
                    result, team_data = test_url(team_url)
                    print_test_outcome(result)
                    ret_val += result
                    for game in team_data[1][2:]: #this is why the server is bad
                        #test team scores page
                        date = str(game[0])
                        result, dum = test_url(base_url+'Game/'+team_id+'/'+date)
                        print_test_outcome(result)
                        ret_val += result
                    

    if ret_val:
        print txtred + "Error returned when checking " + ret_val + " endpoints." + txtwht
        
    return ret_val


if __name__ == "__main__":
    err = main()
    exit(err)
