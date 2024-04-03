
# Online Python - IDE, Editor, Compiler, Interpreter
import random

class وجبة:
    def __init__(self, الاسم):
        self.الاسم = الاسم
        self.العناصر = []

    def اضافة_عنصر(self, المكون, الكمية):
        self.العناصر.append((المكون, الكمية))

class مكون:
    def __init__(self, الاسم, السعرات_الحرارية_للغرام, التصنيف):
        self.الاسم = الاسم
        self.السعرات_الحرارية_للغرام = السعرات_الحرارية_للغرام
        self.التصنيف = التصنيف

def حساب_السعرات(وجبة):
    اجمالي_السعرات = 0
    for المكون, الكمية in وجبة.العناصر:
        اجمالي_السعرات += المكون.السعرات_الحرارية_للغرام * الكمية
    return اجمالي_السعرات

def انشاء_وجبة_عشوائية(الاسم, العناصر_المتاحة, عدد_الأصناف):
    وجبة_عشوائية = وجبة(الاسم)
    for _ in range(عدد_الأصناف):
        مكون_عشوائي = random.choice(العناصر_المتاحة)
        العناصر_المتاحة.remove(مكون_عشوائي)
        الكمية = random.randint(50, 200)  # توليف كمية عشوائية بين 50 و 200 غرام
        وجبة_عشوائية.اضافة_عنصر(مكون_عشوائي, الكمية)
    return وجبة_عشوائية

def main():
    الايام = ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة"]
    العناصر_المتاحة = [
        مكون("أرز", 1.3, "كربوهيدرات"),
        مكون("دجاج", 3.5, "بروتين"),
        مكون("بروكلي", 0.4, "خضروات"),
        مكون("لحم بقري", 2.5, "بروتين"),
        مكون("بطاطا", 0.9, "كربوهيدرات"),
        مكون("سلمون", 2.8, "دهون"),
        مكون("زيتون", 1.2, "دهون"),
        مكون("بيض", 1.6, "بروتين"),
        مكون("تونة", 3.0, "بروتين"),
        مكون("جبنة شيدر", 4.0, "دهون"),
        مكون("خس", 0.1, "خضروات"),
        مكون("طماطم", 0.2, "خضروات"),
        # يمكنك إضافة المزيد من المكونات هنا
    ]

    عدد_الأصناف_لوجبة = {"وجبة الإفطار": 3, "وجبة الغداء": 4, "وجبة العشاء": 3}

    for يوم in الايام:
        print("\n" + يوم + ":")
        الوجبات_اليومية = []
        العناصر_المتاحة_مؤقتة = list(العناصر_المتاحة)  # إنشاء نسخة مؤقتة للعناصر المتاحة لكل يوم
        for وجبة, عدد_الأصناف in عدد_الأصناف_لوجبة.items():
            وجبة_عشوائية = انشاء_وجبة_عشوائية(وجبة, العناصر_المتاحة_مؤقتة, عدد_الأصناف)
            الوجبات_اليومية.append(وجبة_عشوائية)

        for وجبة in الوجبات_اليومية:
            print("\nوجبة: " + وجبة.الاسم)
            print("العناصر:")
            for المكون, الكمية in وجبة.العناصر:
                print("- " + المكون.الاسم + ": " + str(الكمية) + " غرام" + " (" + المكون.التصنيف + ")")
            print("إجمالي السعرات:", حساب_السعرات(وجبة))

if __name__ == "__main__":
    main()