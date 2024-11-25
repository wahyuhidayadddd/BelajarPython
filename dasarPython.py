

# Python tidak memiliki perintah untuk mendeklarasikan variabel.
# Suatu variabel tercipta pada saat pertama kali Anda menetapkan suatu nilai padanya.
x = 10
y = "Wahyu Hidayat"
print(x)
print(y)




# Variabel tidak perlu dideklarasikan dengan tipe tertentu , dan bahkan dapat mengubah tipe setelah ditetapkan.

x = 4
u = "Wahyu"
print(u)








# Casting
# Jika Anda ingin menentukan tipe data suatu variabel, ini dapat dilakukan dengan casting.

umurku = str(22)
umurKamu = int(16)
umurMamamu = float(40)
print(umurku,umurKamu,umurMamamu)








# LEGAL VARIABLE NAMES

myvar = "Wahyu Hidayat"
my_Var = "ucok"
_my_Var= "udin sitompul"
myVar = "keysha"
MYVAR = "UDINN"
myvar2 = "upin"


print(myvar)
print(my_Var)
print(_my_Var)
print(myVar)
print(MYVAR)
print(myvar2)



# Slicing

b = "WAHYU HIDAYAT"
print(b[2:5])





a = ["wahyu","udin","ucok"]
print(type(a)) 



# (boolean)
print(20>9)



c = 200
d = 10

if c > d:
    print("c lebih besar dari d ")
else:
    print("c tidak besar dari d")




# LIST ITEMS

makanan = ["sopBuah","buburAyam","coklat","mentega",]
print(makanan[1:3])


# Insert Items

iniList = ["apple","mangga","jeruk"]
iniList.insert(0,"mellon")
print(iniList)




# Append Items

thisList = ["babi","kucing","ayam","harimau","singa"]
thisList.append("toluimau")
print(thisList)


# REMOVE ITEMS
thisList = ["apel","jeruk","mangga","buahnaga"]
thisList.remove("apel")
print(thisList)



# Remove Specified Index

thisList = ["harimau","kucing","singa"]
thisList.pop(1)
print(thisList)




# Loop Through a List