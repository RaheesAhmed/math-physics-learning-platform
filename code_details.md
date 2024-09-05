# Math and Physics Educational Platform - Summary

## Project Overview
A FastAPI-based backend providing endpoints for mathematical calculations, physics simulations, and data visualizations. 

## Key Features
- Complex function visualization
- Fourier transform analysis
- Differential equation solver
- Projectile motion simulation
- Damped harmonic motion simulation

## File Structure Summary

1. `app/main.py`
   - Main FastAPI application
   - Sets up CORS middleware
   - Includes routers for math and physics endpoints

2. `app/core/config.py`
   - Configuration settings using Pydantic
   - Defines project name, version, and allowed origins

3. `app/api/math_routes.py`
   - FastAPI router for math-related endpoints
   - Endpoints:
     - Complex function visualization
     - Fourier transform
     - Differential equation solver

4. `app/api/physics_routes.py`
   - FastAPI router for physics-related endpoints
   - Endpoints:
     - Projectile motion
     - Damped harmonic motion

5. `app/services/math_service.py`
   - Contains functions for mathematical computations
   - Implements:
     - Complex function plotting
     - Fourier transform calculation
     - Differential equation solving

6. `app/services/physics_service.py`
   - Contains functions for physics simulations
   - Implements:
     - Projectile motion calculation
     - Damped harmonic motion simulation

7. `app/utils/plotting.py`
   - Utility function to convert Matplotlib figures to base64 encoded strings

8. `requirements.txt`
   - Lists all Python dependencies

9. `Dockerfile`
   - Instructions for building a Docker image of the application

10. `.env`
    - Environment variables for configuration

## Key Code Snippets

1. Complex Function Visualization (`math_service.py`):
   ```python
   def generate_complex_function_plot(function_type: str, x_range: tuple, y_range: tuple):
       # Creates contour plots for magnitude and phase of complex functions
   ```

2. Fourier Transform (`math_service.py`):
   ```python
   def generate_fourier_transform(signal_type: str, frequency: float, duration: float, sample_rate: float):
       # Generates time-domain signal and its Fourier transform
   ```

3. Differential Equation Solver (`math_service.py`):
   ```python
   def solve_differential_equation(equation_type: str, parameters: dict, initial_conditions: list, t_span: list):
       # Solves different types of ODEs using scipy.integrate.odeint
   ```

4. Projectile Motion (`physics_service.py`):
   ```python
   def simulate_projectile_motion(initial_velocity, angle_degrees, gravity=9.8):
       # Calculates and plots projectile motion
   ```

5. Damped Harmonic Motion (`physics_service.py`):
   ```python
   def simulate_damped_harmonic_motion(mass: float, spring_constant: float, damping_coefficient: float, initial_displacement: float, initial_velocity: float, duration: float):
       # Simulates damped harmonic oscillator using odeint
   ```

## API Endpoints Summary

1. `POST /api/math/complex_function`
   - Visualizes complex functions

2. `POST /api/math/fourier_transform`
   - Performs Fourier transform on various signal types

3. `POST /api/math/differential_equation`
   - Solves and plots solutions for different types of ODEs

4. `POST /api/physics/projectile_motion`
   - Simulates projectile motion

5. `POST /api/physics/damped_harmonic_motion`
   - Simulates damped harmonic motion

## Setup and Running
1. Install dependencies: `pip install -r requirements.txt`
2. Run server: `uvicorn app.main:app --reload`
3. Access API at `http://localhost:8000`

## Docker Support
- Build: `docker build -t math-physics-platform .`
- Run: `docker run -p 8000:8000 math-physics-platform`