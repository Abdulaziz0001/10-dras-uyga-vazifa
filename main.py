# # 1-misol
# from multiprocessing import Process, Queue
# import time
#
#
# def generate_numbers(res: Queue):
#     i = 0
#     yigindi = 0
#     while i < 10:
#         print(i + 1)
#         i += 1
#         yigindi += i
#         time.sleep(0.5)
#     res.put(yigindi)
#
# if __name__ == "__main__":
#     l = Queue()
#     pr = Process(target=generate_numbers, args=(l,))
#
#     pr.start()
#
#     pr.join()
#
#     print(f"Yigindi: {l.get()}")

# # 2-misol
# from multiprocessing import Process, Queue
#
# def aylantirish(res: Queue):
#     royxat = [1, 2, 3, 4]
#     if royxat:
#         royxat.append(royxat.pop(0))
#     res.put(royxat)
# if __name__ == "__main__":
#     l1 = Queue()
#     pr = Process(target=aylantirish, args=(l1,))
#     pr.start()
#     pr.join()
#     print(f"Aylantirilgan ro'yxat: {l1.get()}")

# # 3-misol
# from multiprocessing import Process, Queue
#
# def katta_sonlar(sonlar, res: Queue):
#     res.put(max(sonlar))
#
# def kichik_sonlar(sonlar, res: Queue):
#     res.put(min(sonlar))
#
# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     l1 = Queue()
#     l2 = Queue()
#
#     pr1 = Process(target=katta_sonlar, args=(numbers, l1,))
#     pr2 = Process(target=kichik_sonlar, args=(numbers, l2,))
#
#     pr1.start()
#     pr2.start()
#
#     pr1.join()
#     pr2.join()
#
#     katta = l1.get()
#     kichik = l2.get()
#
#     print(f"Katta sonlar: {katta}")
#     print(f"Kichik sonlar: {kichik}")

# # 4-misol
# from multiprocessing import Process, Queue
#
#
# def element_qidirish(numbers, element, res: Queue):
#     if element in numbers:
#         res.put(True)
#     else:
#         res.put(False)
#
# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     element = 10
#
#     l = Queue()
#     pr = Process(target=element_qidirish, args=(numbers, element, l,))
#     pr.start()
#     pr.join()
#     natija = l.get()
#     if natija:
#         print(f"{element} ro'yxatda mavjut!!!")
#     else:
#         print(f"{element} ro'yxatda mavjut emas!!!")

# # 5-misol
# from multiprocessing import Process, Queue
#
# def numbers(royxat, yangilangan_royxat, res: Queue):
#     for i in royxat:
#         if i not in yangilangan_royxat:
#             yangilangan_royxat.append(i)
#             yangilangan_royxat.sort()
#         res.put(yangilangan_royxat)
#
# if __name__ == "__main__":
#     royxat = [1, 2, 3, 4, 5, 5, 2, 4, 7, 6, 9 ,7, 8, 10]
#     yangilangan_royxat = []
#
#     l = Queue()
#     pr = Process(target=numbers, args=(royxat, yangilangan_royxat, l,))
#     pr.start()
#     pr.join()
#     print(l.get())

# # 6-misol
# from multiprocessing import Process, Queue
#
#
# def teskari_sozlar(royxat, res: Queue):
#     teskari_sozlar = [soz[::-1] for soz in royxat]
#     res.put(teskari_sozlar)
#
# if __name__ == "__main__":
#     royxat = ["Abdulaziz", "Muhammadali"]
#
#     l = Queue()
#     pr = Process(target=teskari_sozlar, args=(royxat, l,))
#     pr.start()
#     pr.join()
#     natija = l.get()
#     print(f"Teskari so'zlar: {natija}")

# # 7-misol
# from multiprocessing import Process, Queue
#
# def eng_katta_soz(royxat, res: Queue):
#     eng_uzun_soz = max(royxat)
#     res.put(f"Eng uzun soz: {eng_uzun_soz}")
#
# if __name__ == "__main__":
#     royxat = ["Abdulaziz", "Muhammadali", "Abdurahmon"]
#
#     l = Queue()
#     pr = Process(target=eng_katta_soz, args=(royxat, l,))
#     pr.start()
#     pr.join()
#     print(l.get())

# # 8-misol
# from multiprocessing import Process, Queue
#
# def qidirish(royxat, element, res: Queue):
#     a = royxat.count(element)
#     res.put(f"Kiritilgan element royxatda {a} martda takrorlangan.")
#
# if __name__ == "__main__":
#     royxat = [1, 2, 1, 2, 3, 1, 2, 1]
#     element = 1
#
#     l = Queue()
#     pr = Process(target=qidirish, args=(royxat, element, l,))
#     pr.start()
#     pr.join()
#     print(l.get())

# # 9-misol
# from multiprocessing import Process, Queue
#
# def raqamlar(royxat, yangi_royxat, res: Queue):
#     for i in royxat:
#         if isinstance(i, int):
#             yangi_royxat.append(i)
#     res.put(yangi_royxat)
#
# if __name__ == "__main__":
#     royxat = ["a", 1, 2, 3, 1, 2, "w", "s", 4, "f"]
#     yangi_royxat = []
#     l = Queue()
#     pr = Process(target=raqamlar, args=(royxat, yangi_royxat, l,))
#     pr.start()
#     pr.join()
#     print(l.get())

