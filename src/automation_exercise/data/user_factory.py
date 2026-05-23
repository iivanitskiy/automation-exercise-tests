import uuid
from dataclasses import dataclass, asdict
from typing import Any

from faker import Faker

faker = Faker()


@dataclass(frozen=True)
class UserData:
    name: str
    email: str
    password: str
    title: str
    birth_date: str
    birth_month: str
    birth_year: str
    firstname: str
    lastname: str
    company: str
    address1: str
    address2: str
    country: str
    zipcode: str
    state: str
    city: str
    mobile_number: str

    def to_api_payload(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def display_name(self) -> str:
        return f"{self.firstname} {self.lastname}"


class UserFactory:
    @staticmethod
    def build(**overrides: Any) -> UserData:
        first = faker.first_name()
        last = faker.last_name()
        defaults = UserData(
            name=f"{first} {last}",
            email=f"qa_{uuid.uuid4().hex[:12]}@autotest.example",
            password=faker.password(length=12, special_chars=True, digits=True, upper_case=True),
            title="Mr",
            birth_date="10",
            birth_month="5",
            birth_year="1990",
            firstname=first,
            lastname=last,
            company=faker.company(),
            address1=faker.street_address(),
            address2=faker.secondary_address(),
            country="Canada",
            zipcode=faker.postcode(),
            state=faker.state(),
            city=faker.city(),
            mobile_number=faker.numerify(text="##########"),
        )
        if not overrides:
            return defaults
        data = defaults.to_api_payload()
        data.update(overrides)
        return UserData(**data)
