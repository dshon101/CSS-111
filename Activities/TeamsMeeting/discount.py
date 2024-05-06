""" we could use list variables for the can_name, can_radius, can_height and  can_cost
can_name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 7.62, 8.10]
can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
can_cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
"""
import math
 
can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 7.62, 8.10]
can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

def main():
    name = "#1 Picnic"
    volume = compute_volume(6.83, 10.16)
    surface_area = compute_surface_area(6.83, 10.16)
    storage = storage_efficiency(volume, surface_area)
    print(f"{name} {storage:.2f}")
 

def compute_volume(radius, height):   # volume = π * radius**  * height (use import math for pi)
   
    volume = math.pi * radius**2 * height
    return volume
 
def compute_surface_area(radius, height):  # surface_area = 2π * radius * (radius + height)
    surface_area = 2 * math.pi * radius * (radius + height)  
    return surface_area

def storage_efficiency(volume, surface_area):
    storage = volume / surface_area
    return storage
        #storage_efficiency = compute_volume(radius, height) / compute_surface_area(radius, height)
main()
