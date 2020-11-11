
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, choices=["diff", "annuity"])
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
p = args.principal
n = args.periods
i = args.interest
a = args.payment

arguments = [p, n, i, a, args.type]
arguments_f = [i for i in arguments if i is not None]

continue_ = True

if len(arguments_f) < 4:
    continue_ = False

if args.type == "diff" and a is not None:
    continue_ = False

if i is None:
    continue_ = False

if continue_:

    calc_type = [arguments.index(i) for i in arguments if i is None]
    types = ["p", "n", "i", "a"]
    calc_type = types[calc_type[0]]

    interest = (i / 100) / 12
    principal = 0
    period = 0
    annuity = 0

    if args.type == "annuity":
        if calc_type == "p":
            x = interest * (1 + interest) ** n
            y = (1 + interest) ** n - 1
            z = x / y
            principal = int(a / z)
            print(f"Your loan principal = {principal}!")
            print()
            print(f"Overpayment = {a * n - principal}")
        elif calc_type == "n":
            x = a - interest * p
            y = a / x
            period = math.ceil(math.log(y, interest + 1))
            if period < 12:
                print(f"It will take 11 {'months' if period > 1 else 'month'} to repay this loan!")
            else:
                years = period // 12
                months = period % 12
                if months != 0:
                    print(f"It will take {years} {'years' if years > 1 else 'year'} and \
        {months} {'months' if period > 1 else 'month'} to repay this loan!")
                else:
                    print(f"It will take {years} {'years' if years > 1 else 'year'} to repay this loan!")
            print(f"Overpayment = {int(a * period - p)}")
        else:
            x = interest * (1 + interest) ** n
            y = (1 + interest) ** n - 1
            z = x / y
            annuity = math.ceil(p * z)
            print(f"Your monthly payment = {annuity}!")
            print(f"Overpayment = {int(annuity * n - p)}")

    else:
        ov = []
        for m in range(n):
            s1 = p * m
            s2 = s1 / n
            s3 = p - s2
            s4 = interest * s3
            s5 = p / n
            d = s5 + s4
            ov.append(math.ceil(d))
            print(f"Month {m + 1}: payment is {math.ceil(d)}")

        print("")
        print(f"Overpayment = {int(sum(ov) - p)}")
else:
    print("Incorrect parameters")