# # 10-misol
# from multiprocessing import Process, Queue
#
# def raqamlar(royxat, yangi_royxat, res: Queue):
#     for i in royxat:
#         if isinstance(i, int):
#             i *= 2
#             yangi_royxat.append(i)
#     res.put(yangi_royxat)
#
# if __name__ == "__main__":
#     royxat = ["a", 1, 2, 3, 1, 2, "w", "s", 4, "f"]
#     yangi_royxat = []
#     l = Queue()
#     pr = Process(target=raqamlar, args=(royxat, yangi_royxat, l,))
#     pr.start()
#     pr.join()
#     print(l.get())

# # 11-misol
# from multiprocessing import Process, Queue
#
# def eng_katta_qiymat_kalit(lugat, res: Queue):
#     if lugat:
#         eng_katta_kalit = max(lugat, key=lugat.get)
#         res.put(eng_katta_kalit)
#     else:
#         res.put("Lug‘at bo‘sh.")
#
# if __name__ == "__main__":
#     lugat = {"a": 10, "b": 25, "c": 15, "d": 30}
#     res = Queue()
#
#     pr = Process(target=eng_katta_qiymat_kalit, args=(lugat, res))
#     pr.start()
#     pr.join()
#
#     print(f"Eng katta qiymatga ega kalit: {res.get()}")

# # 12-misol
# from multiprocessing import Process, Queue
#
# def ortacha_qiymat(lugat, res: Queue):
#     if lugat:
#         qiymatlar = lugat.values()
#         ortacha = sum(qiymatlar) / len(qiymatlar)
#         res.put(ortacha)
#
# if __name__ == "__main__":
#     lugat = {"a": 10, "b": 20, "c": 30, "d": 40}
#     res = Queue()
#
#     pr = Process(target=ortacha_qiymat, args=(lugat, res))
#     pr.start()
#     pr.join()
#
#     print(f"Qiymatlarning o‘rtacha qiymati: {res.get()}")

# # 13-misol
# from multiprocessing import Process, Queue
#
# def royxatlar(royxat1, royxat2, res: Queue):
#     ikki_royxat = royxat1 + royxat2
#     qoshish = sum(ikki_royxat)
#     res.put(qoshish)
#
# if __name__ == "__main__":
#     royxat1 = [1, 2, 3, 4, 5]
#     royxat2 = [6, 7, 8, 9, 10]
#     l = Queue()
#     pr = Process(target=royxatlar, args=(royxat1, royxat2, l,))
#     pr.start()
#     pr.join()
#     natija = l.get()
#     print(f"Natija: {natija}")

# # 14-misol
# from multiprocessing import Process, Queue
# def sozlar(lugat, res: Queue):
#     if lugat:
#         eng_uzun_soz = max(lugat)
#         eng_kichik_soz = min(lugat)
#     res.put(f"Eng uzun soz: {eng_uzun_soz}\nEng kichick soz: {eng_kichik_soz}")
#
# if __name__ == "__main__":
#     lugat = {"a": "Abdulaziz", "b": "Muhammadali", "c": "Abdurahmfgon"}
#     l = Queue()
#     pr = Process(target=sozlar, args=(lugat, l,))
#     pr.start()
#     pr.join()
#     print(l.get())

# # 15-misol
# from multiprocessing import Process, Queue
#
# def convert_numbers(dictionary, queue):
#     converted_dict = {}
#     for key, value in dictionary.items():
#         if isinstance(value, str) and value.isdigit():
#             converted_dict[key] = int(value)
#         else:
#             converted_dict[key] = value
#     queue.put(converted_dict)
#
# if __name__ == "__main__":
#     input_dict = {
#         "age": "25",
#         "name": "Aziz",
#         "height": "180",
#         "weight": "75kg"
#     }
#
#     queue = Queue()
#
#     process = Process(target=convert_numbers, args=(input_dict, queue))
#     process.start()
#     process.join()
#
#     result = queue.get()
#     print("Yangi lug‘at:", result)

# # 16-misol
# from multiprocessing import Process, Queue
#
# def multiply_values(dictionary, queue):
#     new_dict = {}
#     for key, value in dictionary.items():
#         if isinstance(value, (int, float)):
#             new_dict[key] = value * 2
#         else:
#             new_dict[key] = value
#     queue.put(new_dict)
#
# if __name__ == "__main__":
#     input_dict = {
#         "a": 10,
#         "b": 15.5,
#         "c": "hello",
#         "d": 7
#     }
#
#     queue = Queue()
#
#     process = Process(target=multiply_values, args=(input_dict, queue))
#     process.start()
#     process.join()
#
#     result = queue.get()
#     print("Yangi lug‘at:", result)

# # 17-misol
# from multiprocessing import Process, Queue
#
# def teskari_aylantirish(lugat, res: Queue):
#     for key, value in  lugat.items():
#         if isinstance(value, str):
#             aylantirish = value[::-1]
#     res.put(aylantirish)
#
#
# if __name__ == "__main__":
#     lugat = {"e1": "Abdulaziz", "e2": "Muhammadali"}
#     l = Queue()
#     pr = Process(target=teskari_aylantirish, args=(lugat, l,))
#     pr.start()
#     pr.join()
#     print(l.get())