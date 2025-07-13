import threading
import queue
from GUI import run_gui
from network import listen


def main():
    msg_queue = queue.Queue()

    t1 = threading.Thread(target=run_gui, args=(msg_queue,))
    t2 = threading.Thread(target=listen_network, args=(msg_queue,), daemon=True)

    t1.start()
    t2.start()

    t1.join()  # Wait for GUI to close


if __name__ == "__main__":

    main()