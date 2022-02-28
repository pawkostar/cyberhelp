import sys
import json
import socket
from os import path

f_domains = sys.argv[1]

result_list = []
if path.exists(f_domains):

    with open(f_domains) as f:
        lines = f.read().splitlines()
        for domain in lines:
            ip = socket.gethostbyname(domain.strip())
            data = {
                'domain': domain,
                'ip': ip
            }
            result_list.append(data)
    with open('domain-ip-list.json', 'w') as outfile:
        json.dump(result_list, outfile)
else:
    print("File '%s' does not exist" % f_domains)
