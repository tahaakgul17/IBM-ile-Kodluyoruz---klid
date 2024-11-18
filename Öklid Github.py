import math

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Kullanıcıdan güvenli bir şekilde bir nokta al
def getPoint(prompt):
    while True:
        try:
            print(prompt + " (Örneğin: 1.5 2.3)")
            x, y = map(float, input().strip().split())  # Kullanıcının girdisini al
            return (x, y)
        except ValueError:
            print("Hatalı giriş! Lütfen x ve y değerlerini arasında bir boşluk olacak şekilde girin.")

# Kullanıcıdan iki nokta al
point1 = getPoint("İlk nokta koordinatlarını girin (x1 y1)")
point2 = getPoint("İkinci nokta koordinatlarını girin (x2 y2)")

# Öklid mesafesini hesapla
distance = euclideanDistance(point1, point2)

# Sonucu yazdır
print(f"Noktalar: {point1}, {point2}")
print(f"Öklid Mesafesi: {distance}")
