import requests as req
from datetime import datetime
import time

# Paste links column within t
t = """www.example.com
www.example.com/anotherLink"""

# Get links into a list
links = t.split("\n")

# Preview links list
for i in links[:5]:
    print(i)

sec = 10
print("Paused for {} seconds.".format(str(sec)))
time.sleep(sec)

# Get link status code, build CSV for download
csv = ""
for link in links:
    try:
        got = req.get(link)
        csv += link + "," + str(got.status_code) + "\n"
    except:
        csv += link + "," + "JO's script error" + "\n"

# Preview CSV output
preview = csv.split("\n")
for i in preview[:5]:
    print(i)

print("Paused for {} seconds.".format(str(sec)))
time.sleep(sec)

# Write out to CSV file (saves to machine)
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H%M")
with open("link_status_" + timestamp + ".csv", "w") as f:
    f.write(csv)
