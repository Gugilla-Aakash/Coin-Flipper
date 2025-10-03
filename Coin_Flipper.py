import random
heads_count = 0
tails_count = 0

def coin_flipper():
    return random.choice(["Heads","Tails"])
def result_save(result):
    with open("result.txt", "a") as file:
        file.write(result + "\n")

def main(flips = 1):
    global heads_count , tails_count
    for _ in range(flips):
        result = coin_flipper()
        print(f"Your result is: {result}")
        result_save(result)
        if result == 'Heads':
            heads_count += 1
        else:
            tails_count += 1
if __name__ == "__main__":
    while True:
        try:
            flips = int(input("How many times do you want to flip the coin?(default 1):") or 1)
        except ValueError:
            print("Please enter valid number.")
            continue
        main(flips)
        while True:
            again = input("Do you wanna continue again?(yes/no): ").strip().lower()
            if again in ('yes','y'):
                break
            elif again in ('no','n'):
                print('\n ===Exiting Coin Flipper! , GoodBye===')
                print('\n ===Results are===')
                print(f"Heads = {heads_count}")
                print(f"Tails = {tails_count}")
                print(f"Total Count = {heads_count + tails_count} ")
                exit()
            else:
                print("Please Enter only yes/no (or y/n)")