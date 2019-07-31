import sys
import urllib.request
import hashlib

if len(sys.argv) != 2:
  print("Usage: %s <PASSWORD>" % sys.argv[0])
  print("Delete CLI history afterwards ;)" )
  exit(1)

password = sys.argv[1]
password_hash = hashlib.sha1(password.encode()).hexdigest().upper()

pwnd_password_url = "https://api.pwnedpasswords.com/range"

password_hashes = dict((x.decode().split(":")[0],x.decode().split(":")[1]) for x in urllib.request.urlopen("%s/%s" % (pwnd_password_url, password_hash[:5])).read().splitlines())

try:
    print("'%s' is used %s times!" % (password, password_hashes[password_hash[5:]]))
except:
    print("Your password doesn't pop up in the database.")
