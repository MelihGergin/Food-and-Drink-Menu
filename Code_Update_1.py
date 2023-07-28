print("\nYEMEK MENÜSÜ SEÇİM PROGRAMINA HOŞ GELDİNİZ..."
      "\n\nLütfen önce yemeğinizi seçiniz."
      "\n1. Hamburger"
      "\n2. Salata"
      "\n3. Makarna")

try:

    a = int(input("Seçilen yemeğin numarası:"))

    print("\n\nLütfen içeceğinizi seçiniz."
          "\n1. Ayran"
          "\n2. Limonata"
          "\n3. Su")

    b = int(input("Seçilen içeceğin numarası:"))

    print("Seçtiğiniz yemek numarası", a, "ve seçtiğiniz içecek numarası", b, ".")

    b3 = input("\nOnaylıyor musunuz?(evet/hayır)")

    if b3 == "evet":
        print("Seçiminiz onaylandı, afiyet olsun.")
        e = input("\nFiş almak ister misiniz?(evet/hayır)")

    elif b3 == "hayır":
        print("Lütfen tekrar seçiniz.")
        c = input("Seçilen yemeğin numarası:")
        d = input("Seçilen içeceğin numarası:")
        print("Seçtiğiniz yemek numarası", c, "ve seçtiğiniz içecek numarası", d, ". Afiyet olsun")
        e = input("\nFiş almak ister misiniz?(evet/hayır)")

    if e == "evet":
        print("\n1. Hamburger"
              "\n2. Salata"
              "\n3. Makarna"
              "\n\n1. Ayran"
              "\n2. Limonata"
              "\n3. Su")
        b1 = int(input("\nSeçilen yemeğin numarası:"))
        b2 = int(input("Seçilen içeceğin numarası:"))
        dosya = open(r"C:\Users\Melih\Desktop\Menü_Fişi.txt", mode="w")
        dosya.write("///////////////////////////////////////////////////////////////////////////////\n")
        dosya.write("\nYiyecekler 1. Hamburger 2. Salata 3. Makarna \nİçecekler 1. Ayran 2. Limonata 3. Su\n\n")
        dosya.write(b1)
        dosya.write(" nolu yiyecek ")
        dosya.write(" ve ")
        dosya.write(b2)
        dosya.write(" nolu içecek ")
        dosya.write("seçimi yapıldı. \n\nMenünüzü teslim alırken fişinizi veriniz. Yine bekleriz... \n16.07.2023 10:00\n")
        dosya.write("\n///////////////////////////////////////////////////////////////////////////////")
        dosya.close()
        print("Yine bekleriz...")

    else:
        print("Fiş oluşturulmadı. Yine bekleriz...")

except:
    print("Hatalı seçim yapıldı...")
