# დაგუგლე ქსელური პროგრამირების მაგალითი (socket_ის გამოყენებით) და გაარჩიე. დაუწერე კომენტარები.

# შემოტანილია socket და threading მოდულები
import socket
import threading

# პირველი ფუნქციაა start_server
def start_server():
    # ფუნქცია ქმნის ახალ socket-ს
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # აკავშირებს socket-ს მისამართზე 'localhost'(port=12345)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    # უსმენს შემომავალ კავშირებს(მაქსიმალური ზომა 1-ა) და ბეჭდავს შესაბამის მესიჯს
    server_socket.listen(1)
    print('Server is waiting for connections...')
    # იღებს შემომავალ კავშირს, ქმნის ახალ socket-ს და იღებს კლიენტის მისამართს
    client_socket, client_address = server_socket.accept()
    print('Connection established with', client_address)
    # კომუნიკაცია კლიენტთან:
    try:
        # აგზავნის შეტყობინებას და იღებს ინფორმაციას კლიენტისგან
        message = 'Welcome to the server!'
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print('Received:', data.decode())
    finally:
        # ხურავს კლიენტისა და სერვერის socket-ებს
        print('Closing the connection...')
        client_socket.close()
        server_socket.close()

# მეორე ფუნქციაა start_client
        
def start_client():
    # ეს ფუნქცია კლიენტისთვის ქმნის ახალ socket-ს
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # სერვერს აკავშირებს გარკვეულ მისამართზე
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    try:
        # იღებს შეტყობინებას სერვერისგან და თვითონაც უგზავნის მესიჯს
        data = client_socket.recv(1024)
        print('Received from server:', data.decode())
        message = 'Hello, server!'
        client_socket.sendall(message.encode())
    finally:
        # წყვეტს კავშირს
        print('Closing the connection...')
        client_socket.close()

if __name__ == "__main__":
    # main ბლოკი ქმნის ორ thread-ს, ერთს სერვერისთვის, მეორეს კლიენტისთვის
    # ორივე ერთდროულად იწყება. join მეთოდი გამოიყენება იმისთვის, რომ სკრიპტმა იმუშაოს ორივე thread-ის დასრულებამდე
    server_thread = threading.Thread(target=start_server)
    client_thread = threading.Thread(target=start_client)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()