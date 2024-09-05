import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from app.utils.plotting import plot_to_base64


def simulate_projectile_motion(initial_velocity, angle_degrees, gravity=9.8):
    angle_radians = np.radians(angle_degrees)
    vx = initial_velocity * np.cos(angle_radians)
    vy = initial_velocity * np.sin(angle_radians)

    # Calculate time of flight
    t_flight = 2 * vy / gravity

    # Generate time points
    t = np.linspace(0, t_flight, 100)

    # Calculate x and y positions
    x = vx * t
    y = vy * t - 0.5 * gravity * t**2

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y)
    ax.set_title("Projectile Motion")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.grid(True)

    # Add some key points
    max_height = vy**2 / (2 * gravity)
    max_range = vx * t_flight
    ax.plot(max_range / 2, max_height, "ro", label="Max Height")
    ax.plot(max_range, 0, "bo", label="Max Range")
    ax.legend()

    # Add text annotations
    ax.text(
        max_range / 2,
        max_height,
        f"Max Height: {max_height:.2f} m",
        verticalalignment="bottom",
    )
    ax.text(max_range, 0, f"Max Range: {max_range:.2f} m", horizontalalignment="right")

    return plot_to_base64(fig)


def damped_harmonic_oscillator(y, t, b, k, m):
    x, v = y
    dydt = [v, -b / m * v - k / m * x]
    return dydt


def simulate_damped_harmonic_motion(
    mass: float,
    spring_constant: float,
    damping_coefficient: float,
    initial_displacement: float,
    initial_velocity: float,
    duration: float,
):
    t = np.linspace(0, duration, 1000)
    y0 = [initial_displacement, initial_velocity]

    sol = odeint(
        damped_harmonic_oscillator,
        y0,
        t,
        args=(damping_coefficient, spring_constant, mass),
    )

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    ax1.plot(t, sol[:, 0])
    ax1.set_title("Displacement vs Time")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Displacement (m)")

    ax2.plot(t, sol[:, 1])
    ax2.set_title("Velocity vs Time")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Velocity (m/s)")

    plt.tight_layout()

    return plot_to_base64(fig), {
        "time": t.tolist(),
        "displacement": sol[:, 0].tolist(),
        "velocity": sol[:, 1].tolist(),
    }
