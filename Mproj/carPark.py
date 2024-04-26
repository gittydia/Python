class ParkingOrga:
    def __init__(self):
        self.parkingrate = {
            "sedan" : 100,
            "hatchback" : 150,
            "suv" : 200,
            "pickup" : 170,
            "motorcycle" : 75,
            "super car" : 200 
        }

    def calculating_fee(self, car_type, park_hrs):
        if car_type == "super car":
            return self.parkingrate.get(car_type.lower(), 0) * park_hrs + 100
        elif car_type == "motorcycle":
            return self.parkingrate.get(car_type.lower(), 0) * park_hrs
        else:
            return self.parkingrate.get(car_type.lower(), 0) * park_hrs + 60
    
    def get_user_input(self):
        self.name = input("Enter your name: \n")
        self.car_model = input("Enter your vehicle model: \n")
        self.car_type = input("Enter your vehicle type: \nsedan : 100\n hatchback : 150\n suv : 200\n pickup : 170\n motorcycle : 75\n super car : 200 \n")
        self.park_hrs = int(input("Enter your parking hours: \n"))

    def display_receipt(self):
        fee = self.calculating_fee(self.car_type, self.park_hrs)
        #print the receipt
        print(f"Receipt for {self.name}")
        print(f"Vehicle model: {self.car_model}")
        print(f"vehicle type: {self.car_type}")
        print(f"Parking hours: {self.park_hrs}")
        print(f"Fee: {fee}")
        print(f"Total: {fee + 100}")



def main():
    while True:
    # create an instance of the ParkingOrga class
        print("-----PARKING-----")
        print("-----CAR RATE-----")
        print("\n sedan : 100\n hatchback : 150\n suv : 200\n pickup : 170\n motorcycle : 75\n super car : 200 \n")
        orga = ParkingOrga()
        orga.get_user_input()
        with open("Mproj/carinfos.txt", "a+") as file:
            file.write(f"owner name: {orga.name}\ncar model:{orga.car_model}\ncar type: {orga.car_type}\nparking hrs: {orga.park_hrs} hrs\ntotal: {orga.calculating_fee(orga.car_type, orga.park_hrs)} \n")
            file.write("----------------------------------------\n")
            
        print("----------DISPLAY RECEIPT------------")
        orga.display_receipt()
        cont = input("Do you want to continue? y/n: ")
        if cont.lower() == "n":
            break




        
if __name__ == "__main__":
    main()