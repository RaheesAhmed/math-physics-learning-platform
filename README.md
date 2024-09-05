# Math and Physics Educational Platform API

This project is a FastAPI-based backend API for a Math and Physics Educational Platform. It provides various endpoints for mathematical calculations, physics simulations, and data visualizations. The platform is designed to be easily extendable and can be used as a foundation for educational tools or scientific computing applications.

## Features

- Complex function visualization
- Fourier transform analysis
- Differential equation solver
- Projectile motion simulation
- Damped harmonic motion simulation

## Project Structure

```
math_physics_platform/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── math_routes.py
│   │   └── physics_routes.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   └── __init__.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── math_service.py
│   │   └── physics_service.py
│   └── utils/
│       ├── __init__.py
│       └── plotting.py
├── tests/
│   └── __init__.py
├── .env
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/raheesahmed/math-physics-learning-platform.git
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add the following:
   ```
   PROJECT_NAME=Math and Physics Educational Platform
   PROJECT_VERSION=1.0.0
   ALLOWED_ORIGINS=http://localhost:3000
   ```

5. Run the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

The server will start running on `http://localhost:8000`.

## API Endpoints

### Mathematics

1. Complex Function Visualization
   - Endpoint: `POST /api/math/complex_function`
   - Payload:
     ```json
     {
       "function": "z^2",
       "x_range": [-5, 5],
       "y_range": [-5, 5]
     }
     ```

2. Fourier Transform
   - Endpoint: `POST /api/math/fourier_transform`
   - Payload:
     ```json
     {
       "signal_type": "sine",
       "frequency": 10,
       "duration": 1,
       "sample_rate": 1000
     }
     ```

3. Differential Equation Solver
   - Endpoint: `POST /api/math/differential_equation`
   - Payload:
     ```json
     {
       "equation_type": "predator_prey",
       "parameters": {"a": 1.0, "b": 0.1, "c": 1.5, "d": 0.075},
       "initial_conditions": [10, 5],
       "t_span": [0, 30]
     }
     ```

### Physics

1. Projectile Motion
   - Endpoint: `POST /api/physics/projectile_motion`
   - Payload:
     ```json
     {
       "initial_velocity": 50,
       "angle_degrees": 45,
       "gravity": 9.8
     }
     ```

2. Damped Harmonic Motion
   - Endpoint: `POST /api/physics/damped_harmonic_motion`
   - Payload:
     ```json
     {
       "mass": 1,
       "spring_constant": 10,
       "damping_coefficient": 0.5,
       "initial_displacement": 1,
       "initial_velocity": 0,
       "duration": 10
     }
     ```

CHECK MORE ABOUT CODE here [CODE DOCS](/backend/code_details.md)

## Usage Examples

You can use curl to test the API endpoints. Here are some examples:

1. Complex Function Visualization:
   ```bash
   curl -X POST "http://localhost:8000/api/math/complex_function" \
        -H "Content-Type: application/json" \
        -d '{"function": "z^2", "x_range": [-2, 2], "y_range": [-2, 2]}'
   ```

2. Fourier Transform:
   ```bash
   curl -X POST "http://localhost:8000/api/math/fourier_transform" \
        -H "Content-Type: application/json" \
        -d '{"signal_type": "sine", "frequency": 10, "duration": 1, "sample_rate": 1000}'
   ```

3. Differential Equation Solver:
   ```bash
   curl -X POST "http://localhost:8000/api/math/differential_equation" \
        -H "Content-Type: application/json" \
        -d '{
            "equation_type": "predator_prey",
            "parameters": {"a": 1.0, "b": 0.1, "c": 1.5, "d": 0.075},
            "initial_conditions": [10, 5],
            "t_span": [0, 30]
        }'
   ```

4. Projectile Motion:
   ```bash
   curl -X POST "http://localhost:8000/api/physics/projectile_motion" \
        -H "Content-Type: application/json" \
        -d '{"initial_velocity": 50, "angle_degrees": 45, "gravity": 9.8}'
   ```

5. Damped Harmonic Motion:
   ```bash
   curl -X POST "http://localhost:8000/api/physics/damped_harmonic_motion" \
        -H "Content-Type: application/json" \
        -d '{"mass": 1, "spring_constant": 10, "damping_coefficient": 0.5, "initial_displacement": 1, "initial_velocity": 0, "duration": 10}'
   ```

## Docker Support

To run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t math-physics-platform .
   ```

2. Run the Docker container:
   ```
   docker run -p 8000:8000 math-physics-platform
   ```

The API will be available at `http://localhost:8000`.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or concerns, please open an issue on the GitHub repository.