from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator


LeadStatus = Literal[
    "new",
    "contacted",
    "qualified",
    "converted",
    "lost",
]


class LeadCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    full_name: str = Field(min_length=2, max_length=120)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=30)
    company: str | None = Field(default=None, max_length=150)
    source: str | None = Field(default=None, max_length=100)
    status: LeadStatus = "new"
    notes: str | None = None

    @model_validator(mode="after")
    def validate_contact_information(self):
        if not self.email and not self.phone:
            raise ValueError(
                "At least one contact method (email or phone) is required."
            )
        return self


class LeadRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    email: EmailStr | None
    phone: str | None
    company: str | None
    source: str | None
    status: LeadStatus
    notes: str | None
    created_at: datetime
    updated_at: datetime
