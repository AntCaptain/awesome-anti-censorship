s = "- [{project}](https://github.com/{project})[![{project}](https://img.shields.io/github/stars/{project}.svg?style=social&label=Stars)](https://github.com/{project}) ![last-commit](https://img.shields.io/github/last-commit/{project}.svg)"

repos="""\
OpenVPN/openvpn
shadowsocks/shadowsocks-libev
txthinking/brook
v2ray/v2ray-core
XX-net/XX-Net
StreisandEffect/streisand\
""".split('\n')
for r in repos:
    print(s.format(project=r))
