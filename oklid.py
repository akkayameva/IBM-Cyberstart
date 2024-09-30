import math

# Öklid mesafe
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların listesi
points = [(2, 3), (5, 7), (1, 9), (8, 4), (0, 0)]

# Mesafe
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı çiftleri tekrar hesaplamamak için
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
min_distance = min(distances)

print("Minimum mesafe:", min_distance)
