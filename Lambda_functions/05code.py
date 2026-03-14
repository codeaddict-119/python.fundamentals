students = [
    ("Alice", [85, 90, 88]),
    ("Bob", [70, 75, 72]),
    ("Charlie", [95, 92, 96]),
    ("David", [82, 80, 84]),
    ("Eva", [60, 65, 70]),
    ("Frank", [89, 91, 87])
]

result = list(
    map(
        lambda x: (x[0], sum(x[1]) / len(x[1])),
        sorted(
            filter(
                lambda x: sum(x[1]) / len(x[1]) > 80,
                students
            ),
            key=lambda x: sum(x[1]) / len(x[1]),
            reverse=True
        )
    )
)[:3]

print(result)
