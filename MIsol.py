x=input("Parolni kiriting:")
if str(x)=="Mexmonov":
    print("Xush kelibsiz Anvar Mexmonov")
    odamlar=[]
    while True:
        odam=input("Login kiriting:")
        if odam in odamlar:
            print("Ushbu login band, iltimos qaytadan urinib ko'ring!")
        else:
            odamlar.append(odam)
            print(f"Xush kelibsiz {odam}")
        if len(odamlar)==15:
            print("Ro'yxat to'lganligi sababli ro'yxatga olish toxtatildi")
            break
            print("Ro'yxat to'lganligi sababli ro'yxatga olish toxtatildi")
else:
    print("Siz Anvar Mexmonovmassiz, dastur siz uchun ishlamaydi")
    
        
        
    
    
