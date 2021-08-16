class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerating..")
    def change_gear(self,gear_type):
        return gear_type
        print("gear shift")

Hennesy = Car("Hennesy venom gt","Slate Grey","Hennesy",270)
print(Hennesy.change_gear(6))