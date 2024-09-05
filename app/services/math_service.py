import numpy as np
import matplotlib.pyplot as plt
from app.utils.plotting import plot_to_base64
from scipy.integrate import odeint


def generate_complex_function_plot(function_type: str, x_range: tuple, y_range: tuple):
    x = np.linspace(x_range[0], x_range[1], 200)
    y = np.linspace(y_range[0], y_range[1], 200)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    if function_type == "z^2":
        W = Z**2
    elif function_type == "exp":
        W = np.exp(Z)
    elif function_type == "gamma":
        W = gamma(Z)
    else:
        raise ValueError("Unsupported function type")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    c1 = ax1.contourf(X, Y, np.abs(W), cmap="viridis")
    fig.colorbar(c1, ax=ax1)
    ax1.set_title(f"Magnitude of {function_type}(z)")
    ax1.set_xlabel("Real Part")
    ax1.set_ylabel("Imaginary Part")

    c2 = ax2.contourf(X, Y, np.angle(W), cmap="hsv")
    fig.colorbar(c2, ax=ax2)
    ax2.set_title(f"Phase of {function_type}(z)")
    ax2.set_xlabel("Real Part")
    ax2.set_ylabel("Imaginary Part")

    return plot_to_base64(fig)


def generate_fourier_transform(
    signal_type: str, frequency: float, duration: float, sample_rate: float
):
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

    if signal_type == "sine":
        signal = np.sin(2 * np.pi * frequency * t)
    elif signal_type == "square":
        signal = np.sign(np.sin(2 * np.pi * frequency * t))
    elif signal_type == "sawtooth":
        signal = 2 * (t * frequency - np.floor(0.5 + t * frequency))
    else:
        raise ValueError("Unsupported signal type")

    fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(t), 1 / sample_rate)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    ax1.plot(t, signal)
    ax1.set_title(f"{signal_type.capitalize()} Wave")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Amplitude")

    ax2.plot(freqs[: len(freqs) // 2], np.abs(fft)[: len(freqs) // 2])
    ax2.set_title("Fourier Transform")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Magnitude")
    ax2.set_xlim(0, frequency * 10)

    plt.tight_layout()

    return plot_to_base64(fig), {
        "time": t.tolist(),
        "signal": signal.tolist(),
        "frequencies": freqs[: len(freqs) // 2].tolist(),
        "magnitudes": np.abs(fft)[: len(freqs) // 2].tolist(),
    }


def solve_differential_equation(
    equation_type: str, parameters: dict, initial_conditions: list, t_span: list
):
    t = np.linspace(t_span[0], t_span[1], 1000)

    if equation_type == "first_order_linear":

        def ode(y, t, a, b):
            return a * y + b

        solution = odeint(
            ode, initial_conditions[0], t, args=(parameters["a"], parameters["b"])
        )
    elif equation_type == "second_order_linear":

        def ode(y, t, a, b, c):
            y1, y2 = y
            return [y2, a * y2 + b * y1 + c]

        solution = odeint(
            ode,
            initial_conditions,
            t,
            args=(parameters["a"], parameters["b"], parameters["c"]),
        )
    elif equation_type == "predator_prey":

        def ode(y, t, a, b, c, d):
            prey, predator = y
            dprey_dt = a * prey - b * prey * predator
            dpredator_dt = -c * predator + d * prey * predator
            return [dprey_dt, dpredator_dt]

        solution = odeint(
            ode,
            initial_conditions,
            t,
            args=(parameters["a"], parameters["b"], parameters["c"], parameters["d"]),
        )
    else:
        raise ValueError("Unsupported equation type")

    fig, ax = plt.subplots(figsize=(10, 6))

    if equation_type in ["first_order_linear", "second_order_linear"]:
        ax.plot(t, solution)
        ax.set_ylabel("y")
    elif equation_type == "predator_prey":
        ax.plot(t, solution[:, 0], label="Prey")
        ax.plot(t, solution[:, 1], label="Predator")
        ax.legend()
        ax.set_ylabel("Population")

    ax.set_xlabel("t")
    ax.set_title(f'Solution of {equation_type.replace("_", " ").title()} ODE')
    ax.grid(True)

    return plot_to_base64(fig), {"t": t.tolist(), "solution": solution.tolist()}
