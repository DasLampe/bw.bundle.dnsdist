defaults = {}

if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            'dnsdist': {'installed': True, },
        }
    }

if node.has_bundle("iptables"):
    defaults += repo.libs.iptables.accept().tcp().chain('INPUT').dest_port(53)
    defaults += repo.libs.iptables.accept().udp().chain('INPUT').dest_port(53)
