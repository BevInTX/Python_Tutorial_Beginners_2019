has_high_income = False
has_good_credit = False

#if has_high_income and has_good_credit:
if has_high_income or has_good_credit:
    print("Eligible for loan")

has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")