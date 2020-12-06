with open('input.txt')as file:
    seats = [(row, col) for row in range(128) for col in range(8)]
    seat_ids = []
    for line in file.readlines():
        row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
        col = int(line[7:10].replace("L", "0").replace("R", "1"), 2)
        seat_ids.append(row*8+col)
        seats.remove((row, col))
    print(max(seat_ids))
