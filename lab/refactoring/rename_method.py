# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def cal_un_gr(graph):   # TODO: Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_value(li):  # TODO: Rename this function to reflect what it's doing.
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(get_value(li))

############################
def split_word_by_whitespace(sentence):
    return sentence[0:].split(' ')

print(process('If you were a vegetable, you’d be a ‘cute-cumber.'))
