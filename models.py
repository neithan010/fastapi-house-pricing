"""
Pydantic models for house pricing API.
"""
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class HouseFeatures(BaseModel):
    """Input model for house features."""
    
    area: float = Field(..., gt=0, description="Area of the house in square feet")
    bedrooms: int = Field(..., ge=1, le=10, description="Number of bedrooms")
    bathrooms: float = Field(..., ge=1, le=10, description="Number of bathrooms")
    floors: int = Field(..., ge=1, le=4, description="Number of floors")
    year_built: int = Field(..., ge=1800, le=2025, description="Year the house was built")
    location_score: float = Field(..., ge=0, le=10, description="Location quality score (0-10)")
    condition: int = Field(..., ge=1, le=5, description="Condition of the house (1-5, where 5 is best)")
    
    @field_validator("area")
    @classmethod
    def validate_area(cls, v: float) -> float:
        if v > 50000:
            raise ValueError("Area must be less than 50,000 sq ft")
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "area": 2500,
                "bedrooms": 4,
                "bathrooms": 2.5,
                "floors": 2,
                "year_built": 2010,
                "location_score": 8.5,
                "condition": 4
            }
        }


class PricePrediction(BaseModel):
    """Output model for price prediction."""
    
    estimated_price: float = Field(..., description="Estimated house price in USD")
    confidence_score: float = Field(..., ge=0, le=1, description="Confidence score of the prediction (0-1)")
    price_range_min: float = Field(..., description="Minimum estimated price in USD")
    price_range_max: float = Field(..., description="Maximum estimated price in USD")
    
    class Config:
        json_schema_extra = {
            "example": {
                "estimated_price": 450000,
                "confidence_score": 0.85,
                "price_range_min": 405000,
                "price_range_max": 495000
            }
        }


class HealthCheck(BaseModel):
    """Health check response model."""
    
    status: str = Field(..., description="API status")
    version: str = Field(..., description="API version")
