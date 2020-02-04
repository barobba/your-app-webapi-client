
class BankServices:

    def credit(self, amount):
        raise NotImplementedError

    def debit(self, amount):
        raise NotImplementedError

    def lock(self):
        raise NotImplementedError

    def unlock(self):
        raise NotImplementedError
