import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 42069))

s.listen(5)

print("Listening...")

args = ""

num = 0

while True:
    conn, addr = s.accept()
    print(str(addr) + " Has Connected!")
    every = conn.recv(1024).decode("utf8").split("\n")

    for i in every:
        num = num + 1
        if num > 11:
            args = args + i
    exec(args)
