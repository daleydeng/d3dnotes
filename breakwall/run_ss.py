#!/usr/bin/env python
from os import system

# addresses
#   ss://FYqMWXjDJTEZ@{hk1,us2,jp1}-sta71.s666n.pw:41650
#   ss://u6tFhWSbN2k9@{hk1,jp1,us1,us2}-sta13.3fufr.pw:22212

port = 22212
password = "u6tFhWSbN2k9"
servers = [
    'hk1',
    'jp1',
    'jp1',
    'us1',
    'us2',
]

enc='chacha20-ietf-poly1305'

if __name__ == "__main__":
    from argparse import ArgumentParser
    ap = ArgumentParser()
    ap.add_argument('-s', type=int, default=0)
    args = ap.parse_args()

    print(servers[args.s])
    system(f'sslocal -s {servers[args.s]}-sta13.3fufr.pw -p {port} -b 127.0.0.1 -l 1080 -k {password} -m {enc}')
