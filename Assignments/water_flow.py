# writing three functions that need to be tested.

# making global variables
p = 998.2000000 # ρ is the density of water
g = 9.8066500 # g is the acceleration from Earths gravity
μ = 0.0010016 # μ is the dynamic viscosity of water

def water_column_height(tower_height, tank_height):
    # calculating the water column height using the formula 
    # h = t + (3w) / 4
    t = tower_height
    w = tank_height
    h = t + (3 * (w)) / 4
    return h # h being the height of the water column

def pressure_gain_from_water_height(height):
    # In this function, i will be using the following formula 
    # for calculating pressure caused by Earth’s gravity.
    # P = (p * g * h) / 1000
    # P is the pressure in kilopascals
    # ρ is the density of water 998.2 ( kilogram / meter3) *Just use # in your calculations
    # g is the acceleration from Earths gravity 9.80665 (meter / second2) *Just use # in your calculations
    # h is the height of the water column in meters
    h = height
    P = (p * g * h) / 1000
    return P # P is the pressure in kilopascals

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    # In this function, use the following formula for calculating 
    # pressure loss from friction within a pipe.
    # P = ((-f) * L * p (v ** 2)) / (2000 * d)
    # P is the lost pressure in kilopascals
    # f is the pipe’s friction factor
    # L is the length of the pipe in meters
    # ρ is the density of water 998.2 (kilogram / meter3) *Just use # in your calculations
    # v is the velocity of the water flowing through the pipe in meters / second
    # d is the diameter of the pipe in meters
    f = friction_factor
    L = pipe_length
    v = fluid_velocity
    d = pipe_diameter
    P = ((-f) * L * p * (v ** 2)) / (2000 * d)
    return P # P is the lost pressure in kilopascals

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    # In this function, use the following formula for 
    # calculating pressure loss from pipe fittings.
    # p = (-0.04 * p * (v ** 2) * n) / 2000
    # P is the lost pressure in kilopascals
    # ρ is the density of water (998.2 kilogram / meter3)
    # v is the velocity of the water flowing through the pipe in meters / second
    # n is the quantity of fittings
    v = fluid_velocity
    n = quantity_fittings
    P = (-0.04 * p * (v ** 2) * n) / 2000
    return P # P is the lost pressure in kilopascals

def reynolds_number(hydraulic_diameter, fluid_velocity):
    # The Reynolds number is a unitless ratio of the inertial and 
    # viscous forces in a fluid that is useful for predicting 
    # fluid flow in different situations.
    
    # In this function, use the following formula for 
    # calculating the Reynolds number
    # R = (p * d * v) / μ
    # R is the Reynolds number
    # ρ is the density of water (998.2 kilogram / meter3)
    # d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
    # v is the velocity of the water flowing through the pipe in meters / second
    # μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
    d = hydraulic_diameter
    v = fluid_velocity
    R = (p * d * v) / μ
    return R # R is the Reynolds number

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    # In this function, use the following two formulas for 
    # calculating pressure loss from a rounded reduction in a pipe’s diameter.
    # k = (0.1 + (50 / R)) * (((D / d) ** 4) - 1)
    # P = (-k * p * (v ** 2)) / 2000
    # k is a constant computed by the first formula and used in the second formula
    # R is the Reynolds number that corresponds to the pipe with the larger diameter
    # D is the diameter of the larger pipe in meters
    # d is the diameter of the smaller pipe in meters
    # P is the lost pressure kilopascals
    # ρ is the density of water (998.2 kilogram / meter3)
    # v is the velocity of the water flowing through the larger diameter pipe in meters / second
    R = reynolds_number
    D = larger_diameter
    d = smaller_diameter
    v = fluid_velocity
    k = (0.1 + (50 / R)) * (((D / d) ** 4) - 1)
    P = (-k * p * (v ** 2)) / 2000
    return P # P is the lost pressure kilopascals


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def psi_from_kPa(pressure):
    kPa = pressure
    psi = kPa * 0.14503773773020923
    return psi # psi is pounds per square inch

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    psi_pressure = psi_from_kPa(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f'Pressure at house in PSI: {psi_pressure:.1f} PSI')

if __name__ == "__main__":
    main()