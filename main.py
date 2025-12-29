"""
FastAPI House Pricing API
A high-performance REST API for real estate price estimation using FastAPI and Pydantic validation.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import HouseFeatures, PricePrediction, HealthCheck
from predictor import HousePricePredictor

# API version
API_VERSION = "1.0.0"

# Initialize FastAPI app
app = FastAPI(
    title="House Pricing API",
    description="A high-performance REST API for real estate price estimation using FastAPI and Pydantic validation.",
    version=API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize predictor
predictor = HousePricePredictor()


@app.get("/", response_model=HealthCheck, tags=["Health"])
async def root():
    """
    Root endpoint - Health check.
    
    Returns:
        Health check response with API status and version
    """
    return HealthCheck(status="ok", version=API_VERSION)


@app.get("/health", response_model=HealthCheck, tags=["Health"])
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        Health check response with API status and version
    """
    return HealthCheck(status="ok", version=API_VERSION)


@app.post("/predict", response_model=PricePrediction, tags=["Prediction"])
async def predict_price(features: HouseFeatures):
    """
    Predict house price based on features.
    
    Args:
        features: House features including area, bedrooms, bathrooms, etc.
    
    Returns:
        Price prediction with estimated price, confidence score, and price range
        
    Raises:
        HTTPException: If prediction fails
    """
    try:
        prediction = predictor.predict(features)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


@app.get("/api/info", tags=["Info"])
async def api_info():
    """
    Get API information.
    
    Returns:
        Dictionary with API details
    """
    return {
        "name": "House Pricing API",
        "version": API_VERSION,
        "description": "A high-performance REST API for real estate price estimation",
        "endpoints": {
            "health": "/health - Health check",
            "predict": "/predict - Predict house price (POST)",
            "docs": "/docs - Interactive API documentation",
            "redoc": "/redoc - Alternative API documentation"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
