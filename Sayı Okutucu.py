def oku(sayi):
    birler = [" ", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = [" ", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

    s = str(sayi)

    sayimiz = (onlar[int(s[0])] + " " + birler[int(s[1])])

    return sayimiz


while True:
    sayi= int(input("İki basamaklı bir sayı giriniz: "))

    print("Okunuşu: ", oku(sayi))