# 1. დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს(Thread) 30-დან 50-მდე ლუწი და კენტი რიცხვების მოსაძებნად და დასაბეჭდად.

import threading

def print_even_numbers():
    for i in range(30, 51, 2):
        print(f"Even: {i}")

def print_odd_numbers():
    for i in range(31, 51, 2):
        print(f"Odd: {i}")

if __name__ == "__main__":
    even_thread = threading.Thread(target=print_even_numbers)
    odd_thread = threading.Thread(target=print_odd_numbers)

    even_thread.start()
    even_thread.join()  

    odd_thread.start()
    odd_thread.join()  

    print("Both threads have finished.")

# 2. დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს(Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.

import os
import threading
import requests

def download_mp3(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {destination}")
    else:
        print(f"Failed to download {url}")

def main():
    url = input("Enter the URL for the MP3 file: ")
    destination = input("Enter name for the MP3 file: ")

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    filename = os.path.join("downloads", f"{destination}.mp3")

    thread = threading.Thread(target=download_mp3, args=(url, filename))
    thread.start()

    thread.join()

    print("Download is complete.")

if __name__ == "__main__":
    main()
