"""
Steps (mirrors the Java server):
  1. Create Product objects
  2. Export them (register with a Pyro5 Daemon)   -> UnicastRemoteObject.exportObject
  3. Bind them in the naming service              -> registry.bind(...)
  4. Wait for client requests                     -> JVM keeps running in Java
"""
import Pyro5.api
from product import Product

HOST = "127.0.0.1"
NS_PORT = 9000  # same port as the Java RMI registry (LocateRegistry.getRegistry(..., 9000))


def main():
    print("Server is booting....")

    # Create the product objects
    p1 = Product("Laptop", "Lenovo laptop", 800000.0)
    p2 = Product("Mobile", "MI 9 mobile", 24000.0)
    p3 = Product("Bag", "Branded bag", 800.0)
    p4 = Product("Charger", "MI Charger", 230.0)

    #  Create the daemon (the remote-object server) on 127.0.0.1
    #  equivalent to java.rmi.server.hostname=127.0.0.1
    daemon = Pyro5.api.Daemon(host=HOST)

    # Register each object with the daemon -> returns its URI (like a stub reference)
    uri1 = daemon.register(p1)
    uri2 = daemon.register(p2)
    uri3 = daemon.register(p3)
    uri4 = daemon.register(p4)

    # 3. Locate the name server (the "registry") and bind names to the URIs
    ns = Pyro5.api.locate_ns(host=HOST, port=NS_PORT)
    ns.register("laptop", uri1)
    ns.register("ram", uri2)      # kept from the Java code: the Mobile object is bound as "ram"
    ns.register("bag", uri3)
    ns.register("charger", uri4)

    print("Registered objects:")
    for name, uri in (("laptop", uri1), ("ram", uri2), ("bag", uri3), ("charger", uri4)):
        print(f"  {name:8} -> {uri}")
    print("Server is ready and waiting for client requests...")

    # 4. Enter the request loop (blocks until Ctrl+C)
    try:
        daemon.requestLoop()
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        daemon.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Server error", e)
