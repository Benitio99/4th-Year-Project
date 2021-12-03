with open("static/words") as wf:
    # Aaron Nolan, C3 20/21 student spotted a bug on this next line.  The fix is on line after.
    # words = {line.strip("\n").strip("'s").lower() for line in wf}  # A set.
    words = {line.strip("\n").replace("'s", "").lower() for line in wf}  # A set.
words = sorted(words)[1:]  # Ignore the empty word at the start of the list.


def find_possible_matches(pattern):
    """Given any pattern of the type "__a___b__c", this function
       looks up and returns all the potential matches for the
       pattern in the Linux dictionary of words."""

    def match_pattern(w, p):
        """Returns True if 'w' matches 'p', False otherwise."""
        letters = {k: v for k, v in enumerate(p) if v != "_"}
        return not any([w[i] != p[i] for i in letters.keys()])

    pattern = pattern.lower()  # Just in case...
    matches = {
        word  ## SELECT...
        for word in words  ## FROM...
        if len(word) == len(pattern) and match_pattern(word, pattern)  ## WHERE...
    }
    return matches
