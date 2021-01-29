def print_note():
    print("/---------Truth Table Generator---------\\")
    print("|-----------------!NOTE-----------------|")
    print("| COPY PASTE||LOGICAL CONNECTIVES BELOW |")
    print("|                                       |")
    print("|    I. Negation Operator >       ¬     |")
    print("|    II. Conjunction Operator >   ^     |")
    print("|    III. Exclusive OR Operator > ⊻     |")
    print("|    IV. Disjunction Operator >   v     |")
    print("|    V. Implication Operator >    →     |")
    print("|    VI. BiConditional Operator > ↔     |")
    print("|                                       |")
    print("|---------------------------------------|")
    print("|                                       |")
    print("| Print In This Format (p_connective_q) |")
    print("|   p & q = any char | (_) are spaces   |")
    print("|                                       |")
    print("\\--------------END OF NOTE--------------/")
    print("")


def check_negation(p, q):
    if "¬" in p:
        p_truth_val = {0: False, 1: False, 2: True, 3: True}
        p_bool = False
    else:
        p_truth_val = {0: True, 1: True, 2: False, 3: False}
        p_bool = True
    if "¬" in q:
        q_truth_val = {0: False, 1: True, 2: False, 3: True}
        q_bool = False
    else:
        q_truth_val = {0: True, 1: False, 2: True, 3: False}
        q_bool = True

    return p_truth_val, q_truth_val, p_bool, q_bool


def call_conj(p, q, p_true, q_true):
    p_conj_q = {}

    if p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_conj_q.update({x: ["True", "True", "True"]})
            elif p[x] and not q[x]:
                p_conj_q.update({x: ["True", "False", "False"]})
            elif not p[x] and q[x]:
                p_conj_q.update({x: ["False", "True", "False"]})
            elif not p[x] and not q[x]:
                p_conj_q.update({x: ["False", "False", "False"]})
    elif p_true and not q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_conj_q.update({x: ["True", "True", "False", "True"]})
            elif p[x] and not q[x]:
                p_conj_q.update({x: ["True", "False", "True", "False"]})
            elif not p[x] and q[x]:
                p_conj_q.update({x: ["False", "True", "False", "False"]})
            elif not p[x] and not q[x]:
                p_conj_q.update({x: ["False", "False", "True", "False"]})
    elif not p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_conj_q.update({x: ["True", "True", "False", "True"]})
            elif p[x] and not q[x]:
                p_conj_q.update({x: ["True", "False", "False", "False"]})
            elif not p[x] and q[x]:
                p_conj_q.update({x: ["False", "True", "True", "False"]})
            elif not p[x] and not q[x]:
                p_conj_q.update({x: ["False", "False", "True", "False"]})
    elif not p_true and not q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_conj_q.update({x: ["False", "False", "True", "True", "True"]})
            elif p[x] and not q[x]:
                p_conj_q.update({x: ["False", "True", "True", "False", "False"]})
            elif not p[x] and q[x]:
                p_conj_q.update({x: ["True", "False", "False", "True", "False"]})
            elif not p[x] and not q[x]:
                p_conj_q.update({x: ["True", "True", "False", "False", "False"]})

    return p_conj_q


def call_disk(p, q, p_true, q_true):
    p_disk_q = {}

    if p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_disk_q.update({x: ["True", "True", "True"]})
            elif p[x] and not q[x]:
                p_disk_q.update({x: ["True", "False", "True"]})
            elif not p[x] and q[x]:
                p_disk_q.update({x: ["False", "True", "True"]})
            elif not p[x] and not q[x]:
                p_disk_q.update({x: ["False", "False", "False"]})
    if p_true and not q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_disk_q.update({x: ["True", "True", "False", "True"]})
            elif p[x] and not q[x]:
                p_disk_q.update({x: ["True", "False", "True", "True"]})
            elif not p[x] and q[x]:
                p_disk_q.update({x: ["False", "True", "False", "True"]})
            elif not p[x] and not q[x]:
                p_disk_q.update({x: ["False", "False", "True", "False"]})
    if not p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_disk_q.update({x: ["True", "True", "False", "True"]})
            elif p[x] and not q[x]:
                p_disk_q.update({x: ["True", "False", "False", "True"]})
            elif not p[x] and q[x]:
                p_disk_q.update({x: ["False", "True", "True", "True"]})
            elif not p[x] and not q[x]:
                p_disk_q.update({x: ["False", "False", "True", "False"]})
    if not p_true and not q_true:
        for x in range(0, 4):
            if not p[x] and not q[x]:
                p_disk_q.update({x: ["True", "True", "False", "False", "False"]})
            elif p[x] and not q[x]:
                p_disk_q.update({x: ["False", "True", "True", "False", "True"]})
            elif not p[x] and q[x]:
                p_disk_q.update({x: ["True", "False", "False", "True", "True"]})
            elif p[x] and q[x]:
                p_disk_q.update({x: ["False", "False", "True", "True", "True"]})

    return p_disk_q


