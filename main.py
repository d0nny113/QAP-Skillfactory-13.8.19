ticket_count = int(input("Введите количество билетов: "))
ticket_cost = 0
counter = 0
while ticket_count > counter:
    age = int(input("Введите возраст посетителя " + str(counter+1) + ": "))
    if age < 18:
        ticket_cost += 0
    if 18 <= age <= 25:
        ticket_cost += 990
    if age > 25:
        ticket_cost += 1390
    counter += 1
if ticket_count <= 3:
    total_cost = ticket_cost
else:
    total_cost = ticket_cost - (ticket_cost / 100 * 10)
print(total_cost)
