from car import Car


car = Car("Ferrari", "812GTS", 2022, "Red", 750)
print("Color Atributes: ")
print(car.get_color(), car.get_brand())
print(car.change_color("Yellow"))
print(car.change_color("Yellow"))
print(car.change_color(2))

print("\nHP Change: ")
print("Model:", car.get_model(), "HP:", car.get_horse_power())
print(car.get_horse_power())
print(car.increase_horse_power(50))
print(car.increase_horse_power(-30))
print(car.increase_horse_power("enzo"))