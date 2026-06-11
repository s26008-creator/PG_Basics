facts = dict()

facts["height"] = "168"
(facts["height"])

facts["eyecolor"] = "black"
(facts["eyecolor"])

facts["nationality"] = "japan"
(facts["nationality"])



ask=input("知りたい特徴を入力してください")
if ask in facts:
    answer=facts[ask]
    print(answer)
else:
    print("それはわかりません")

