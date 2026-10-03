from datetime import datetime
# datetime is used to represent the last maintenance date of the space station
# and pydantic be able to convert the string representation of the date into a
# datetime object

from pydantic import BaseModel, Field, ValidationError
from typing import Optional
# Pydantic is used for data validation and settings management using Python
# type annotations
# BaseModel is the base class for creating data models so that we can define
# the structure and validation rules for our data
# Field is used to lets you put validation rules on your attributes


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)
# Optional[str] indicates that the notes field can be either a string or None


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    station = SpaceStation.model_validate({
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2026-09-20T23:30:00",
        "notes": "Konnichiwa!"
    })

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Not Operational"
    print(f"Status: {status}")

    print("========================================")

    try:
        SpaceStation.model_validate({
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 25,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2026-07-24T23:30:00"
        })
    except ValidationError as e:
        print("Expected validation error:")
        print(e)
# This is the error type Pydantic raises when the data doesn't satisfy the
# rules


if __name__ == "__main__":
    main()

# pip install pydantic
# Pydantic can automatically convert compatible input data into the type you
# declared in your model.
# Important: Pydantic doesn't blindly convert anything into anything. The input
# has to be compatible with the expected type format.
# "2026-09-20T23:30:00"
#         ↓
#      Pydantic
#         ↓
# datetime(2026, 9, 20, 23, 30, 0)
