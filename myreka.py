import time
print("--------------------------------------------------")
#Welcome the user
print("SELAMAT DATANG KE KUIZ ASK !")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("Anda boleh memilih satu", chances,"jawapan betul.\nAnda akan dapat 1 markah sekiranya jawapan anda betul.\n")
time.sleep(2)

#markah
markah=0

#question 1
print("==================================================")
soalan_1=print("1) BERAPAKAH TEKNIK DALAM PEMIKIRAN KOMPUTASIONAL?\n(A) 1\n(B) 2\n(C) 3\n(D) 4\n\n")
jawapan_1= "D"

for i in range(chances):
    jawapan = input("JAWAPAN: ")
    if (jawapan.lower() == jawapan_1):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        markah = markah + 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN SEBENAR IALAH:", jawapan_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
soalan_2 = print("2) BERAPAKAH TATACARA PENAMBAHAN DUA NOMBOR PERDUAAN?\n(A) 1\n(B) 2\n(C) 3\n(D) 4\n\n")  
jawapan_2 = "B"

for i in range(chances):
    jawapan = input("jawapan: ")
    if (jawapan.lower() == jawapan_2):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        markah = markah + 1
        break
    else:
        print("SALAH!\n ")
        time.sleep(0.5)
        print("JAWAPAN SEBENAR IALAH:", jawapan_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
soalan_3 =print("3)  JENIS FAIL AUDIO YANG MANAKAH DALAM BENTUK MAMPATAN?\n(A) MP3\n(B) MIDI\n(C) BMP\n(D) WAVE\n\n")
jawapan_3= "A"

for i in range(chances):
    jawapan = input("Jawapan: ")
    if ( jawapan.lower() ==  jawapan_3):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        markah = markah + 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN SEBENAR IALAH:", jawapan_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
soalan_4 =print("4)  APAKAH ELEMEN YANG TERKECIL UNTUK PAPARAN IMEJ DIGITAL DI SKRIN KOMPUTER?\n(A) RESOLUSI\n(B) BIT\n(C) PIKSEL\n(D) DIMENSI\n\n")
jawapan_4= "C"

for i in range(chances):
    jawapan = input("Answer: ")
    if (jawapan.lower() == jawapan_4):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        markah = markah + 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN SEBENAR IALAH:",jawapan_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  YANG MANAKAH BUKAN TEKNIK PEMIKIRAN KOMPUTASIONAL?\n(A) LERAIAN\n(B) PENGEKODAN\n(C) PENGECAMAN\n(D) PENISKALAAN\n\n")
jawapan_5= "B"

for i in range(chances):
    jawapan = input("Jawapan: ")
    if (jawapan.lower() == jawapan_5):
        print("TAHNIAH! JAWAPAN ANDA BETUL!\n")
        markah = markah + 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN SEBENAR IALAH:", jawapan_5, "\n\n")

time.sleep(2)

#print the markah
print("==================================================")
while markah >=2:
    print("TAHNIAH! MARKAH ANDA IALAH:", markah)
    break

while markah <2:
    print("CUBA LAGI! MARKAH ANDA IALAH:",markah)
    break

#Goobye message
print("TERIMA KASIH MENYERTAI KUIZ ASK!")