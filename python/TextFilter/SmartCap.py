# -*- coding: utf-8 -*-
import regex
import jellyfish


def abbreviation_filter(string):
    pattern = regex.compile(r'(?i)\b(?:prof[.]ssa|dott[.]ssa|stim[.]mo|preg[.]mo|gent[.]mo|gent[.]mi|gent[.]me|gent[.]ma|chia[.]mo|dr[.]ssa|sig[.]ra|sig[.]na|ill[.]mo|ass[.]to|egr[.]ia|d[.]ssa|f[.]lli|egr[.]i|v[.]le|p[.]za|c[.]so)\b')
    return regex.sub(pattern,
                    (lambda m: m.group()[:1].upper() + m.group()[1:].lower()),
                    string)


def comma_space_filter(string):
    pattern = regex.compile(r',(?=[^ \t])')
    return regex.sub(pattern,', ',string)


def capitalize_filter(string):
    pattern = regex.compile(r'(?<=\b|_)[a-z]')
    return regex.sub(pattern, (lambda m: m.group().upper()), string.lower())


def company_type_acronym_filter(string):
    pattern = regex.compile(r'(?i)(?<=\b|[ \t_])(s[.])((?:c[.]a[.]r[.]l|r[.]l[.]s|c[.]r[.]l|a[.]p[.]a|r[.]l|p[.]a|n[.]c|a[.]s|a[.]a)[.]?)(?=[ \t]|-|_|$)')
    return regex.sub(pattern,
                    (lambda m: m.group(1).upper() + m.group(2).lower()),
                    string)


def elided_preposition_filter(string):
    pattern = regex.compile(r"(?i)(?<=[ \t])(?:sull|nell|dell|dall|all)(?='[a-z])")
    return regex.sub(pattern,
                    (lambda m: m.group().lower()),
                    string)


def preposition_filter(string):
    pattern = regex.compile(r"(?i)(?<=[ \t])(?:sullo|sulle|sulla|sugli|nello|nelle|nella|negli|dello|delle|della|degli|dallo|dalle|dalla|dagli|allo|alle|alla|agli|tra|sul|sui|per|nel|nei|fra|del|dei|dal|dai|con|su|in|di|da|al|ai|ad|a)(?=[ \t])")
    return regex.sub(pattern, (lambda m: m.group().lower()), string)


def province_abbreviation_filter(string):
    pattern = regex.compile(r'(?i)(?<=[(])(?:AG|AL|AN|AO|AP|AQ|AR|AT|AV|BA|BG|BI|BL|BN|BO|BR|BS|BT|BZ|CA|CB|CE|CH|CI|CL|CN|CO|CR|CS|CT|CV|CZ|EN|FC|FE|FG|FI|FM|FR|GE|GO|GR|IM|IS|KR|LC|LE|LI|LO|LT|LU|MB|MC|ME|MI|MN|MO|MS|MT|NA|NO|NU|OG|OR|OT|PA|PC|PD|PE|PG|PI|PN|PO|PR|PT|PU|PV|PZ|RA|RC|RE|RG|RI|RM|RN|RO|SA|SI|SM|SO|SP|SR|SS|SV|TA|TE|TN|TO|TP|TR|TS|TV|UD|VA|VB|VC|VE|VI|VR|VS|VT|VV)(?=[)])')
    return regex.sub(pattern, (lambda m: m.group().upper()), string)


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



