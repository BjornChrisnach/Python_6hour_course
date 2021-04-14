# file = open("file.txt, "r")
# try:
# file.write("hello")
# finally:
# file.close()

# with open("file.txt","r") as file:
#     file.write("hello")
class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):
        print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()
        if type == Exception:
            return True


with File("file.txt", "w") as f:
    print("Middle")
    f.write("hello!")
