class WyjscieZKumplamiNaPiwo:
    def __enter__(self):
        print("Żona krzyczy, żebyś znowu się nie uchlał!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Kac morderca i kazanie od żony gwarantowane!")


with WyjscieZKumplamiNaPiwo():
    print("Pijemy piwo!")
    print("Pijemy inne trunki!")
    print("Śpiewamy Polacy nic się nie stało.")