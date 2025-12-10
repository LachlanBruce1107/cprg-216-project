class Car:
    
    def __init__(self,id,name,make,body,year,value):
        self.id = id
        self.name = name
        self.make = make
        self.body = body
        self.year = year
        self.value = value

    def set_id(self,value):
        self.id = value

    def set_name(self,value):
        self.name = value

    def set_make(self,value):
        self.make = value

    def set_body(self,value):
        self.body = value

    def set_year(self,value):
        self.year = value

    def set_value(self,value):
        self.value = value

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_make(self):
        return self.make
    
    def get_body(self):
        return self.body
    
    def get_year(self):
        return self.year
    
    def get_value(self):
        return self.value
    
    def get_all_attributes(self):
        return f"{self.id}\t{self.name}\t{self.make}\t{self.body}\t{self.year}\t{self.value}"