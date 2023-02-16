


i = 1
while i < 2:

    spisok = []


    for element in elems:
        aroma_names = ["Zesty Tobacco Type Flavor CC", "Wintergreen Flavor"]
        print("clear spisok ")
        spisok.clear()
        print(spisok)

        for name in aroma_names:

            aromas_prices = ["4 = 111$", "gallon = 200$", "case = 400$"]


            for price in aromas_prices:
                prefix = price[0:3]


                if prefix == 'gall':
                    spisok.append(price)
                elif prefix == 'case':
                    spisok.append(price)
                else:
                    print(f"else  {spisok}")
            print(spisok)
            names_list.update({str(name.text): spisok})
            print(spisok)
