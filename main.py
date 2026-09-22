# Insurance AI V2 - 1000 Customers
# Built with 4GB phone in Kaduna

import random

print("--- AI na Kaduna na nazarin mutane 1000 ---")

masu_taba = 0
masu_taba_claim = 0
basa_taba_claim = 0

for i in range(1000):
    age = random.randint(18, 75)
    smoker = random.choice([0, 1])
    
    if smoker == 1 and age > 45:
        claim = 1 if random.random() > 0.3 else 0
    elif smoker == 1:
        claim = 1 if random.random() > 0.6 else 0
    else:
        claim = 1 if random.random() > 0.8 else 0

    if smoker == 1:
        masu_taba += 1
        if claim == 1:
            masu_taba_claim += 1
    else:
        basa_taba += 1
        if claim == 1:
            basa_taba_claim += 1

risk_taba = (masu_taba_claim / masu_taba) * 100
risk_babu = (basa_taba_claim / basa_taba) * 100

print(f"Masu taba: {masu_taba}")
print(f"Masu taba da suka yi claim: {masu_taba_claim}")
print(f"Hadarin masu taba: {risk_taba:.1f}%")
print(f"Hadarin marasa taba: {risk_babu:.1f}%")
print(f"\nKammalawa: Masu taba sun fi hadari sau {risk_taba/risk_babu:.1f}!")
print("Wannan shine logic da kamfanin inshora ke amfani dashi!")