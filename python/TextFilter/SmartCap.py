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
    return regex.sub(pattern,u', ',string)


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
        "aglie":                  u"Agliè",
        "alluvioni cambio":       u"Alluvioni Cambiò",
        "alme":                   u"Almè",
        "ali":                    u"Alì",
        "antey-saint-andre":      u"Antey-Saint-André",
        "arsie":                  u"Arsiè",
        "barzano":                u"Barzanò",
        "bascape":                u"Bascapè",
        "baselga di pine":        u"Baselga di Pinè",
        "basico":                 u"Basicò",
        "bastia mondovi":         u"Bastia Mondovì",
        "belvi":                  u"Belvì",
        "bianze":                 u"Bianzè",
        "bidoni":                 u"Bidonì",
        "budduso":                u"Buddusò",
        "cagno":                  u"Cagnò",
        "canicatti":              u"Canicattì",
        "cantu":                  u"Cantù",
        "carde":                  u"Cardè",
        "carre":                  u"Carrè",
        "carru":                  u"Carrù",
        "castel san niccolo":     u"Castel San Niccolò",
        "castelfranco piandisco": u"Castelfranco Piandiscò",
        "cavaglia":               u"Cavaglià",
        "cefalu":                 u"Cefalù",
        "centa san nicolo":       u"Centa San Nicolò",
        "cesaro":                 u"Cesarò",
        "ciglie":                 u"Cigliè",
        "cimina":                 u"Ciminà",
        "cirie":                  u"Ciriè",
        "ciro":                   u"Cirò",
        "codogne":                u"Codognè",
        "condro":                 u"Condrò",
        "cuorgne":                u"Cuorgnè",
        "dare":                   u"Darè",
        "dasa":                   u"Dasà",
        "dolce":                  u"Dolcè",
        "erbe":                   u"Erbè",
        "fenegro":                u"Fenegrò",
        "fiave":                  u"Fiavè",
        "forli":                  u"Forlì",
        "forza d'agro":           u"Forza d'Agrò",
        "fosso":                  u"Fossò",
        "frazzano":               u"Frazzanò",
        "galtelli":               u"Galtellì",
        "gambolo":                u"Gambolò",
        "gonnosno":               u"Gonnosnò",
        "gressoney-la-trinite":   u"Gressoney-la-Trinité",
        "gualtieri sicamino":     u"Gualtieri Sicaminò",
        "leini":                  u"Leinì",
        "lode":                   u"Lodè",
        "loranze":                u"Loranzè",
        "lusiglie":               u"Lusigliè",
        "maiera":                 u"Maierà",
        "male":                   u"Malè",
        "mansue":                 u"Mansuè",
        "mazze":                  u"Mazzè",
        "melicucca":              u"Melicuccà",
        "meri":                   u"Merì",
        "mondovi":                u"Mondovì",
        "montaldo di mondovi":    u"Montaldo di Mondovì",
        "monta":                  u"Montà",
        "muggio":                 u"Muggiò",
        "nardo":                  u"Nardò",
        "nughedu san nicolo":     u"Nughedu San Nicolò",
        "onani":                  u"Onanì",
        "palu":                   u"Palù",
        "panchia":                u"Panchià",
        "paterno":                u"Paternò",
        "patu":                   u"Patù",
        "petrona":                u"Petronà",
        "plati":                  u"Platì",
        "ponte san nicolo":       u"Ponte San Nicolò",
        "portobuffole":           u"Portobuffolè",
        "prela":                  u"Prelà",
        "revo":                   u"Revò",
        "rocca ciglie":           u"Rocca Cigliè",
        "roccaforte mondovi":     u"Roccaforte Mondovì",
        "ronca":                  u"Roncà",
        "rora":                   u"Rorà",
        "rosa":                   u"Rosà",
        "roveredo di gua":        u"Roveredo di Guà",
        "salo":                   u"Salò",
        "san michele mondovi":    u"San Michele Mondovì",
        "san pietro di carida":   u"San Pietro di Caridà",
        "sanfre":                 u"Sanfrè",
        "santa maria hoe":        u"Santa Maria Hoè",
        "santa maria la carita":  u"Santa Maria la Carità",
        "santhia":                u"Santhià",
        "scorze":                 u"Scorzè",
        "secli":                  u"Seclì",
        "senorbi":                u"Senorbì",
        "serra ricco":            u"Serra Riccò",
        "soddi":                  u"Soddì",
        "sorga":                  u"Sorgà",
        "staletti":               u"Stalettì",
        "temu":                   u"Temù",
        "torpe":                  u"Torpè",
        "torre mondovi":          u"Torre Mondovì",
        "tortoli":                u"Tortolì",
        "trinita":                u"Trinità",
        "vestigne":               u"Vestignè",
        "vialfre":                u"Vialfrè",
        "vigano":                 u"Viganò",
        "viggiu":                 u"Viggiù",
        "villa d'alme":           u"Villa d'Almè",
        "villanova mondovi":      u"Villanova Mondovì",
        "viu":                    u"Viù",
        "zane":                   u"Zanè",
        "zerbolo":                u"Zerbolò"
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