def call_impl(p, q, p_true, q_true):
    p_impl_q = {}

    if p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_impl_q.update({x: ["True", "True", "True"]})
            elif p[x] and not q[x]:
                p_impl_q.update({x: ["True", "False", "False"]})
            elif not p[x] and q[x]:
                p_impl_q.update({x: ["False", "True", "True"]})
            elif not p[x] and not q[x]:
                p_impl_q.update({x: ["False", "False", "True"]})
    if p_true and not q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_impl_q.update({x: ["True", "True", "False", "True"]})
            elif p[x] and not q[x]:
                p_impl_q.update({x: ["True", "False", "True", "False"]})
            elif not p[x] and q[x]:
                p_impl_q.update({x: ["False", "True", "False", "True"]})
            elif not p[x] and not q[x]:
                p_impl_q.update({x: ["False", "False", "True", "True"]})
    if not p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_impl_q.update({x: ["True", "True", "False", "True"]})
            elif p[x] and not q[x]:
                p_impl_q.update({x: ["True", "False", "False", "False"]})
            elif not p[x] and q[x]:
                p_impl_q.update({x: ["False", "True", "True", "True"]})
            elif not p[x] and not q[x]:
                p_impl_q.update({x: ["False", "False", "True", "True"]})
    if not p_true and not q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_impl_q.update({x: ["False", "False", "True", "True", "True"]})
            elif p[x] and not q[x]:
                p_impl_q.update({x: ["False", "True", "True", "False", "False"]})
            elif not p[x] and q[x]:
                p_impl_q.update({x: ["True", "False", "False", "True", "True"]})
            elif not p[x] and not q[x]:
                p_impl_q.update({x: ["True", "True", "False", "False", "True"]})

    return p_impl_q


def call_bacon(p, q, p_true, q_true):
    p_bacon_q = {}

    if p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_bacon_q.update({x: ["True", "True", "True"]})
            elif p[x] and not q[x]:
                p_bacon_q.update({x: ["True", "False", "False"]})
            elif not p[x] and q[x]:
                p_bacon_q.update({x: ["False", "True", "False"]})
            elif not p[x] and not q[x]:
                p_bacon_q.update({x: ["False", "False", "True"]})
    if p_true and not q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_bacon_q.update({x: ["True", "True", "False", "True"]})
            elif p[x] and not q[x]:
                p_bacon_q.update({x: ["True", "False", "True", "False"]})
            elif not p[x] and q[x]:
                p_bacon_q.update({x: ["False", "True", "False", "False"]})
            elif not p[x] and not q[x]:
                p_bacon_q.update({x: ["False", "False", "True", "True"]})
    if not p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_bacon_q.update({x: ["True", "True", "False", "True"]})
            elif p[x] and not q[x]:
                p_bacon_q.update({x: ["True", "False", "False", "False"]})
            elif not p[x] and q[x]:
                p_bacon_q.update({x: ["False", "True", "True", "False"]})
            elif not p[x] and not q[x]:
                p_bacon_q.update({x: ["False", "False", "True", "True"]})
    if not p_true and not q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_bacon_q.update({x: ["False", "False", "True", "True", "True"]})
            elif p[x] and not q[x]:
                p_bacon_q.update({x: ["False", "True", "True", "False", "False"]})
            elif not p[x] and q[x]:
                p_bacon_q.update({x: ["True", "False", "False", "True", "False"]})
            elif not p[x] and not q[x]:
                p_bacon_q.update({x: ["True", "True", "False", "False", "True"]})

    return p_bacon_q


