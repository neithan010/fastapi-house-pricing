"""
House price prediction logic.
This is a simplified model for demonstration purposes.
In a production environment, this would be replaced with a trained ML model.
"""
from datetime import datetime
from models import HouseFeatures, PricePrediction


class HousePricePredictor:
    """Simple rule-based house price predictor."""
    
    def __init__(self):
        # Base price per square foot
        self.base_price_per_sqft = 150
        
        # Multipliers for different features
        self.bedroom_value = 15000
        self.bathroom_value = 10000
        self.floor_value = 5000
        self.location_multiplier = 0.05  # 5% per location point
        self.condition_multiplier = 0.02  # 2% per condition point
        
        # Age depreciation (per year after 2020)
        self.new_home_bonus = 1.1  # 10% bonus for homes built after 2020
        self.age_depreciation = 0.002  # 0.2% per year for older homes
    
    def predict(self, features: HouseFeatures) -> PricePrediction:
        """
        Predict house price based on features.
        
        Args:
            features: House features
            
        Returns:
            Price prediction with confidence score and range
        """
        # Base calculation
        base_price = features.area * self.base_price_per_sqft
        
        # Add value for rooms
        room_value = (features.bedrooms * self.bedroom_value + 
                     features.bathrooms * self.bathroom_value +
                     features.floors * self.floor_value)
        
        # Calculate age factor
        current_year = datetime.now().year
        age = current_year - features.year_built
        if features.year_built >= 2020:
            age_factor = self.new_home_bonus
        else:
            age_factor = max(0.7, 1 - (age * self.age_depreciation))
        
        # Location premium
        location_factor = 1 + (features.location_score * self.location_multiplier)
        
        # Condition premium
        condition_factor = 1 + ((features.condition - 3) * self.condition_multiplier)
        
        # Calculate final price
        estimated_price = (base_price + room_value) * age_factor * location_factor * condition_factor
        
        # Calculate confidence score based on feature reasonableness
        confidence = self._calculate_confidence(features)
        
        # Calculate price range (±10% based on confidence)
        uncertainty = 0.1 + (0.1 * (1 - confidence))
        price_range_min = estimated_price * (1 - uncertainty)
        price_range_max = estimated_price * (1 + uncertainty)
        
        return PricePrediction(
            estimated_price=round(estimated_price, 2),
            confidence_score=round(confidence, 2),
            price_range_min=round(price_range_min, 2),
            price_range_max=round(price_range_max, 2)
        )
    
    def _calculate_confidence(self, features: HouseFeatures) -> float:
        """
        Calculate confidence score based on feature values.
        Higher confidence for typical houses, lower for unusual ones.
        """
        confidence = 1.0
        
        # Penalize very large or very small houses
        if features.area > 5000 or features.area < 500:
            confidence -= 0.1
        
        # Penalize unusual bedroom/area ratios
        bedrooms_per_1000sqft = features.bedrooms / (features.area / 1000)
        if bedrooms_per_1000sqft > 3 or bedrooms_per_1000sqft < 0.5:
            confidence -= 0.1
        
        # Penalize very old houses
        current_year = datetime.now().year
        age = current_year - features.year_built
        if age > 100:
            confidence -= 0.15
        
        # Boost confidence for good location and condition
        if features.location_score >= 7 and features.condition >= 4:
            confidence += 0.05
        
        return max(0.5, min(1.0, confidence))
