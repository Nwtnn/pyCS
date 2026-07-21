import nmap

nm = nmap.PortScanner()

target = ""   


options = "-sV -sC"

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")

    for protocol in nm[host].all_protocols():
        print(f"Protocol: {protocol}")

        port_info = nm[host][protocol]

        for port, info in port_info.items():
            print(f"Port: {port}\tState: {info['state']}")
            if 'name' in info:
                print(f"\tService: {info['name']}")
            if 'product' in info:
                print(f"\tProduct: {info['product']}")
            if 'version' in info:
                print(f"\tVersion: {info['version']}")
