"""permet de nettoyer les fichiers de:
https://wortschatz.uni-leipzig.de/en/download/English
https://wortschatz.uni-leipzig.de/en/download/French
"""

import sys
import re

data = open(sys.argv[1], 'r', encoding='utf-8')
output = open(sys.argv[2], 'w', encoding ='utf-8')
language = sys.argv[3]

for line in data.readlines():
	line = re.sub('^[0-9]+\t', '', line)
	line = re.sub('\n$', '', line)
	output.write(f"{line}\t{language}\n")

output.close()
