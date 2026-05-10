from memory.short_term_memory import (
    save_short_term_memory,
    get_recent_memory
)

from memory.long_term_memory import (
    save_long_term_memory,
    load_long_term_memory
)


def save_memory(role, message):

    save_short_term_memory(role, message)

    save_long_term_memory(role, message)


def retrieve_memory():

    short_term = get_recent_memory()

    long_term = load_long_term_memory()

    return {
        "short_term": short_term,
        "long_term": long_term
    }