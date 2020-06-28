from termcolor import colored


def lower_case(result_pm):
    result_lwc = []
    for r in result_pm:
        lower_case_text = r.lower()
        result_lwc.append(lower_case_text)
    print(colored("[LOWER CASE]", "green"))
    for r in result_lwc:
        print(r)
    return result_lwc
