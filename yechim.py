# # #1-masala
# # for i in range(1, 11):
# #     print(i, end=" ")
# # #2-masala
# # word = "Python"
# # for l in word:
# #     print(" -", l)
# # #3-masala
# # names = ["Ali", "Vali", "Hasan", "Husan"]
# # for index, name in enumerate(names, start=1):
# #     print(f"{index}. {name}")
# # #4-masala
# # for i in range(1, 21):
# #     if i % 2 == 0:
# #         print(i, end=" ")
# # #5-masala
# # summa = 0
# # for x in range(1, 51):
# #     summa = summa + x
# # print(f"1dan 50gacha bolgan sonlar yigindisi = {summa}")
# # #6-masala
# # count = 0
# # for i in range(1, 101):
# #     if i % 3 == 0:
# #         print(i, end=" ")
# #         count += 1
# # print()
# # print(f"Jami: {count} ta son topildi")
# # # 7-masala
# # matn = "Python dasturlash juda qiziqarli va foydali"
# # unli = "aeiouAEIOU"
# # count = 0
# # for belgi in matn:
# #     if belgi in unli:
# #         count += 1
# # print("Matn:", matn)
# # print("Unli harflar soni:", count)
# #8-masala
# # sonlar = [45, 12, 89, 34, 67, 23, 91, 56, 78]
# # eng_katta = sonlar[0]
# # for son in sonlar:
# #     if son > eng_katta:
# #         eng_katta = son
# # print("Eng katta son:", eng_katta)
# #9-masala
# sonlar = [34, 12, 89, 5, 67, 23, 91, 45]
# yigindi = 0
# maksimum = sonlar[0]
# minimum = sonlar[0]
# for son in sonlar:
#     yigindi += son
#     if son > maksimum:
#         maksimum = son
#     if son < minimum:
#         minimum = son
# ortalama = yigindi / len(sonlar)
#
# print("Yig'indi:", yigindi)
# print("Eng katta son:", maksimum)
# print("Eng kichik son:", minimum)
# print("O'rtacha qiymat:", ortalama)
# # 10-masala
# matn = "Python"
# teskari = ""
# for harf in matn:
#     teskari = harf + teskari
# print("Asl matn:", matn)
# print("Teskari matn:", teskari)
#11-masala
# print("1 dan 10 gacha bo'lgan ko'paytirish jadvali:\n")
# for i in range(1, 11):
#     print(f"{i} ning ko'paytirish jadvali:")
#     for j in range(1, 11):
#         print(f" {i} × {j} = {i * j:2}")
#     print()
#12-masala
# n = int(input("Piramida balandligini kiriting: "))
# for qator in range(1, n + 1):
#     for boosh in range(n - qator):
#         print(" ", end="")
#     for yul in range(2 * qator - 1):
#         print("*", end="")
#     print()
# #13-masala
# a = 0
# b = 1
# print(a, end=' ')
# for _ in range(9):
#     print(b, end=' ')
#     a, b = b, a + b
# #14-masala
# gap = "Python dasturlash tili juda qiziqarli va kuchli"
# soz = ""      # joriy so'z
# soz_soni = 0  # so'zlar soni
# for belgi in gap:
#     if belgi != " ":
#         soz += belgi
#     else:
#         if soz != "":
#             soz_soni += 1
#             print(f"{soz_soni}. {soz}")
#             soz = ""
# if soz != "":
#     soz_soni += 1
#     print(f"{soz_soni}. {soz}")
# print(f"Jami so'zlar soni: {soz_soni}")
#15-masala
n = 5
t = ''
for qator in range(1, n + 1):
    for boosh in range(n - qator):
        print(" ", end="")
    for yul in range(2 * qator - 1):
        print("*", end="")
    for qato in range(1, n-1):
        print("", end="")
    for ch in range (2 * qator +1):
        print("*", end="")
print()