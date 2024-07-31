def zrob_przelew(id_pierwszego_klienta, kwota, id_drugiego_klienta):
    print("Pobieram dane od pierwszego klienta")
    print("Zrob przelew")
    print("Pobierz dane drugiego klienta")
    print("Dodanie operacji do listy.")

def pobieranie_danych_klienta(nazwa_klienta):
    print(f"Pobieram dane od klienta {nazwa_klienta}")
    print("Zwracam id klienta")

def przelewanie_kwoty(id_pierwszego_klienta, id_drugiego_klienta, kwota):
    print(f"Robie przelew od {id_pierwszego_klienta} do {id_drugiego_klienta} o kwocie {kwota}")


def dodaj_operacje_do_listy(numer_operacji):
    print(f"Dodałem operacje {numer_operacji} do listy")


def zrob_przelew_agregat(pierwszy_klient, drugi_klient, kwota):
    pobieranie_danych_klienta(pierwszy_klient)
    pobieranie_danych_klienta(drugi_klient)
    przelewanie_kwoty(pierwszy_klient, drugi_klient, kwota)
    dodaj_operacje_do_listy(1)


zrob_przelew_agregat("Michal", "Adam", 6000)


class EmpikUser:
    def __init__(self, username, email, password, orders):
        self.username = username
        self.email = email
        self.password = password
        self.orders = orders

    def change_password(self, new_password):
        self.password = new_password


class UserManager:

    def __init__(self, users):
        self.users = users

    def add_new_user(self, new_user):
        self.users.append(new_user)

    def remove_user(self, user):
        self.users.remove(user)


class EmailSender:
    def send_email_to_users(self):
        print("Wysyłam maila")

class SMSSender:
    def send_sms_to_users(self):
        print("Wysyłam sms do użytkowników")


class SubscriptionManager:
    def renew_subscription_for_users(self):
        print("Odnawiam subskrypcje użytkowników")


class UserManagerWithSMSOptionAvailable(UserManager, SMSSender):
    pass


class UserManagerWithSubscription(UserManager, SubscriptionManager):
    pass



manager = UserManager([EmpikUser("michal", "michalzietkowski@gmail.com", "123", []), EmpikUser("michal", "aaaa@gmail.con", "222", [])])


sms_users_manager = UserManagerWithSMSOptionAvailable([EmpikUser("michal", "michalzietkowski@gmail.com", "123", []), EmpikUser("michal", "aaaa@gmail.con", "222", [])])
sms_users_manager.send_sms_to_users()
manager.send_email_to_users()
premium_manager = UserManagerWithSubscription([])