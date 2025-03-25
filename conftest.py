import pytest

from models import Person, Bank, BankAccount


@pytest.fixture()
def person() -> Person:
    oleg = Person("Oleg")
    return oleg


@pytest.fixture()
def another_person() -> Person:
    oleg = Person("Oleg")
    return oleg


@pytest.fixture()
def bank() -> Bank:
    b = Bank("Mono")
    return b


@pytest.fixture()
def bank2() -> Bank:
    b2 = Bank("Private")
    return b2


@pytest.fixture()
def bank_account(bank, person) -> BankAccount:
    account = bank.open_account(person)
    return account


@pytest.fixture()
def bank_account2(bank2, another_person) -> BankAccount:
    account = bank2.open_account(another_person)
    return account
