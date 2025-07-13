import threading
import queue
from GUI import run_gui
#from network import listen


def main():
    msg_queue = queue.Queue()

    # Start network thread only
  #  threading.Thread(target=listen_network, args=(msg_queue,), daemon=True).start()

    # GUI must run on main thread
    run_gui(msg_queue)


if __name__ == "__main__":

    main()