

 # **************01.movie profit (simple calculations) *************************

movie = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_percent = int(input())

revenue = tickets * ticket_price * days
total_earned = revenue * (1-cinema_percent/100)

print(f"The profit from the movie {movie} is {total_earned:.2f} lv.")
