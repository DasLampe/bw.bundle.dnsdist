# Install [dnsdist](https://dnsdist.org/) via Bundlewrap

## Dependencies
- [apt-Bundle](https://github.com/sHorst/bw.bundle.apt)

## Demo Config
```
'dnsdist': {
    'listen_addresses': [
        '0.0.0.0:53',
        '[::]:53',
    ],
    'allowed_netmasks': [
        '0.0.0.0/0',
        '::/0',
    ],
    'servers': [
        {'address': '127.0.0.1:5300', 'pool': 'auth'},
        {'address': '127.0.0.1:5301', 'pool': 'recursor'}
    ],
    'allowed_recursion_netmasks': [
        '192.168.0.0/24',
    ],
    'actions': [
        "NetmaskGroupRule(recursive_ips), PoolAction('recursor')",
        "AllRule(), PoolAction('auth')",
    ], 
}
```
