class Fan:
    def __init__(self):
        self.speed = 0  # 0: off, 1: low, 2: medium, 3: high
    
    def turn_on(self):
        if self.speed == 0:
            self.speed = 1
        print("Fan is turned on.")
    
    def turn_off(self):
        self.speed = 0
        print("Fan is turned off.")
    
    def set_speed(self, speed):
        if speed in [0, 1, 2, 3]:
            self.speed = speed
            print(f"Fan speed set to {self.get_speed()} level.")
        else:
            print("Invalid speed level. Please enter 1, 2, or 3.")
    
    def get_speed(self):
        speed_levels = {0: "off", 1: "low", 2: "medium", 3: "high"}
        return speed_levels[self.speed]

def main():
    fan = Fan()
    
    while True:
        print("\nFan Control Menu:")
        print("1. Turn on the fan")
        print("2. Turn off the fan")
        print("3. Set fan speed")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            fan.turn_on()
        elif choice == '2':
            fan.turn_off()
        elif choice == '3':
            speed = int(input("Enter speed level (1: low, 2: medium, 3: high): "))
            fan.set_speed(speed)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        print(f"Current fan speed is {fan.get_speed()}.")

if __name__ == "__main__":
    main()