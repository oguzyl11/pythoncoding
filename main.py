import matplotlib.pyplot as plt
trucks = [
    {"id": 35 , "capacity": 100 , "loaded_cargo": [] },
    {"id": 52 , "capacity": 70 , "loaded_cargo": [] },
    {"id": 23 , "capacity": 150 , "loaded_cargo": [] }
]

cargo = [
    {"id": 1 , "weight": 50 , "importance" : 1 , "x": 10 , "y": 20 },
    {"id": 2 , "weight": 120 , "importance": 0, "x": 25 , "y": 70 },
    {"id": 3 , "weight": 30 , "importance": 0, "x": 55 , "y": 20 },
    {"id": 4 , "weight": 20 , "importance": 1, "x": 50 , "y": 40 },
    {"id": 5 , "weight": 100 , "importance": 0, "x": 80 , "y": 60 }
 ]

n = len(trucks)
m = len(cargo)
for i in range(m-1):
    for j in range(m-i-1):
        if cargo[j]["importance"] < cargo[j+1]["importance"] or (cargo[j]["importance"] == cargo[j+1]["importance"] and cargo[j]["weight"] < cargo[j+1]["weight"]):
            cargo[j], cargo[j+1] = cargo[j+1], cargo[j]
for i in range(m):
    capacity_weight_difference = 9999
    best_trucks_id = -1
    for j in range(n):
        if cargo[i]["weight"] <= trucks[j]["capacity"]:
            capacity_for_trucks = trucks[j]["capacity"] - cargo[i]["weight"]
            if capacity_weight_difference > capacity_for_trucks:
                capacity_weight_difference = capacity_for_trucks
                best_trucks_id = j

    if best_trucks_id != -1:
        trucks[best_trucks_id]["capacity"] -= cargo[i]["weight"]
        trucks[best_trucks_id]["loaded_cargo"].append(cargo[i])


for t in trucks:
    x1 = 0
    y1 = 0
    t["distance"] = 0.0
    current_x = 0
    current_y = 0
    for c in t["loaded_cargo"]:
        current_x = c["x"]
        current_y = c["y"]
        t["distance"] += ((current_x - x1) ** 2 + (current_y - y1) ** 2) ** 0.5
        x1 = current_x
        y1 = current_y
    
for t in trucks:
    print(f"Truck ID: {t['id']}, Distance: {t['distance']}, Remaining Capacity: {t['capacity']}, Loaded Cargo IDs: {[c['id'] for c in t['loaded_cargo']]}")
        
colors = ['cyan', 'blue', 'green' , 'orange', 'purple']
color_order = 0
plt.figure(figsize=(10,6))
plt.title("Truck Routes")
plt.scatter(0,0, color='red', s=150, label='Warehouse', zorder = 5 )

for t in trucks:
    if not t["loaded_cargo"]:
        continue
    x_coords = [0]
    y_coords = [0]

    for c in t["loaded_cargo"]:
        x_coords.append(c["x"])
        y_coords.append(c["y"])

        plt.scatter(c["x"], c["y"], color=colors[color_order], s=80, zorder=5)
        plt.text(c["x"] + 2, c["y"] + 2, f"Cargo {c['id']}",fontsize=10, fontweight='bold')
        plt.plot(x_coords, y_coords, color=colors[color_order], linestyle='-', linewidth=2, label=f"Truck {t['id']}")
        color_order += 1

    plt.xlabel("X coords")
plt.ylabel("Y coords")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()    

 