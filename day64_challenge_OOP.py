# WE are going to create jobs. Doctor, teacher and lawyer include everything thats included in normal job
# we are going to include speciality and year experience and teacher should include subject and position. And print functions

# vamos a crear 3 trabajos. 1: abogado, 2: profesor, 3: doctor 
# luego lo vamos a mostrar en pantalla usando las funciones integradas

class job:
    name = None
    salary = None
    hours = None
    
    def __init__(self, name, salary, hours):
        self.name = name
        self.salary = salary
        self.hours = hours

    def print(self):
        print("@@ JOB @@ ")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hours:>10}")

class doctor(job): # RECUERDA: al llamar "doctor(job)"" estamos heredando el salario, horas del abogado y luego definimos y añadimos experience y speciality
    
    experience = None
    speciality = None

    def __init__(self, salary, hours, experience, speciality):
        self.name = "Doctor"
        self.salary = salary
        self.hours = hours
        self.experience = experience
        self.speciality = speciality

    def print(self):
        print("@@ JOB @@ ")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hours:>10}") #recuerda los <15 y tal son para la alineación a la izq, derch y centro
        print(f"{self.experience:<10} {self.speciality:>21}")

class teacher(job):

    subject = None
    position = None

    def __init__(self, salary, experience, subject, position):
        self.name = "Teacher"
        self.salary = salary
        self.subjetct = subject
        self.experience = experience
        self.position = position

    def print(self):
        print("@@ JOB @@ ")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.experience:>10}") #recuerda los <15 y tal son para la alineación a la izq, derch y centro
        print(f"{self.subjetct:<10} {self.position:>21}")




lawyer = job("Lawyer", "~$100.000", "40")
lawyer.print()

doc = doctor("~$200.000", "35", "7 years", "Pediaric")
doc.print()

teach = teacher("~$50.0000", "3 years", "Maths", "Principal")
teach.print()


        
