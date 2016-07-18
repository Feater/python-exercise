import os;
import re;

files = os.listdir('.');

def runChecker(folder):
  files = os.listdir(folder);
  for file in files:
    if re.search(r'\.py$', file) and not re.match(r'^checker\.py$', file):
      print('need run checker', file);
      os.execv('echo', ('abc',));
    else:
      print('does not need check', file);

for file in files:
  if re.match(r'^\d\d', file):
    runChecker(file);
  else:
    print('ignore', file);
