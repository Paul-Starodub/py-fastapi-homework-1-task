from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict


class MovieModelBase(BaseModel):
    id: int
    name: str = Field(max_length=255)
    date: date
    score: float
    genre: str = Field(max_length=255)
    overview: str
    crew: str
    orig_title: str = Field(max_length=255)
    status: str = Field(max_length=50)
    orig_lang: str = Field(max_length=50)
    budget: Decimal = Field(max_digits=12, decimal_places=2)
    revenue: float
    country: str = Field(max_length=3)

    model_config = ConfigDict(from_attributes=True, json_encoders={Decimal: float})


class MovieDetailResponseSchema(MovieModelBase):
    pass


class MovieListResponseSchema(MovieModelBase):
    pass
