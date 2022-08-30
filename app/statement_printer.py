import math


class StatementPrinter:

    def print(self, invoice, plays):
        total_amount = 0
        volume_credits = 0
        result = f'Statement for {invoice.customer}\n'

        for perf in invoice.performances:
            play = plays[perf.play_id]
            if play.play_type == "tragedy":
                this_amount = 40000
                if perf.audience > 30:
                    this_amount += 1000 * (perf.audience - 30)
            elif play.play_type == "comedy":
                this_amount = 30000
                if perf.audience > 20:
                    this_amount += 10000 + 500 * (perf.audience - 20)

                this_amount += 300 * perf.audience

            else:
                raise ValueError(f'unknown type: {play.play_type}')

            # add volume credits
            volume_credits += max(perf.audience - 30, 0)
            # add extra credit for every ten comedy attendees
            if "comedy" == play.play_type:
                volume_credits += math.floor(perf.audience / 5)
            # print line for this order
            result += f' {play.name}: {self.format_as_dollars(this_amount / 100)} ({perf.audience} seats)\n'
            total_amount += this_amount

        result += f'Amount owed is {self.format_as_dollars(total_amount / 100)}\n'
        result += f'You earned {volume_credits} credits\n'
        return result

    def format_as_dollars(self, amount):
        return f"${amount:0,.2f}"
