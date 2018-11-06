# -*- coding: utf-8 -*-
import regex


def abbreviation_filter(string):
    pattern = regex.compile(r'(?i)\b(?:prof[.]ssa|dott[.]ssa|stim[.]mo|preg[.]mo|gent[.]mo|gent[.]mi|gent[.]me|gent[.]ma|chia[.]mo|dr[.]ssa|sig[.]ra|sig[.]na|ill[.]mo|ass[.]to|egr[.]ia|d[.]ssa|f[.]lli|egr[.]i|v[.]le|p[.]za|c[.]so)\b')
    return regex.sub(pattern,
                    (lambda m: m.group()[:1].upper() + m.group()[1:].lower()),
                    string)


def capitalize_filter(string):
    pattern = regex.compile(r'(?<=\b|_)[a-z]')
    return regex.sub(pattern, (lambda m: m.group().upper()), string.lower())


def company_type_acronym_filter(string):

    pattern = regex.compile(r'(?i)(?<=\b|[ \t_])(s[.])((?:c[.]a[.]r[.]l|r[.]l[.]s|c[.]r[.]l|a[.]p[.]a|r[.]l|p[.]a|n[.]c|a[.]s|a[.]a)[.]?)(?=[ \t]|-|_|$)')
    return regex.sub(pattern,
                    (lambda m: m.group(1).upper() + m.group(2).lower()),
                    string)


def cut_preposition_filter(string):
    pattern = regex.compile(r"(?i)(?<=[ \t])(?:sull|nell|dell|dall|all)(?='[a-z])")
    return regex.sub(pattern,
                    (lambda m: m.group().lower()),
                    string)


def preposition_filter(string):
    pattern = regex.compile(r"(?i)(?<=[ \t])(?:sullo|sulle|sulla|sugli|nello|nelle|nella|negli|dello|delle|della|degli|dallo|dalle|dalla|dagli|allo|alle|alla|agli|tra|sul|sui|per|nel|nei|fra|del|dei|dal|dai|con|su|in|di|da|al|ai|ad|a)(?=[ \t])")
    return regex.sub(pattern, (lambda m: m.group().lower()), string)


def roman_number_filter(string):
    pattern = regex.compile(r'(?iV1)(?<=^|[ \t]|[\p{P}--.])(?=[MDCLXVI])M*(?:C[MD]|D?C{0,3})(?:X[CL]|L?X{0,3})(?:I[XV]|V?I{0,3})(?=[\p{P}--.]|[ \t]|$)')
    exclude = regex.compile(r'(?i)^[MDCLV]I$')
    return regex.sub(pattern,
                    (lambda m: m.group() if (exclude.match(m.group())) else (m.group().upper())),
                    string)


def simple_conjunction_filter(string):
    pattern = regex.compile(r'(?i)(?<=[ \t])(?:ed|e|o)(?=[ \t])')
    return regex.sub(pattern,
                    (lambda m: m.group().lower()),
                    string)


def no_null_filter(string):
    if string is None:
        raise ValueError("Input is NULL: can't go ahead.")
    else:
        return string


def smart_cap(string):
    return cut_preposition_filter(
                preposition_filter(
                    abbreviation_filter(
                        simple_conjunction_filter(
                            company_type_acronym_filter(
                                roman_number_filter(
                                    capitalize_filter(
                                        no_null_filter(string)
                                    )
                                )
                            )
                        )
                    )
                )
            )
