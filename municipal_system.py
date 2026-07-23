class Personnel: 
    def __init__ (self,name,surname,department,salary):
        self.name = name
        self.surname = surname
        self.department = department
        self.__salary = salary 

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,new_salary):
        if new_salary > 0:
            self.__salary = new_salary 
        else:
            print("Invalid salary!")

    def __str__(self):
        return F"{self.name} {self.surname} {self.department} {self.salary}" 

class SoftwareDeveloper(Personnel):
    def __init__(self, name, surname, department, salary,languages):
        super().__init__(name, surname, department, salary)
        self.languages = languages 
    def __str__(self):
        return F"{self.name} {self.surname} {self.department} {self.salary} {self.languages}"
    


class FieldWorker (Personnel): 
    def __init__(self, name, surname, department, salary,assigned_region):
        super().__init__(name, surname, department, salary)
        self.assigned_region = assigned_region
    def __str__(self):
        return F"{self.name} {self.surname} {self.department} {self.salary} {self.assigned_region}"

class Asset:
    def __init__(self,asset_name,value):
        self.asset_name = asset_name
        self.value = value

    def __str__(self):
        return F"{self.asset_name} {self.value}"
    
    def __add__(self, other):
        return self.value + other.value

class MunicipalSystem:
    def __init__(self,municipality_name):
        self.municipality_name = municipality_name
        self.personnel_list = []
        self.asset_list = []

    def add_personnel(self,personnel):
        self.personnel_list.append(personnel)
    
    def add_asset(self, asset):
        self.asset_list.append(asset)
    
    def calculate_total_salary(self):
        total = 0
        for i in self.personnel_list:
            total += i.salary 
        return total

    def __len__(self):
        return len(self.personnel_list)

if __name__ == "__main__":
    system = MunicipalSystem("Ankara MunicipalSystem")

    dev = SoftwareDeveloper("Ahmet", "Yılmaz", "IT", 50000, ["Python", "SQL"])
    worker = FieldWorker("Mehmet", "Kaya", "Operations", 35000, "Çankaya")

    # Personelleri sisteme ekliyoruz:
    system.add_personnel(dev)
    system.add_personnel(worker)

    truck = Asset("Garbage Truck", 1500000)
    server = Asset("Main Server", 400000)

    system.add_asset(truck)
    system.add_asset(server)

    print("--- Personnel List ---")
    print(dev)
    print(worker)

    print("\n--- System Status ---")
    print(f"Total Personnel Count: {len(system)}")
    print(f"Total Salary Budget: {system.calculate_total_salary()} TL")
    
    print("\n--- Asset Magic Method Test ---")
    total_asset_value = truck + server
    print(f"Combined Value of Truck + Server: {total_asset_value} TL")