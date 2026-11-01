import pytest
from pydantic import ValidationError

from app.schemas import LeadCreate


def test_lead_create_accepts_email_contact():
    lead = LeadCreate(full_name="Ada Lovelace", email="ada@example.com")

    assert lead.full_name == "Ada Lovelace"
    assert lead.email == "ada@example.com"
    assert lead.status == "new"


def test_lead_create_accepts_phone_without_email():
    lead = LeadCreate(full_name="Ada Lovelace", phone="+441234567890")

    assert lead.phone == "+441234567890"
    assert lead.email is None


def test_lead_create_requires_contact_method():
    with pytest.raises(ValidationError):
        LeadCreate(full_name="Ada Lovelace")


def test_lead_create_rejects_invalid_email():
    with pytest.raises(ValidationError):
        LeadCreate(full_name="Ada Lovelace", email="not-an-email")


def test_lead_create_rejects_invalid_status():
    with pytest.raises(ValidationError):
        LeadCreate(
            full_name="Ada Lovelace",
            email="ada@example.com",
            status="pending",
        )
