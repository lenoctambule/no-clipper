import bannergrab as bg

class StealthScan:
    hosts_batch = list(bg.Host)
    port_list = [20,21,22,80,443,1337,8080]

    def __init__(self) -> None:
        pass