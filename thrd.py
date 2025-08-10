class One:
    def get_data(self,a):
        self.a=a
    def display_data(self):
        print(self.a)

b=One()
name=input("enter a name")
b.get_data(name)
b.display_data()