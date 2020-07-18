import requests
from bs4 import BeautifulSoup
import pandas
import os
import time

url='https://www.cricbuzz.com/'
headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
"cookie": "G_ENABLED_IDPS=google; _ga=GA1.2.1132177184.1503645060; __cfduid=da8ef895dbf63eaa35358dd63bbced82f1535638413; __utma=75638727.1132177184.1503645060.1518098925.1537716125.5; cb_config=%7B%7D; cbzads=IN|AS|02|Hyderabad; _gid=GA1.2.1065870403.1559484418; pc=2",
"referer": "https://www.cricbuzz.com/",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

def matchScores():
    res = requests.get("https://www.cricbuzz.com/", headers = headers)
    soup = BeautifulSoup(res.text,"html.parser")

    listOfMatches = soup.find("div",{"class":"cb-col-100 cb-col cb-hm-scg-blk "})

    matches = listOfMatches.findAll("div", {"class":"cb-col cb-col-25 cb-mtch-blk"})
    lines = []

    for match in matches:
        line = ''
        currentTeamScore = match.findAll("div",{"class":"cb-hmscg-bat-txt cb-ovr-flo "})
        line = line + currentTeamScore[0].text +"\n"
        try:
            defendingTeamScore = match.find("div",{"class":"cb-hmscg-bwl-txt "})
            line = line + defendingTeamScore.text + "\n"
        except:
            line = line + currentTeamScore[1].text + "\n"

        try:
            scoreToWin = match.find("div",{"class":" cb-ovr-flo cb-text-live"})
            line = line + scoreToWin.text + "\n"
        except:
            try:
                scoreToWin = match.find("div",{"class":"cb-ovr-flo cb-text-preview ng-binding"})
                line = line + scoreToWin.text + "\n"
            except:
                try:
                    scoreToWin = match.find("div",{"class":" cb-ovr-flo cb-text-complete"})
                    line = line + scoreToWin.text
                except:
                    line = line +"Match yet to be started!" + "\n"
				# try:
				# 	scoreToWin = match.find("div",{"class":" cb-ovr-flo cb-text-complete"})
				# 	line = line + scoreToWin.text + "\n"
				# except:
				# 	line = line +"Match yet to be started!" + "\n"
        lines.append(line)

    return lines
