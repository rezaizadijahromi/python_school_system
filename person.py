from address import Address

class Person:
    def __init__(self, first, last, dob, phone, address):
        self.first = first
        self.last = last 
        self.dare_of_birth = dob
        self.phone = phone
        self.addresses = []

        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise Error("Invalid address...")

            self.addresses = address
        else:
            raise Error("Invalid Address")

    def add_address(self, address):
        if not isinstance(address , Address):
            raise Error("Invalid address")

        self.addresses.append(address)
