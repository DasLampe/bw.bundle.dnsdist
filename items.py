files = {
    '/etc/dnsdist/dnsdist.conf': {
        'source': 'dnsdist.conf',
        'content_type': 'mako',
        'triggers': [
            'svc_systemd:dnsdist:restart',
        ],
        'needs': [
            'pkg_apt:dnsdist',
        ]
    },
}

svc_systemd = {
    'dnsdist': {
        'running': True,
        'enabled': True,
        'needs': [
            'file:/etc/dnsdist/dnsdist.conf',
        ]
    }
}
