from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.physics_service import (
    simulate_projectile_motion,
    simulate_damped_harmonic_motion,
)

router = APIRouter()


class ProjectileMotionRequest(BaseModel):
    initial_velocity: float
    angle_degrees: float
    gravity: float = 9.8


@router.post("/projectile_motion")
async def projectile_motion(request: ProjectileMotionRequest):
    try:
        plot = simulate_projectile_motion(
            request.initial_velocity, request.angle_degrees, request.gravity
        )
        return {"plot": plot}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


class DampedHarmonicMotionRequest(BaseModel):
    mass: float = Field(..., gt=0, le=1000, description="Mass in kg")
    spring_constant: float = Field(
        ..., gt=0, le=1000, description="Spring constant in N/m"
    )
    damping_coefficient: float = Field(
        ..., ge=0, le=100, description="Damping coefficient in Ns/m"
    )
    initial_displacement: float = Field(..., description="Initial displacement in m")
    initial_velocity: float = Field(..., description="Initial velocity in m/s")
    duration: float = Field(
        ..., gt=0, le=100, description="Simulation duration in seconds"
    )


@router.post("/damped_harmonic_motion")
async def damped_harmonic_motion(request: DampedHarmonicMotionRequest):
    try:
        plot, data = simulate_damped_harmonic_motion(
            request.mass,
            request.spring_constant,
            request.damping_coefficient,
            request.initial_displacement,
            request.initial_velocity,
            request.duration,
        )
        return {"plot": plot, "data": data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
