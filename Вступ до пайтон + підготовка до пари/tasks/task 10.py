import math

x1 = 39.9075000
y1 = 116.3972300

x2 = 50.4546600
y2 = 30.5238000

x1_rad = math.radians(x1)
y1_rad = math.radians(y1)
x2_rad = math.radians(x2)
y2_rad = math.radians(y2)

inner_part = math.sin(x1_rad) * math.sin(x2_rad) + math.cos(x1_rad) * math.cos(x2_rad) * math.cos(y1_rad - y2_rad)
distance = 6371.032 * math.acos(inner_part)

print("Distance between Beijing and Kyiv (km):")
print(format(distance, ">10.3f"))