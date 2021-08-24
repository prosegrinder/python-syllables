"""Syllable Estimator

Syllables is a fast, simple syllable estimator intended for use
in places where speed matters. The module has a single function, estimate(),
which accepts an English-language word and returns the estimated number of
syllables in the word.
"""
import re

import pkg_resources

__version__ = (
    pkg_resources.resource_string("syllables", "VERSION").decode("utf-8").strip()
)

# Estimation stuff here

sub_syllables = [
    "cial",
    "tia",
    "cius",
    "cious",
    "uiet",
    "gious",
    "geous",
    "priest",
    "giu",
    "dge",
    "ion",
    "iou",
    "sia$",
    ".che$",
    ".ched$",
    ".abe$",
    ".ace$",
    ".ade$",
    ".age$",
    ".aged$",
    ".ake$",
    ".ale$",
    ".aled$",
    ".ales$",
    ".ane$",
    ".ame$",
    ".ape$",
    ".are$",
    ".ase$",
    ".ashed$",
    ".asque$",
    ".ate$",
    ".ave$",
    ".azed$",
    ".awe$",
    ".aze$",
    ".aped$",
    ".athe$",
    ".athes$",
    ".ece$",
    ".ese$",
    ".esque$",
    ".esques$",
    ".eze$",
    ".gue$",
    ".ibe$",
    ".ice$",
    ".ide$",
    ".ife$",
    ".ike$",
    ".ile$",
    ".ime$",
    ".ine$",
    ".ipe$",
    ".iped$",
    ".ire$",
    ".ise$",
    ".ished$",
    ".ite$",
    ".ive$",
    ".ize$",
    ".obe$",
    ".ode$",
    ".oke$",
    ".ole$",
    ".ome$",
    ".one$",
    ".ope$",
    ".oque$",
    ".ore$",
    ".ose$",
    ".osque$",
    ".osques$",
    ".ote$",
    ".ove$",
    ".pped$",
    ".sse$",
    ".ssed$",
    ".ste$",
    ".ube$",
    ".uce$",
    ".ude$",
    ".uge$",
    ".uke$",
    ".ule$",
    ".ules$",
    ".uled$",
    ".ume$",
    ".une$",
    ".upe$",
    ".ure$",
    ".use$",
    ".ushed$",
    ".ute$",
    ".ved$",
    ".we$",
    ".wes$",
    ".wed$",
    ".yse$",
    ".yze$",
    ".rse$",
    ".red$",
    ".rce$",
    ".rde$",
    ".ily$",
    ".ely$",
    ".des$",
    ".gged$",
    ".kes$",
    ".ced$",
    ".ked$",
    ".med$",
    ".mes$",
    ".ned$",
    ".[sz]ed$",
    ".nce$",
    ".rles$",
    ".nes$",
    ".pes$",
    ".tes$",
    ".res$",
    ".ves$",
    "ere$",
]

add_syllables = [
    "ia",
    "riet",
    "dien",
    "ien",
    "iet",
    "iu",
    "iest",
    "io",
    "ii",
    "ily",
    ".oala$",
    ".iara$",
    ".ying$",
    ".earest",
    ".arer",
    ".aress",
    ".eate$",
    ".eation$",
    "[aeiouym]bl$",
    "[aeiou]{3}",
    "^mc",
    "ism",
    "^mc",
    "asm",
    "([^aeiouy])1l$",
    "[^l]lien",
    "^coa[dglx].",
    "[^gq]ua[^auieo]",
    "dnt$",
]

re_sub_syllables = []
for syllable in sub_syllables:
    re_sub_syllables.append(re.compile(syllable))

re_add_syllables = []
for syllable in add_syllables:
    re_add_syllables.append(re.compile(syllable))


def estimate(word):
    """Estimates the number of syllables in an English-langauge word

    Parameters:
    ----------
    word : str
        The English-langauge word to estimate syllables for

    Returns:
    -------
    int
        the estimated number of syllables in the word

    """
    parts = re.split(r"[^aeiouy]+", word)
    valid_parts = []

    for part in parts:
        if part != "":
            valid_parts.append(part)

    syllables = 0

    for pattern in re_sub_syllables:
        if pattern.match(word):
            syllables -= 1

    for pattern in re_add_syllables:
        if pattern.match(word):
            syllables += 1

    syllables += len(valid_parts)

    if syllables <= 0:
        syllables = 1

    return syllables
