class Employee:
    def __init__(self, name, email, phone, department, title, education):
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.title = title
        self.education = education

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def set_department(self, department):
        self.department = department

    def set_title(self, title):
        self.title = title

    def set_education(self, education):
        self.education = education

    def stringify_attrs(self):
        return "{}/{}/{}/{}/{}/\n".format(self.email, self.phone, self.department, self.title, self.education)
