def kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity**2)


print("Enter mass: ", end="")
mass = float(input())

print("Enter velocity: ", end="")
velocity = float(input())

print(f"Kinetic energy: {kinetic_energy(mass,velocity)}")
