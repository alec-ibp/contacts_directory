import uuid

class Contact:
    def __init__(self, name, company, email, job, uid=None) -> None:
        self.name = name
        self.company = company
        self.email = email
        self.job = job
        self.uid = uid or uuid.uuid4()


    def to_dict(self):
        return vars(self)

    @staticmethod
    def list_schema():
        return ['name, company, email, job, uid']
