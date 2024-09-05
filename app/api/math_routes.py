from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.math_service import (
    generate_complex_function_plot,
    generate_fourier_transform,
    solve_differential_equation,
)
from typing import List, Dict


router = APIRouter()


class ComplexFunctionRequest(BaseModel):
    function: str
    x_range: tuple = (-5, 5)
    y_range: tuple = (-5, 5)


@router.post("/complex_function")
async def complex_function(request: ComplexFunctionRequest):
    try:
        plot = generate_complex_function_plot(
            request.function, request.x_range, request.y_range
        )
        return {"plot": plot}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


class FourierTransformRequest(BaseModel):
    signal_type: str = Field(
        ..., description="Type of signal: sine, square, or sawtooth"
    )
    frequency: float = Field(..., gt=0, le=1000, description="Signal frequency in Hz")
    duration: float = Field(..., gt=0, le=10, description="Signal duration in seconds")
    sample_rate: float = Field(1000, gt=0, le=10000, description="Sample rate in Hz")


@router.post("/fourier_transform")
async def fourier_transform(request: FourierTransformRequest):
    try:
        plot, data = generate_fourier_transform(
            request.signal_type,
            request.frequency,
            request.duration,
            request.sample_rate,
        )
        return {"plot": plot, "data": data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


class DifferentialEquationRequest(BaseModel):
    equation_type: str = Field(
        ...,
        description="Type of differential equation: first_order_linear, second_order_linear, or predator_prey",
    )
    parameters: Dict[str, float] = Field(
        ..., description="Parameters for the differential equation"
    )
    initial_conditions: List[float] = Field(..., description="Initial conditions")
    t_span: List[float] = Field(..., description="Time span for the solution")


@router.post("/differential_equation")
async def differential_equation(request: DifferentialEquationRequest):
    try:
        plot, data = solve_differential_equation(
            request.equation_type,
            request.parameters,
            request.initial_conditions,
            request.t_span,
        )
        return {"plot": plot, "data": data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
