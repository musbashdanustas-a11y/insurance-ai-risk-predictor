# Insurance AI Risk Predictor - by Mus'ab, Kano

data = [[25,0,0],[45,0,0],[50,1,1],[60,1,1],[30,1,1]]

masu_taba = 0
masu_taba_da_asara = 0

for mutum in data:
    if mutum[1] == 1:
        masu_taba += 1
        if mutum[2] == 1:
            masu_taba_da_asara += 1

yiwuwar = (masu_taba_da_asara / masu_taba) * 100
print(f"Yiwuwar asara: {yiwuwar}%")

shekaru = int(input("Shekarun abokin ciniki? "))
taba = input("Yana shan taba? eh/a'a: ")

if taba.lower() == "eh" and shekaru > 40:
    print("Prediction: HADARI MAI GIRMA! N20000")
elif taba.lower() == "eh":
    print("Prediction: Hadari ne, N10000")
else:
    print("Prediction: Low Risk, N5000")