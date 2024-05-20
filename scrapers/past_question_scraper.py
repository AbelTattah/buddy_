from pprint import pprint
import datetime
from bs4 import BeautifulSoup
import pandas as pd
import requests

loginurl = "https://balme.ug.edu.gh/past.exampapers/index.php?p=member&destination="

secureurl ="https://balme.ug.edu.gh/past.exampapers/index.php?p=member"

logouturl = "https://balme.ug.edu.gh/past.exampapers/index.php?p=member&logout=1"
"""
blob:https://balme.ug.edu.gh/ab3e27b1-7797-4b6b-9711-1cac57b9b64f
blob:https://balme.ug.edu.gh/b241868c-859d-42ba-a9a0-2f826b164476

Open Viewing page info
Link Class= "openPopUp"


Download Button info:
id = "download"
class = "toolbarButton download   "


"""
# sample download link "blob:https://balme.ug.edu.gh/b241868c-859d-42ba-a9a0-2f826b164476"
            # sample file viewing link https://balme.ug.edu.gh/past.exampapers/index.php?p=fstream&fid=11182&bid=11030

payload = {
    "memberID":"11335775",
    "memberPassWord":"1133577509JUN2004",
    "logMeIn":"Login"
}

with requests.session() as s:
    r = s.post(loginurl,data=payload)
    print(r.text)
    l = s.get(logouturl)
    print(l.text)