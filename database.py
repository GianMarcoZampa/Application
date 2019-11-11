class DataBase:
    def __init__(self, file_name):
        self.file_name = file_name
        self.users = {}
        self.load()

    # This method is called by the constructor and loads stored data in users variable
    def load(self):
        with open(self.file_name, "r") as f:
            lines = f.readlines()

            for line in lines:
                email, nickname, password = line.split(";", 3)
                self.users[email] = [nickname, password]

    # This method returns the user data if it already exists else false
    def get(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return False

    # This method adds an user to database if it doesn't exists yet else flase
    def add(self, email, nickname, password):
        if email not in self.users:
            self.users[email] = [nickname, password]
            self.save()
            return True
        else:
            print("Email already exists")
            return False

    # This method deletes an user from the database if it already exists else false
    def delete(self, email):
        if email in self.users:
            self.users.pop(email)
            self.save()
            return True
        else:
            print("Cannot delete account")
            return False

    # This method updates user data if the user already exists else false
    def update(self, email, nickname, password):
        if email in self.users:
            self.users[email] = [nickname, password]
            self.save()
            return True
        else:
            print("Email doesn't exists")
            return False

    # This method saves values stored in users inside a .txt file
    def save(self):
        with open(self.file_name, "w") as f:
            for user in self.users.items():
                line = user[0] + ";" + user[1] + ";" + user[3] + "\n"
                f.write(line)
