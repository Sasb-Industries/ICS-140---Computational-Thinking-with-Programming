def get_federal_taxes(total_pay):
    """
    Receives total pay and returns federal tax amount
    using progressive percentages based on total pay
    The first $200 is taxed at 10%
    The next $600 is taxed at 12%
    The next $1100 is taxed at 22%
    The next $2150 is taxed at 24%
    The next $2000 is taxed at 32%
    The next $8400 is taxed at 35%
    Everything above that is taxed at 37%

    Example $1,000 would be taxed at:
    (200 * .1) + (600 * .12) + (200 * .22)
    OR 20 + 72 + 44 = 136
    """
    pass


def get_state_taxes_mn(total_pay):
    """
    Receives total pay and returns the state tax amount
    using progressive percentages based on total pay.
    The first $540 is taxed at 5.35%
    The next $1200 is taxed at 6.8%
    The next $2000 is taxed at 7.85%
    Everything above that is taxed at 9.85%
    """
    pass

