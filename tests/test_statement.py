import pytest
from approvaltests import verify

from app.invoice import Invoice
from app.performance import Performance
from app.play import Play
from app.statement_printer import StatementPrinter


class TestStatementPrinter:

    def test_statement_printer(self):
        plays = {
            "hamlet": Play("Hamlet", "tragedy"),
            "as-like": Play("As You Like It", "comedy"),
            "othello": Play("Othello", "tragedy")
        }

        performances = [Performance("hamlet", 55),
                        Performance("as-like", 35),
                        Performance("othello", 40)]
        invoice = Invoice("BigCo", performances)
        verify(StatementPrinter().print(invoice, plays))

    def test_new_play_type(self):
        plays = {
            "henry-v": Play("Henry V", "history"),
            "as-like": Play("As You Like It", "pastoral")
        }

        performances = [Performance("henry-v", 53), Performance("as-like", 55)]
        invoice = Invoice("BigCo II", performances)

        with pytest.raises(ValueError) as exception_info:
            StatementPrinter().print(invoice, plays)
        assert "unknown type" in str(exception_info.value)

