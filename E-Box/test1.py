# import re
# sentence = 'horses are fast'
# regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
# matched = re.search(regex, sentence)
# print(matched.groupdict())

# import re
# re.ASCII

import re
sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())