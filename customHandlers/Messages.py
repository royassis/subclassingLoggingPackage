

class Message:
    def __init__(self, machine, snif, success, host, internal_ip):
        self.machine = machine
        self.snif = snif
        self.success = success
        self.host = host
        self.internal_ip = internal_ip

    def as_dict(self):
        return self.__dict__

