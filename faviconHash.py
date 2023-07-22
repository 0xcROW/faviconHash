import requests
import mmh3
import base64
import sys
import pyperclip
from io import StringIO

#Get the favicon hash
faviconPath = input("Favicon path: ")
response = requests.get(faviconPath)
favicon = base64.encodebytes(response.content)
hash = mmh3.hash(favicon)
#Shows the hash
print("Here's the hash:",hash)
shodanQuery = 'https://www.shodan.io/search?query=http.favicon.hash%3A'
#Send the stdout to output and clipboard
res = sys.stdout
result = StringIO()
sys.stdout = result
print(shodanQuery,hash, sep="")
sys.stdout = res
print(result.getvalue())
pyperclip.copy(result.getvalue())
print("Hash and URL copied and sent to clipboard, just paste at browser!")
print("Don't forget to login into shodan.")