def call_exc(p, q, p_true, q_true):
    p_exc_q = {}

    if p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_exc_q.update({x: ["True", "True", "False"]})
            elif p[x] and not q[x]:
                p_exc_q.update({x: ["True", "False", "True"]})
            elif not p[x] and q[x]:
                p_exc_q.update({x: ["False", "True", "True"]})
            elif not p[x] and not q[x]:
                p_exc_q.update({x: ["False", "False", "False"]})
    if p_true and not q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_exc_q.update({x: ["True", "True", "False", "False"]})
            elif p[x] and not q[x]:
                p_exc_q.update({x: ["True", "False", "True", "True"]})
            elif not p[x] and q[x]:
                p_exc_q.update({x: ["False", "True", "False", "True"]})
            elif not p[x] and not q[x]:
                p_exc_q.update({x: ["False", "False", "True", "False"]})
    if not p_true and q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_exc_q.update({x: ["True", "True", "False", "False"]})
            elif p[x] and not q[x]:
                p_exc_q.update({x: ["True", "False", "False", "True"]})
            elif not p[x] and q[x]:
                p_exc_q.update({x: ["False", "True", "True", "True"]})
            elif not p[x] and not q[x]:
                p_exc_q.update({x: ["False", "False", "True", "False"]})
    if not p_true and not q_true:
        for x in range(0, 4):
            if p[x] and q[x]:
                p_exc_q.update({x: ["False", "False", "True", "True", "False"]})
            elif p[x] and not q[x]:
                p_exc_q.update({x: ["False", "True", "True", "False", "True"]})
            elif not p[x] and q[x]:
                p_exc_q.update({x: ["True", "False", "False", "True", "True"]})
            elif not p[x] and not q[x]:
                p_exc_q.update({x: ["True", "True", "False", "False", "False"]})

    return p_exc_q


def print_table(dictionary, char_a, char_c, p_boolean, q_boolean, connective):
    print("")
    pros = char_a + " " + connective + " " + char_c
    if p_boolean and q_boolean:
        print("{:<6} |-------TRUTH TABLE-------|".format(" "))
        print("{:<7}|   {:<4}|   {:<4}|  {:<7}|".format(" ", char_a, char_c, pros))
        for key, value in dictionary.items():
            for x in range(0, 1):
                print("{:<6} |-------|-------|---------|".format(" "))
            p, q, proposition = value
            print("{:<6} | {:<5} | {:<5} |  {:<7}|".format(" ", p, q, proposition))
        print("{:<6} |-------------------------|".format(" "))



    elif p_boolean and not q_boolean:
        print("{:<2} |-----------TRUTH TABLE-----------|".format(" "))
        print("{:<3}|   {:<4}|   {:<4}|  {:<5}| {:<6}  |".format(" ", char_a, char_c[1:], char_c, pros))
        for key, value in dictionary.items():
            for x in range(0, 1):
                print("{:<2} |-------|-------|-------|---------|".format(" "))
            p, q, neg_q, proposition = value
            print("{:<2} | {:<5} | {:<5} | {:<5} |  {:<7}|".format(" ", p, neg_q, q, proposition))
        print("{:<2} |---------------------------------|".format(" "))



    elif not p_boolean and q_boolean:
        print("{:<2} |-----------TRUTH TABLE-----------|".format(" "))
        print("{:<3}|   {:<4}|   {:<4}|  {:<5}| {:<6}  |".format(" ", char_a[1:], char_c, char_a, pros))
        for key, value in dictionary.items():
            for x in range(0, 1):
                print("{:<2} |-------|-------|-------|---------|".format(" "))
            p, q, neg_p, proposition = value
            print("{:<2} | {:<5} | {:<5} | {:<5} |  {:<7}|".format(" ", neg_p, q, p, proposition))
        print("{:<2} |---------------------------------|".format(" "))


    elif not p_boolean and not q_boolean:
        print("|-----------TRUTH TABLE-----------------|".format(" "))
        print("|  {:<4} |  {:<4} |  {:<4} |  {:<4} |{:<6}|".format(char_a[1:], char_c[1:], char_a, char_c, pros))
        for key, value in dictionary.items():
            for x in range(0, 1):
                print("|-------|-------|-------|-------|-------|".format(" "))
            neg_p, neg_q, p, q, proposition = value
            print("| {:<5} | {:<5} | {:<5} | {:<5} | {:<6}|".format(neg_p, neg_q, p, q, proposition))
        print("|---------------------------------------|")