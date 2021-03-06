import pytest

from funding_circle.parse_statement import statement # pylint: disable=import-error


@pytest.fixture(scope='session')
def test_data():
    data = [
        ['Date', 'Description', 'Paid In', 'Paid Out'],
        ['2000-01-01', 'EPDQ ID: 1234567890 - TRANSFERIN ORDERID: SOME-VALUE', '10000.0', ''],
        ['2000-01-02', 'Loan offer on Working Capital Loan - 12345', '', '20.0'],
        ['2000-01-03', 'Loan offer on Working Capital Loan - 12346', '', '20.0'],
        ['2020-01-04', 'Servicing fee for Loan ID N/A; Loan Part ID 12345678; Investor ID THISISANID', '', '0.01'],
        ['2000-01-04', 'Loan Part ID 12345678 : Principal 18.97, Interest 0.10, Delta 0.00, Fee 0.00', '', '0.1'],
        ['2000-01-04', 'Loan Part ID 12345678 : Principal 18.97, Interest 0.10, Delta 0.00, Fee 0.00', '', '18.97'],
        ['2020-01-05', 'Servicing fee for Loan ID N/A; Loan Part ID 23456789; Investor ID THISISANID', '','0.02'],
        ['2000-01-05', 'Loan Part ID 23456789 : Principal 19.14, Interest 0.26, Delta 0.00, Fee 0.00', '', '0.26'],
        ['2000-01-05', 'Loan Part ID 23456789 : Principal 19.14, Interest 0.26, Delta 0.00, Fee 0.00', '', '19.14'],
        ['2020-01-10', 'Servicing fee for Loan ID N/A; Loan Part ID 34567890; Investor ID THISISANID', '', '0.01'],
        ['2000-01-10', 'Loan Part ID 34567890 : Principal £7.98, Interest £0.01, Transfer Payment £-0.10, Fee £0.00', '', '7.98'],
        ['2000-01-10', 'Loan Part ID 34567890 : Principal £7.98, Interest £0.01, Transfer Payment £-0.10, Fee £0.00', '0.09', ''],
        ['2000-02-01', 'Principal repayment for loan part 12345678', '0.38', ''],
        ['2000-02-01', 'Interest repayment for loan part 12345678', '0.03', ''],
        ['2000-02-02', 'Early principal repayment for loan part 23456789', '0.9', ''],
        ['2000-02-02', 'Early interest repayment for loan part 23456789', '0.01', ''],
        ['2000-02-03', 'Principal recovery repayment for loan part 11223344', '0.07', ''],
        ['2000-12-31', 'EPDQ ID: 0123456789 - TRANSFEROUT ORDERID: A-UNIQUE-VALUE', '', '5000.0'],
    ]

    yield data


@pytest.fixture(scope='session')
def test_statement_location():
    yield 'tests/test_statement.csv'


@pytest.fixture(scope='session')
def test_statement_object(test_data, test_statement_location):
    statement_obj = statement(test_statement_location)
    statement_obj.readFile()

    yield statement_obj
