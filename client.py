import Pyro5.api

HOST = "127.0.0.1"
NS_PORT = 9000


def main():
    try:
        # Locate the name server (LocateRegistry.getRegistry("127.0.0.1", 9000))
        ns = Pyro5.api.locate_ns(host=HOST, port=NS_PORT)

        # Lookup the laptop object (registry.lookup("laptop"))
        laptop = Pyro5.api.Proxy(ns.lookup("laptop"))

        laptop_name = laptop.get_name()
        laptop_description = laptop.get_description()
        price = laptop.get_price()

        print("Name:" + laptop_name)
        print("Description: " + laptop_description)
        print("Price: " + str(price))
    except Exception as e:
        print("Exception in client side", e)


if __name__ == "__main__":
    main()
