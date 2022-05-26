files = {
    '/etc/dnsdist/dnsdist.conf': {
        'source': 'dnsdist.conf',
        'content_type': 'mako',
        'triggers': [
            'svc_systemd:dnsdist:restart',
        ],
    },
}

svc_systemd = {
    'dnsdist': {
        'running': True,
        'enabled': True,
    }
}
