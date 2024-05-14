from typing import Tuple


def correct_sentence(sentence1: str, sentence2: str) -> Tuple[str, str]:
    corrected_sentence1 = sentence1[0].upper() + sentence1[1:-1] + '.' if sentence1[-1] in ['.', '!', '?'] else \
    sentence1[0].upper() + sentence1[1:] + '.'
    corrected_sentence2 = sentence2[0].upper() + sentence2[1:-1] + '.' if sentence2[-1] in ['.', '!', '?'] else \
    sentence2[0].upper() + sentence2[1:] + '.'
    return corrected_sentence1, corrected_sentence2


if __name__ == "__main__":
    assert correct_sentence("greetings, friends", "Hallo") == ("Greetings, friends.", "Hallo.")
    assert correct_sentence("Greetings. Friends", "Greetings, friends.") == (
    "Greetings. Friends.", "Greetings, friends.")

    sentence1: str = "hello world!"
    sentence2: str = "i love python"

    corrected_sentence1, corrected_sentence2 = correct_sentence(sentence1, sentence2)

    print(corrected_sentence1)
    print(corrected_sentence2)
