class Worker:
    def __init__(self, worker_num, fname, lname,
                 work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age

    def worker_information(self):
        return f"({self.worker_num},{self.fname},{self.lname},{self.work_experience_company},{self.salary},{self.age})"

    def __repr__(self):
        return f"({self.worker_num},{self.fname},{self.lname},{self.work_experience_company},{self.salary},{self.age})"

    def __str__(self):
        return f"({self.worker_num},{self.fname},{self.lname},{self.work_experience_company},{self.salary},{self.age})"

    def __eq__(self, other):
        if not hasattr(other, 'worker_num'):
            return False
        return self.worker_num == other.worker_num

    def salary_bonus(self):
        if self.work_experience_company < 5:
            return round(self.salary*0.5/100, 2)
        elif self.work_experience_company > 10:
            return round(self.salary*2/100, 2)
        else:
            return round(self.salary*1.5/100, 2)