def town_apostrophe2accent_filter(string):
    accented_towns = {
        "aglie":                  "Agliè",
        "alluvioni cambio":       "Alluvioni Cambiò",
        "alme":                   "Almè",
        "ali":                    "Alì",
        "antey-saint-andre":      "Antey-Saint-André",
        "arsie":                  "Arsiè",
        "barzano":                "Barzanò",
        "bascape":                "Bascapè",
        "baselga di pine":        "Baselga di Pinè",
        "basico":                 "Basicò",
        "bastia mondovi":         "Bastia Mondovì",
        "belvi":                  "Belvì",
        "bianze":                 "Bianzè",
        "bidoni":                 "Bidonì",
        "budduso":                "Buddusò",
        "cagno":                  "Cagnò",
        "canicatti":              "Canicattì",
        "cantu":                  "Cantù",
        "carde":                  "Cardè",
        "carre":                  "Carrè",
        "carru":                  "Carrù",
        "castel san niccolo":     "Castel San Niccolò",
        "castelfranco piandisco": "Castelfranco Piandiscò",
        "cavaglia":               "Cavaglià",
        "cefalu":                 "Cefalù",
        "centa san nicolo":       "Centa San Nicolò",
        "cesaro":                 "Cesarò",
        "ciglie":                 "Cigliè",
        "cimina":                 "Ciminà",
        "cirie":                  "Ciriè",
        "ciro":                   "Cirò",
        "codogne":                "Codognè",
        "condro":                 "Condrò",
        "cuorgne":                "Cuorgnè",
        "dare":                   "Darè",
        "dasa":                   "Dasà",
        "dolce":                  "Dolcè",
        "erbe":                   "Erbè",
        "fenegro":                "Fenegrò",
        "fiave":                  "Fiavè",
        "forli":                  "Forlì",
        "forza d'agro":           "Forza d'Agrò",
        "fosso":                  "Fossò",
        "frazzano":               "Frazzanò",
        "galtelli":               "Galtellì",
        "gambolo":                "Gambolò",
        "gonnosno":               "Gonnosnò",
        "gressoney-la-trinite":   "Gressoney-la-Trinité",
        "gualtieri sicamino":     "Gualtieri Sicaminò",
        "leini":                  "Leinì",
        "lode":                   "Lodè",
        "loranze":                "Loranzè",
        "lusiglie":               "Lusigliè",
        "maiera":                 "Maierà",
        "male":                   "Malè",
        "mansue":                 "Mansuè",
        "mazze":                  "Mazzè",
        "melicucca":              "Melicuccà",
        "meri":                   "Merì",
        "mondovi":                "Mondovì",
        "montaldo di mondovi":    "Montaldo di Mondovì",
        "monta":                  "Montà",
        "muggio":                 "Muggiò",
        "nardo":                  "Nardò",
        "nughedu san nicolo":     "Nughedu San Nicolò",
        "onani":                  "Onanì",
        "palu":                   "Palù",
        "panchia":                "Panchià",
        "paterno":                "Paternò",
        "patu":                   "Patù",
        "petrona":                "Petronà",
        "plati":                  "Platì",
        "ponte san nicolo":       "Ponte San Nicolò",
        "portobuffole":           "Portobuffolè",
        "prela":                  "Prelà",
        "revo":                   "Revò",
        "rocca ciglie":           "Rocca Cigliè",
        "roccaforte mondovi":     "Roccaforte Mondovì",
        "ronca":                  "Roncà",
        "rora":                   "Rorà",
        "rosa":                   "Rosà",
        "roveredo di gua":        "Roveredo di Guà",
        "salo":                   "Salò",
        "san michele mondovi":    "San Michele Mondovì",
        "san pietro di carida":   "San Pietro di Caridà",
        "sanfre":                 "Sanfrè",
        "santa maria hoe":        "Santa Maria Hoè",
        "santa maria la carita":  "Santa Maria la Carità",
        "santhia":                "Santhià",
        "scorze":                 "Scorzè",
        "secli":                  "Seclì",
        "senorbi":                "Senorbì",
        "serra ricco":            "Serra Riccò",
        "soddi":                  "Soddì",
        "sorga":                  "Sorgà",
        "staletti":               "Stalettì",
        "temu":                   "Temù",
        "torpe":                  "Torpè",
        "torre mondovi":          "Torre Mondovì",
        "tortoli":                "Tortolì",
        "trinita":                "Trinità",
        "vestigne":               "Vestignè",
        "vialfre":                "Vialfrè",
        "vigano":                 "Viganò",
        "viggiu":                 "Viggiù",
        "villa d'alme":           "Villa d'Almè",
        "villanova mondovi":      "Villanova Mondovì",
        "viu":                    "Viù",
        "zane":                   "Zanè",
        "zerbolo":                "Zerbolò"
    }
    pattern = regex.compile(r"(?i)(\w+[aeiou])'(?=[\p{P}&&[^.]]|[ \t]|$)")
    return regex.sub(pattern, 
                    (lambda m: accented_towns.get(m.group(1).lower(),m.group())),
                    string)


def no_null_filter(string):
    if string is None:
        raise ValueError("Input is NULL: can't go ahead.")
    else:
        return string


def smart_cap(string):
    return elided_preposition_filter(
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


def address_smart_cap(string):
    return comma_space_filter(
                town_apostrophe2accent_filter(
                    smart_cap(string)
                )
           )


def conditional_smart_cap(string,threshold):
    filtered = smart_cap(string)
    distance = jellyfish.jaro_winkler(filtered, string)
    return string if distance >= float(threshold) else filtered
