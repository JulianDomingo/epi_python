from test_framework import generic_test


def h_index(citations):
    citations.sort()
    h_ind = 0
    c_len = len(citations)

    for i, citation in enumerate(citations):
        if citation >= (c_len - i): 
            return (c_len - i) 

    return 0 


if __name__ == '__main__':
    exit(generic_test.generic_test_main("h_index.py", 'h_index.tsv', h_index))
