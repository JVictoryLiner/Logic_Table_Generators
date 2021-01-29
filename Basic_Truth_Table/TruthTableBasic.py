from TTB_Functions import print_note, check_negation, print_table
from TTB_Functions import call_conj, call_disk, call_impl, call_bacon, call_exc


def check_symbol(connective):
    if connective == "^":
        truth_table = call_conj(p_value, q_value, bool_p, bool_q)
        print_table(truth_table, a, c, bool_p, bool_q, connective)
    elif connective == "v":
        truth_table = call_disk(p_value, q_value, bool_p, bool_q)
        print_table(truth_table, a, c, bool_p, bool_q, connective)
    elif connective == "→":
        truth_table = call_impl(p_value, q_value, bool_p, bool_q)
        print_table(truth_table, a, c, bool_p, bool_q, connective)
    elif connective == "↔":
        truth_table = call_bacon(p_value, q_value, bool_p, bool_q)
        print_table(truth_table, a, c, bool_p, bool_q, connective)
    elif connective == "⊻":
        truth_table = call_exc(p_value, q_value, bool_p, bool_q)
        print_table(truth_table, a, c, bool_p, bool_q, connective)
    else:
        print("{:<7}Invalid Logical Connective".format(" "))


print_note()
a, symbol, c = input("{:<7}Input Proposition :".format(" ")).split()

p_value, q_value, bool_p, bool_q = check_negation(a, c)

check_symbol(symbol)



