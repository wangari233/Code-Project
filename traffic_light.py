traffic_light_colour = input("Enter a traffic light colour:")
if not traffic_light_colour:
    print("Wrong colour:Input cannot be empty.")
elif traffic_light_colour == "red":
    print("Stop!")
elif traffic_light_colour == "yellow":
    print("Get Ready!")
elif traffic_light_colour == "green":
    print("Go!")    
else:
    print("Invalid colour")