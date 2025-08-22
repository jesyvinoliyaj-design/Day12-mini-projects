def calculate_gross(basic, hra=0.2, da=0.1, bonus=0.05):
    hra_amt = basic * hra
    da_amt = basic * da
    bonus_amt = basic * bonus
    return basic + hra_amt + da_amt + bonus_amt
