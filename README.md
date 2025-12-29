# FastAPI House Pricing API

A high-performance REST API for real estate price estimation using FastAPI and Pydantic validation.

## Features

- 🚀 Fast and efficient price prediction API
- ✅ Built with FastAPI for high performance
- 🔒 Strong input validation using Pydantic
- 📊 Confidence scores and price ranges
- 📚 Interactive API documentation (Swagger UI)
- 🎯 Simple rule-based prediction model (easily replaceable with ML models)

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository:
```bash
git clone https://github.com/neithan010/fastapi-house-pricing.git
cd fastapi-house-pricing
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the API

Start the server:
```bash
uvicorn main:app --reload
```

Or run directly:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Health Check
```bash
GET /health
```

#### Get API Information
```bash
GET /api/info
```

#### Predict House Price
```bash
POST /predict
Content-Type: application/json

{
  "area": 2500,
  "bedrooms": 4,
  "bathrooms": 2.5,
  "floors": 2,
  "year_built": 2010,
  "location_score": 8.5,
  "condition": 4
}
```

### Example Request

Using cURL:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "area": 2500,
    "bedrooms": 4,
    "bathrooms": 2.5,
    "floors": 2,
    "year_built": 2010,
    "location_score": 8.5,
    "condition": 4
  }'
```

Using Python:
```python
import requests

url = "http://localhost:8000/predict"
data = {
    "area": 2500,
    "bedrooms": 4,
    "bathrooms": 2.5,
    "floors": 2,
    "year_built": 2010,
    "location_score": 8.5,
    "condition": 4
}

response = requests.post(url, json=data)
print(response.json())
```

### Example Response

```json
{
  "estimated_price": 487500.0,
  "confidence_score": 0.95,
  "price_range_min": 438750.0,
  "price_range_max": 536250.0
}
```

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Input Parameters

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| area | float | > 0 | Area of the house in square feet |
| bedrooms | int | 1-10 | Number of bedrooms |
| bathrooms | float | 1-10 | Number of bathrooms |
| floors | int | 1-4 | Number of floors |
| year_built | int | 1800-2025 | Year the house was built |
| location_score | float | 0-10 | Location quality score (0-10) |
| condition | int | 1-5 | Condition of the house (1-5, where 5 is best) |

## Output

| Field | Type | Description |
|-------|------|-------------|
| estimated_price | float | Estimated house price in USD |
| confidence_score | float | Confidence score of the prediction (0-1) |
| price_range_min | float | Minimum estimated price in USD |
| price_range_max | float | Maximum estimated price in USD |

## Project Structure

```
fastapi-house-pricing/
├── main.py           # FastAPI application and endpoints
├── models.py         # Pydantic models for request/response
├── predictor.py      # Price prediction logic
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Extending the Model

The current implementation uses a simple rule-based model for price prediction. To integrate a machine learning model:

1. Train your model (e.g., using scikit-learn, XGBoost, or TensorFlow)
2. Save the trained model to a file
3. Update `predictor.py` to load and use your trained model
4. Adjust the `predict()` method to use your model's prediction logic

Example:
```python
import joblib

class HousePricePredictor:
    def __init__(self):
        self.model = joblib.load('trained_model.pkl')
    
    def predict(self, features: HouseFeatures) -> PricePrediction:
        # Convert features to model input format
        X = self._prepare_features(features)
        prediction = self.model.predict(X)
        # Return formatted prediction
        ...
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
