import requests
from datetime import datetime


nameK = "kaufland" + datetime.now().strftime("%W") + ".pdf"




url = 'https://leaflets.kaufland.com/de/kdz/1960/d46/GetPDF.ashx'
r = requests.get(url, allow_redirects=True)

open(nameK, 'wb').write(r.content)



