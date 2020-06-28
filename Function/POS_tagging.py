import nltk
import pprint
from termcolor import colored


def pos_tagging(result_remove):
    result_ps = []
    for r in result_remove:
        result_ps.append(r)
    result_pos_tagging = nltk.pos_tag(result_ps)
    print(colored("[POS TAGGING]","green"))
    pprint.pprint(result_pos_tagging)

    pos_tagging_clean = [x for (x,y) in result_pos_tagging if
                         y not in ('CC','DT','EX','IN','MD','PDT','WRB','WP$','WP','WDT','POS')]
    print(colored("[CLEAN POS TAGGING]","green"))
    print(pos_tagging_clean)
    return result_pos_tagging
