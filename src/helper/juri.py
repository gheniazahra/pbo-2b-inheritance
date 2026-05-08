class Juri:
    def determine_winner(self, player, computer):
        if player.pilihan == computer.pilihan:
            print("Hasil: Seri!\n")
        elif (player.pilihan == "batu" and computer.pilihan == "gunting") or \
             (player.pilihan == "gunting" and computer.pilihan == "kertas") or \
             (player.pilihan == "kertas" and computer.pilihan == "batu"):
            print("Hasil: Menang!\n")
        else:
            print("Hasil: Kalah!\n")