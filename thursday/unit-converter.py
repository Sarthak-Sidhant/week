#create a programme to convert units of weight, length, temperature and volume
def yesorno():
    print("Do you want to convert another unit?")
    print("Type 'yes' or 'no'")
    answer = input()
    if answer == "yes":
        conversion()
    elif answer == "no":
        print("Thank you for using this programme")
    else:
        print("Please type 'yes' or 'no'")
        yesorno()

def conversion():
    unit=input("what unit do you want to convert? length, weight, temperature or volume? ")
    if unit=="weight":
        weight=input("what weight do you want to convert? kilogram, gram, pound, ounce, tonne, milligram, microgram or stone? ")
        if weight=="kilogram":
            kilogram=float(input("enter the value of kilogram "))
            gram=kilogram*1000
            pound=kilogram*2.20462
            ounce=kilogram*35.274
            tonne=kilogram/1000
            milligram=kilogram*1000000
            microgram=kilogram*1000000000
            stone=kilogram*0.157473
            print("gram=",gram)
            print("pound=",pound)
            print("ounce=",ounce)
            print("tonne=",tonne)
            print("milligram=",milligram)
            print("microgram=",microgram)
            print("stone=",stone)
            yesorno()
        elif weight=="gram":
            gram=float(input("enter the value of gram "))
            kilogram=gram/1000
            pound=gram*0.00220462
            ounce=gram*0.035274
            tonne=gram/1000000
            milligram=gram*1000
            microgram=gram*1000000
            stone=gram*0.000157473
            print("kilogram=",kilogram)
            print("pound=",pound)
            print("ounce=",ounce)
            print("tonne=",tonne)
            print("milligram=",milligram)
            print("microgram=",microgram)
            print("stone=",stone)
            yesorno()
        elif weight=="pound":
            pound=float(input("enter the value of pound "))
            kilogram=pound*0.453592
            gram=pound*453.592
            ounce=pound*16
            tonne=pound*0.000453592
            milligram=pound*453592
            microgram=pound*453592000
            stone=pound*0.0714286
            print("kilogram=",kilogram)
            print("gram=",gram)
            print("ounce=",ounce)
            print("tonne=",tonne)
            print("milligram=",milligram)
            print("microgram=",microgram)
            print("stone=",stone)
            yesorno()
        elif weight=="ounce":
            ounce=float(input("enter the value of ounce "))
            kilogram=ounce*0.0283495
            gram=ounce*28.3495
            pound=ounce*0.0625
            tonne=ounce*0.0000283495
            milligram=ounce*28349.5
            microgram=ounce*28349500
            stone=ounce*0.00446429
            print("kilogram=",kilogram)
            print("gram=",gram)
            print("pound=",pound)
            print("tonne=",tonne)
            print("milligram=",milligram)
            print("microgram=",microgram)
            print("stone=",stone)
            yesorno()   
        elif weight=="tonne":
            tonne=float(input("enter the value of tonne "))
            kilogram=tonne*1000
            gram=tonne*1000000
            pound=tonne*2204.62
            ounce=tonne*35274
            milligram=tonne*1000000000
            microgram=tonne*1000000000000
            stone=tonne*157.473
            print("kilogram=",kilogram)
            print("gram=",gram)
            print("pound=",pound)
            print("ounce=",ounce)
            print("milligram=",milligram)
            print("microgram=",microgram)
            print("stone=",stone)
            yesorno()
        elif weight=="milligram":
            milligram=float(input("enter the value of milligram "))
            kilogram=milligram*0.000001
            gram=milligram*0.001
            pound=milligram*0.00000220462
            ounce=milligram*0.000035274
            tonne=milligram*0.000000001
            microgram=milligram*1000
            stone=milligram*0.000000157473
            print("kilogram=",kilogram)
            print("gram=",gram)
            print("pound=",pound)
            print("ounce=",ounce)
            print("tonne=",tonne)
            print("microgram=",microgram)
            print("stone=",stone)
            yesorno()
        elif weight=="microgram":
            microgram=float(input("enter the value of microgram "))
            kilogram=microgram*0.000000001
            gram=microgram*0.000001
            pound=microgram*0.00000000220462
            ounce=microgram*0.000000035274
            tonne=microgram*0.000000000001
            milligram=microgram*0.001
            stone=microgram*0.000000000157473
            print("kilogram=",kilogram)
            print("gram=",gram)
            print("pound=",pound)
            print("ounce=",ounce)
            print("tonne=",tonne)
            print("milligram=",milligram)
            print("stone=",stone)
            yesorno()
        elif weight=="stone":
            stone=float(input("enter the value of stone "))
            kilogram=stone*6.35029
            gram=stone*6350.29
            pound=stone*14
            ounce=stone*224
            tonne=stone*0.00635029
            milligram=stone*6350290
            microgram=stone*6350290000
            print("kilogram=",kilogram)
            print("gram=",gram)
            print("pound=",pound)
            print("ounce=",ounce)
            print("tonne=",tonne)
            print("milligram=",milligram)
            print("microgram=",microgram)
            yesorno()
        else:
            print("invalid input")
    elif unit=="length":
        length=input("what length do you want to convert? meter, centimeter, kilometer, millimeter, micrometer, nanometer, mile, yard, foot, inch, nautical mile or light year? ")
        if length=="meter":
            meter=float(input("enter the value of meter "))
            centimeter=meter*100
            kilometer=meter/1000
            millimeter=meter*1000
            micrometer=meter*1000000
            nanometer=meter*1000000000
            mile=meter*0.000621371
            yard=meter*1.09361
            foot=meter*3.28084
            inch=meter*39.3701
            nauticalmile=meter*0.000539957
            lightyear=meter*0.0000000000000001057
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("yard=",yard)
            print("foot=",foot)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="centimeter":
            centimeter=float(input("enter the value of centimeter "))
            meter=centimeter/100
            kilometer=centimeter/100000
            millimeter=centimeter*10
            micrometer=centimeter*10000
            nanometer=centimeter*10000000
            mile=centimeter*0.00000621371
            yard=centimeter*0.0109361
            foot=centimeter*0.0328084
            inch=centimeter*0.393701
            nauticalmile=centimeter*0.00000539957
            lightyear=centimeter*0.000000000000000001057
            print("meter=",meter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("yard=",yard)
            print("foot=",foot)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="kilometer":
            kilometer=float(input("enter the value of kilometer "))
            meter=kilometer*1000
            centimeter=kilometer*100000
            millimeter=kilometer*1000000
            micrometer=kilometer*1000000000
            nanometer=kilometer*1000000000000
            mile=kilometer*0.621371
            yard=kilometer*1093.61
            foot=kilometer*3280.84
            inch=kilometer*39370.1
            nauticalmile=kilometer*0.539957
            lightyear=kilometer*0.0000000000001057
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("yard=",yard)
            print("foot=",foot)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="millimeter":
            millimeter=float(input("enter the value of millimeter "))
            meter=millimeter/1000
            centimeter=millimeter/10
            kilometer=millimeter/1000000
            micrometer=millimeter*1000
            nanometer=millimeter*1000000
            mile=millimeter*0.000000621371
            yard=millimeter*0.00109361
            foot=millimeter*0.00328084
            inch=millimeter*0.0393701
            nauticalmile=millimeter*0.000000539957
            lightyear=millimeter*0.000000000000000000001057
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("yard=",yard)
            print("foot=",foot)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="micrometer":
            micrometer=float(input("enter the value of micrometer "))
            meter=micrometer/1000000
            centimeter=micrometer/10000
            kilometer=micrometer/1000000000
            millimeter=micrometer/1000
            nanometer=micrometer*1000
            mile=micrometer*0.000000000621371
            yard=micrometer*0.00000109361
            foot=micrometer*0.00000328084
            inch=micrometer*0.0000393701
            nauticalmile=micrometer*0.000000000539957
            lightyear=micrometer*0.000000000000000000000001057
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("yard=",yard)
            print("foot=",foot)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="nanometer":
            nanometer=float(input("enter the value of nanometer "))
            meter=nanometer/1000000000
            centimeter=nanometer/10000000
            kilometer=nanometer/1000000000000
            millimeter=nanometer/1000000
            micrometer=nanometer/1000
            mile=nanometer*0.000000000000621371
            yard=nanometer*0.00000000109361
            foot=nanometer*0.00000000328084
            inch=nanometer*0.0000000393701
            nauticalmile=nanometer*0.000000000000539957
            lightyear=nanometer*0.000000000000000000000000001057
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("mile=",mile)
            print("yard=",yard)
            print("foot=",foot)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="mile":
            mile=float(input("enter the value of mile "))
            meter=mile*1609.34
            centimeter=mile*160934
            kilometer=mile*1.60934
            millimeter=mile*1609340
            micrometer=mile*1609340000
            nanometer=mile*1609340000000
            yard=mile*1760
            foot=mile*5280
            inch=mile*63360
            nauticalmile=mile*0.868976
            lightyear=mile*0.0000000000000000001057
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("yard=",yard)
            print("foot=",foot)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="yard":
            yard=float(input("enter the value of mile "))
            meter=yard*0.9144
            centimeter=yard*91.44
            kilometer=yard*0.0009144
            millimeter=yard*914.4
            micrometer=yard*914400
            nanometer=yard*914400000
            mile=yard*0.000568182
            foot=yard*3
            inch=yard*36
            nauticalmile=yard*0.000493737
            lightyear=yard*0.0000000000000000966522
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("foot=",foot)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="foot":
            foot=float(input("enter the value of foot "))
            meter=foot*0.3048
            centimeter=foot*30.48
            kilometer=foot*0.0003048
            millimeter=foot*304.8
            micrometer=foot*304800
            nanometer=foot*304800000
            mile=foot*0.000189394
            yard=foot*0.333333
            inch=foot*12
            nauticalmile=foot*0.000164579
            lightyear=foot*0.0000000000000000322174
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("yard=",yard)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="inch":
            inch=float(input("enter the value of inch "))
            meter=inch*0.0254
            centimeter=inch*2.54
            kilometer=inch*0.0000254
            millimeter=inch*25.4
            micrometer=inch*25400
            nanometer=inch*25400000
            mile=inch*0.0000157828
            yard=inch*0.0277778
            foot=inch*0.0833333
            nauticalmile=inch*0.0000137151
            lightyear=inch*0.00000000000000000268478
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("yard=",yard)
            print("foot=",foot)
            print("nauticalmile=",nauticalmile)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="nauticalmile":
            nauticalmile=float(input("enter the value of nautical mile "))
            meter=nauticalmile*1852
            centimeter=nauticalmile*185200
            kilometer=nauticalmile*1.852
            millimeter=nauticalmile*1852000
            micrometer=nauticalmile*1852000000
            nanometer=nauticalmile*1852000000000
            mile=nauticalmile*1.15078
            yard=nauticalmile*2025.37
            foot=nauticalmile*6076.12
            inch=nauticalmile*72913.4
            lightyear=0.000000000000195757
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("yard=",yard)
            print("foot=",foot)
            print("inch=",inch)
            print("lightyear=",lightyear)
            yesorno()
        elif length=="lightyear":
            lightyear=float(input("enter the value of lightyear "))
            meter=lightyear*9460730472580800
            centimeter=lightyear*946073047258080000
            kilometer=lightyear*9460730472580.8
            millimeter=lightyear*9460730472580800000
            micrometer=lightyear*9460730472580800000000
            nanometer=lightyear*9460730472580800000000000
            mile=lightyear*5878625373183.1
            yard=lightyear*10346389259526000
            foot=lightyear*31039167778578000
            inch=lightyear*372471614531336000
            nauticalmile=lightyear*5100720000000
            print("meter=",meter)
            print("centimeter=",centimeter)
            print("kilometer=",kilometer)
            print("millimeter=",millimeter)
            print("micrometer=",micrometer)
            print("nanometer=",nanometer)
            print("mile=",mile)
            print("yard=",yard)
            print("foot=",foot)
            print("inch=",inch)
            print("nauticalmile=",nauticalmile)
            yesorno()
        else:
            print("invalid input")
    elif unit=="volume":
        volume=input("enter the volume unit ")
        if volume=="cubicmeter":
            cubicmeter=float(input("enter the value of cubic meter "))
            cubiccentimeter=cubicmeter*1000000
            cubicmillimeter=cubicmeter*1000000000
            cubicfoot=cubicmeter*35.3147
            cubicinch=cubicmeter*61023.7
            liter=cubicmeter*1000
            milliliter=cubicmeter*1000000
            gallon=cubicmeter*264.172
            quart=cubicmeter*1056.69
            pint=cubicmeter*2113.38
            cup=cubicmeter*4226.75
            fluidounce=cubicmeter*33814
            tablespoon=cubicmeter*67628
            teaspoon=cubicmeter*202884
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="cubiccentimeter":
            cubiccentimeter=float(input("enter the value of cubic centimeter "))
            cubicmeter=cubiccentimeter*0.000001
            cubicmillimeter=cubiccentimeter*1000
            cubicfoot=cubiccentimeter*0.0000353147
            cubicinch=cubiccentimeter*0.0610237
            liter=cubiccentimeter*0.001
            milliliter=cubiccentimeter*1
            gallon=cubiccentimeter*0.000264172
            quart=cubiccentimeter*0.00105669
            pint=cubiccentimeter*0.00211338
            cup=cubiccentimeter*0.00422675
            fluidounce=cubiccentimeter*0.033814
            tablespoon=cubiccentimeter*0.067628
            teaspoon=cubiccentimeter*0.202884
            print("cubicmeter=",cubicmeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="cubicmillimeter":
            cubicmillimeter=float(input("enter the value of cubic millimeter "))
            cubicmeter=cubicmillimeter*0.000000001
            cubiccentimeter=cubicmillimeter*0.001
            cubicfoot=cubicmillimeter*0.0000000353147
            cubicinch=cubicmillimeter*0.0000610237
            liter=cubicmillimeter*0.000001
            milliliter=cubicmillimeter*0.001
            gallon=cubicmillimeter*0.000000264172
            quart=cubicmillimeter*0.00000105669
            pint=cubicmillimeter*0.00000211338
            cup=cubicmillimeter*0.00000422675
            fluidounce=cubicmillimeter*0.000033814
            tablespoon=cubicmillimeter*0.000067628
            teaspoon=cubicmillimeter*0.000202884
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="cubicfoot":
            cubicfoot=float(input("enter the value of cubic foot "))
            cubicmeter=cubicfoot*0.0283168
            cubiccentimeter=cubicfoot*28316.8
            cubicmillimeter=cubicfoot*28316800
            cubicinch=cubicfoot*1728
            liter=cubicfoot*28.3168
            milliliter=cubicfoot*28316.8
            gallon=cubicfoot*7.48052
            quart=cubicfoot*29.9221
            pint=cubicfoot*59.8442
            cup=cubicfoot*119.688
            fluidounce=cubicfoot*957.506
            tablespoon=cubicfoot*1915.01
            teaspoon=cubicfoot*5745.03
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="cubicinch":
            cubicinch=float(input("enter the value of cubic inch "))
            cubicmeter=cubicinch*0.0000163871
            cubiccentimeter=cubicinch*16.3871
            cubicmillimeter=cubicinch*16387.1
            cubicfoot=cubicinch*0.000578704
            liter=cubicinch*0.0163871
            milliliter=cubicinch*16.3871
            gallon=cubicinch*0.004329
            quart=cubicinch*0.017316
            pint=cubicinch*0.034632
            cup=cubicinch*0.069264
            fluidounce=cubicinch*0.554113
            tablespoon=cubicinch*1.10823
            teaspoon=cubicinch*3.32469
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="liter":
            liter=float(input("enter the value of liter "))
            cubicmeter=liter*0.001
            cubiccentimeter=liter*1000
            cubicmillimeter=liter*1000000
            cubicfoot=liter*0.0353147
            cubicinch=liter*61.0237
            milliliter=liter*1000
            gallon=liter*0.264172
            quart=liter*1.05669
            pint=liter*2.11338
            cup=liter*4.22675
            fluidounce=liter*33.814
            tablespoon=liter*67.628
            teaspoon=liter*202.884
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="milliliter":
            milliliter=float(input("enter the value of milliliter "))
            cubicmeter=milliliter*0.000001
            cubiccentimeter=milliliter*1
            cubicmillimeter=milliliter*1000
            cubicfoot=milliliter*0.0000353147
            cubicinch=milliliter*0.0610237
            liter=milliliter*0.001
            gallon=milliliter*0.000264172
            quart=milliliter*0.00105669
            pint=milliliter*0.00211338
            cup=milliliter*0.00422675
            fluidounce=milliliter*0.033814
            tablespoon=milliliter*0.067628
            teaspoon=milliliter*0.202884
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="gallon":
            gallon=float(input("enter the value of gallon "))
            cubicmeter=gallon*0.00378541
            cubiccentimeter=gallon*3785.41
            cubicmillimeter=gallon*3785410
            cubicfoot=gallon*0.133681
            cubicinch=gallon*231
            liter=gallon*3.78541
            milliliter=gallon*3785.41
            quart=gallon*4
            pint=gallon*8
            cup=gallon*16
            fluidounce=gallon*128
            tablespoon=gallon*256
            teaspoon=gallon*768
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="quart":
            quart=float(input("enter the value of quart "))
            cubicmeter=quart*0.000946353
            cubiccentimeter=quart*946.353
            cubicmillimeter=quart*946353
            cubicfoot=quart*0.0334201
            cubicinch=quart*57.75
            liter=quart*0.946353
            milliliter=quart*946.353
            gallon=quart*0.25
            pint=quart*2
            cup=quart*4
            fluidounce=quart*32
            tablespoon=quart*64
            teaspoon=quart*192
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="pint":
            pint=float(input("enter the value of pint "))
            cubicmeter=pint*0.000473176
            cubiccentimeter=pint*473.176
            cubicmillimeter=pint*473176
            cubicfoot=pint*0.0167101
            cubicinch=pint*28.875
            liter=pint*0.473176
            milliliter=pint*473.176
            gallon=pint*0.125
            quart=pint*0.5
            cup=pint*2
            fluidounce=pint*16
            tablespoon=pint*32
            teaspoon=pint*96
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="cup":
            cup=float(input("enter the value of cup "))
            cubicmeter=cup*0.000236588
            cubiccentimeter=cup*236.588
            cubicmillimeter=cup*236588
            cubicfoot=cup*0.00835504
            cubicinch=cup*14.4375
            liter=cup*0.236588
            milliliter=cup*236.588
            gallon=cup*0.0625
            quart=cup*0.25
            pint=cup*0.5
            fluidounce=cup*8
            tablespoon=cup*16
            teaspoon=cup*48
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="fluidounce":
            fluidounce=float(input("enter the value of fluidounce "))
            cubicmeter=fluidounce*0.0000295735
            cubiccentimeter=fluidounce*29.5735
            cubicmillimeter=fluidounce*29573.5
            cubicfoot=fluidounce*0.00104084
            cubicinch=fluidounce*1.80469
            liter=fluidounce*0.0295735
            milliliter=fluidounce*29.5735
            gallon=fluidounce*0.0078125
            quart=fluidounce*0.03125
            pint=fluidounce*0.0625
            cup=fluidounce*0.125
            tablespoon=fluidounce*2
            teaspoon=fluidounce*6
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="tablespoon":
            tablespoon=float(input("enter the value of tablespoon "))
            cubicmeter=tablespoon*0.0000147868
            cubiccentimeter=tablespoon*14.7868
            cubicmillimeter=tablespoon*14786.8
            cubicfoot=tablespoon*0.00052042
            cubicinch=tablespoon*0.902344
            liter=tablespoon*0.0147868
            milliliter=tablespoon*14.7868
            gallon=tablespoon*0.00390625
            quart=tablespoon*0.015625
            pint=tablespoon*0.03125
            cup=tablespoon*0.0625
            fluidounce=tablespoon*0.5
            teaspoon=tablespoon*3
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        elif volume=="teaspoon":
            teaspoon=float(input("enter the value of teaspoon "))
            cubicmeter=teaspoon*0.00000492892
            cubiccentimeter=teaspoon*4.92892
            cubicmillimeter=teaspoon*4928.92
            cubicfoot=teaspoon*0.000173473
            cubicinch=teaspoon*0.300781
            liter=teaspoon*0.00492892
            milliliter=teaspoon*4.92892
            gallon=teaspoon*0.00130208
            quart=teaspoon*0.00520833
            pint=teaspoon*0.0104167
            cup=teaspoon*0.0208333
            fluidounce=teaspoon*0.166667
            tablespoon=teaspoon*0.333333
            print("cubicmeter=",cubicmeter)
            print("cubiccentimeter=",cubiccentimeter)
            print("cubicmillimeter=",cubicmillimeter)
            print("cubicfoot=",cubicfoot)
            print("cubicinch=",cubicinch)
            print("liter=",liter)
            print("milliliter=",milliliter)
            print("gallon=",gallon)
            print("quart=",quart)
            print("pint=",pint)
            print("cup=",cup)
            print("fluidounce=",fluidounce)
            print("tablespoon=",tablespoon)
            print("teaspoon=",teaspoon)
            yesorno()
        else:
            print("invalid input")
    elif unit=="temperature":
        temperature=input("enter the temperature unit ")
        if temperature=="celsius":
            celsius=float(input("enter the value of celsius "))
            fahrenheit=(celsius*1.8)+32
            kelvin=celsius+273.15
            print("fahrenheit=",fahrenheit)
            print("kelvin=",kelvin)
            yesorno()
        elif temperature=="fahrenheit":
            fahrenheit=float(input("enter the value of fahrenheit "))
            celsius=(fahrenheit-32)/1.8
            kelvin=celsius+273.15
            print("celsius=",celsius)
            print("kelvin=",kelvin)
            yesorno()
        elif temperature=="kelvin":
            kelvin=float(input("enter the value of kelvin "))
            celsius=kelvin-273.15
            fahrenheit=(celsius*1.8)+32
            print("celsius=",celsius)
            print("fahrenheit=",fahrenheit)
            yesorno()
        else:
            print("invalid input")



#903 lines of code? HEH
