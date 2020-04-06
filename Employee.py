

class Employee:
    def __init__(self, name, email, phone, department, title, education):
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.title = title
        self.education = education

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def set_department(self, department):
        self.department = department

    def get_department(self):
        return self.department

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_education(self, education):
        self.education = education

    def get_education(self):
        return self.education

    def get_attrs(self):
        return "{}/{}/{}/{}/{}/\n".format(self.email, self.phone, self.department, self.title, self.education)

    # def __str__(self):
    #     return "{}/{}/{}/{}/{}/{}/\n".format(self.name, self.email, self.phone, self.department, self.title,
    #                                          self.education)
