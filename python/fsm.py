'''
Automatons, or Finite State Machines (FSM), are extremely useful to programmers when it comes to software design. You will be given a simplistic version of an FSM to code for a basic TCP session.

The outcome of this exercise will be to return the correct state of the TCP FSM based on the array of events given.
'''

def traverse_TCP_states(events):
    state_transition_table = {
        "CLOSED" : {
            "APP_PASSIVE_OPEN" : "LISTEN",
            "APP_ACTIVE_OPEN" : "SYN_SENT"
        },
        "LISTEN" : {
            "RCV_SYN" : "SYN_RCVD",
            "APP_SEND" : "SYN_SENT",
            "APP_CLOSE" : "CLOSED"
        },
        "SYN_RCVD" : {
            "APP_CLOSE" : "FIN_WAIT_1",
            "RCV_ACK" : "ESTABLISHED",
        },
        "SYN_SENT" : {
            "RCV_SYN" : "SYN_RCVD",
            "RCV_SYN_ACK" : "ESTABLISHED",
            "APP_CLOSE" : "CLOSED"
        },
        "ESTABLISHED" : {
            "APP_CLOSE" : "FIN_WAIT_1",
            "RCV_FIN" : "CLOSE_WAIT"
        },
        "FIN_WAIT_1" : {
            "RCV_FIN" : "CLOSING",
            "RCV_FIN_ACK" : "TIME_WAIT",
            "RCV_ACK" : "FIN_WAIT_2"
        },
        "CLOSING" : {
            "RCV_ACK" : "TIME_WAIT"
        },
        "FIN_WAIT_2" : {
            "RCV_FIN" : "TIME_WAIT"
        },
        "TIME_WAIT" : {
            "APP_TIMEOUT" : "CLOSED"
        },
        "CLOSE_WAIT" : {
            "APP_CLOSE" : "LAST_ACK"
        },
        "LAST_ACK" : {
            "RCV_ACK" : "CLOSED"
        }
        
    }
    state = "CLOSED"  # initial state, always
    try:
        for event in events:
            state = state_transition_table[state][event]
    except KeyError as e:
        return "ERROR"
