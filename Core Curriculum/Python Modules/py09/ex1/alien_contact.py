from datetime import datetime
from enum import Enum
# enum (special data type to define a fixed set of named constants) is used to define a set of named values, which can be used to represent the type of contact in the AlienContact model

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"
# these are the possible types of alien contact that can be logged in the AlienContact model
# i can use this enum to restrict the contact_type field in the AlienContact model to only these values


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    # it tells pydantic that the contact_type field must be one of the values defined in the ContactType enum
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    # 24 * 60 = 1440 minutes in a day
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    # or optional[str] = Field(default=None, max_length=500) can also be used to indicate that the message_received field can be either a string or None
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def custom_validation(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with AC"
            )

        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError(
                "Physical contact reports must be verified"
            )

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals require received messages"
            )

        return self
    # @model_validator(mode="after") is a decorator that allows you to define custom validation logic that runs after the built-in validation rules have been applied.
    # This is useful for implementing complex validation rules that depend on multiple fields or require additional checks beyond what can be expressed with simple field constraints.
    # (sometimes your validation rule depends on multiple fields.)


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2026-07-16T12:00:00",
        location="Area 51, Nevada",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    print("Valid contact report:")
    print(f"ID: {valid_contact.contact_id}")
    print(f"Type: {valid_contact.contact_type.value}")
    print(f"Location: {valid_contact.location}")
    print(f"Signal: {valid_contact.signal_strength}/10")
    print(f"Duration: {valid_contact.duration_minutes} minutes")
    print(f"Witnesses: {valid_contact.witness_count}")
    print(f"Message: '{valid_contact.message_received}'")

    print("======================================")

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2026-07-16T13:00:00",
            location="Mars Colony",
            contact_type="telepathic",
            signal_strength=5.0,
            duration_minutes=20,
            witness_count=1,
        )

    except ValidationError as error:
        print("Expected validation error:")
        print(str(error.errors()[0]["msg"]).replace("Value error, ", ""))


if __name__ == "__main__":
    main()
