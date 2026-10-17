# Python RMI Lab (Pyro5)

## Requirements

- Python 3.8+
- Pyro5

## How to run

Open **three terminals** in the project folder, and run them in this order.

**Terminal 1 - Name server (the "registry")**

command:  ( python -m Pyro5.nameserver -n 127.0.0.1 -p 9000 )


**Terminal 2 - Server**

command: ( python server.py )


**Terminal 3 - Client**

command: ( python client.py )


## Expected output

Server:

Server is booting....
Registered objects:
  laptop   -> PYRO:obj_...@127.0.0.1:...
  ram      -> PYRO:obj_...@127.0.0.1:...
  bag      -> PYRO:obj_...@127.0.0.1:...
  charger  -> PYRO:obj_...@127.0.0.1:...
Server is ready and waiting for client requests...


Client:

Name:Laptop
Description: Lenovo laptop
Price: 800000.0


## Notes

- The Mobile object is bound under the name `ram`, exactly as in the original Java server.
- Stop the server and name server with `Ctrl+C`.
