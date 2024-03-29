# -*- coding: utf-8 -*-
from TextFilter import SmartCap

def test_abbreviation_filter():
    assert SmartCap.abbreviation_filter("F.LLI SASSO")               == "F.lli SASSO"
    assert SmartCap.abbreviation_filter("FR.LLI SASSO")              == "FR.LLI SASSO"
    assert SmartCap.abbreviation_filter("DOTT.SSA CRISTINA D'AVENA") == "Dott.ssa CRISTINA D'AVENA"
    assert SmartCap.abbreviation_filter("D.SSA MARIA PIA")           == "D.ssa MARIA PIA"
    assert SmartCap.abbreviation_filter("DOT.SSA NINA")              == "DOT.SSA NINA"


def test_capitalize_filter():
    assert SmartCap.capitalize_filter("DI QUESTO")                   == "Di Questo"
    assert SmartCap.capitalize_filter("A NOI")                       == "A Noi"
    assert SmartCap.capitalize_filter("VENUTI DA CUPERTINO")         == "Venuti Da Cupertino"
    assert SmartCap.capitalize_filter("IN SELLA ALLA MOTOSLITTA")    == "In Sella Alla Motoslitta"
    assert SmartCap.capitalize_filter("CON TANTA CAPARBIETÀ")        == "Con Tanta Caparbietà"
    assert SmartCap.capitalize_filter("SU PER LA MONTAGNA")          == "Su Per La Montagna"
    assert SmartCap.capitalize_filter("TRA FIERI STAMBECCHI")        == "Tra Fieri Stambecchi"
    assert SmartCap.capitalize_filter("FRA CESPUGLI ODOROSI")        == "Fra Cespugli Odorosi"
    assert SmartCap.capitalize_filter("NON INTERESSA")               == "Non Interessa"
    assert SmartCap.capitalize_filter("AD OGNI PIE' SOSPESO")        == "Ad Ogni Pie' Sospeso"
    assert SmartCap.capitalize_filter("AL SOSPIRO DEL VENTO")        == "Al Sospiro Del Vento"
    assert SmartCap.capitalize_filter("ALLO SCALPICCIO DEI CAVALLI") == "Allo Scalpiccio Dei Cavalli"
    assert SmartCap.capitalize_filter("TE-ST")                       == "Te-St"


def test_comma_space_filter():
    assert SmartCap.comma_space_filter("virgola,senza spazio")                == "virgola, senza spazio"
    assert SmartCap.comma_space_filter("virgola alla fine,")                  == "virgola alla fine,"
    assert SmartCap.comma_space_filter(",virgola iniziale e finale,")         == ", virgola iniziale e finale,"
    assert SmartCap.comma_space_filter("virgola con tab,	e senza,dopo") == "virgola con tab,	e senza, dopo"
    assert SmartCap.comma_space_filter("  ,   virgola con tab,	e senza,dopo") == "  ,   virgola con tab,	e senza, dopo"


def test_company_type_acronym_filter():
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ s.p.a.-RICCA") == "SoCiEtÀ S.p.a.-RICCA"
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ s.p.a-RICCA")  == "SoCiEtÀ S.p.a-RICCA"
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ s.r.l.")       == "SoCiEtÀ S.r.l."
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ s.r.l.s.")     == "SoCiEtÀ S.r.l.s."
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ S.N.C.")       == "SoCiEtÀ S.n.c."
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ S.c.A.r.L.")   == "SoCiEtÀ S.c.a.r.l."
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ s.C.r.L.")     == "SoCiEtÀ S.c.r.l."
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ s.A.s")        == "SoCiEtÀ S.a.s"
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ S.A.A.")       == "SoCiEtÀ S.a.a."
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ S.A.p.A.")     == "SoCiEtÀ S.a.p.a."
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ S.R.l.A.")     == "SoCiEtÀ S.R.l.A."
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ S.P.C.")       == "SoCiEtÀ S.P.C."
    assert SmartCap.company_type_acronym_filter("SoCiEtÀ S.P.A.S.")     == "SoCiEtÀ S.P.A.S."


def test_elided_preposition_filter():
    assert SmartCap.elided_preposition_filter("PER POCO SULL'ACQUA")         == "PER POCO sull'ACQUA"
    assert SmartCap.elided_preposition_filter("ANCHE NELL'ANCORA BUIO VELO") == "ANCHE nell'ANCORA BUIO VELO"
    assert SmartCap.elided_preposition_filter("DELLA SERA DELL'EST")         == "DELLA SERA dell'EST"
    assert SmartCap.elided_preposition_filter("DAL BASSO E DALL'ALTO")       == "DAL BASSO E dall'ALTO"
    assert SmartCap.elided_preposition_filter("ARRIVAVANO ALL'ALTIPIANO")    == "ARRIVAVANO all'ALTIPIANO"
    assert SmartCap.elided_preposition_filter("ROMANO D'EZZELLINO")          == "ROMANO D'EZZELLINO"


def test_preposition_filter():
    assert SmartCap.preposition_filter("PERCIÒ DI QUESTO")              == "PERCIÒ di QUESTO"
    assert SmartCap.preposition_filter("A NOI, PROPRIO A NOI")          == "A NOI, PROPRIO a NOI"
    assert SmartCap.preposition_filter("VENUTI DA CUPERTINO")           == "VENUTI da CUPERTINO"
    assert SmartCap.preposition_filter("IN SELLA ALLA MOTOSLITTA")      == "IN SELLA alla MOTOSLITTA"
    assert SmartCap.preposition_filter("PURE CON TANTA CAPARBIETÀ")     == "PURE con TANTA CAPARBIETÀ"
    assert SmartCap.preposition_filter("FIN SU PER LA MONTAGNA")        == "FIN su per LA MONTAGNA"
    assert SmartCap.preposition_filter("SALENDO TRA FIERI STAMBECCHI")  == "SALENDO tra FIERI STAMBECCHI"
    assert SmartCap.preposition_filter("E FRA CESPUGLI ODOROSI")        == "E fra CESPUGLI ODOROSI"
    assert SmartCap.preposition_filter("NON INTERESSA.")                == "NON INTERESSA."
    assert SmartCap.preposition_filter("ODE AD OGNI PIE' SOSPESO")      == "ODE ad OGNI PIE' SOSPESO"
    assert SmartCap.preposition_filter("E AL SOSPIRO DEL VENTO")        == "E al SOSPIRO del VENTO"
    assert SmartCap.preposition_filter("E ALLO SCALPICCIO DEI CAVALLI") == "E allo SCALPICCIO dei CAVALLI"


def test_province_abbreviation_filter():
    assert SmartCap.province_abbreviation_filter("Città del Vaticano (cv)")        == "Città del Vaticano (CV)"
    assert SmartCap.province_abbreviation_filter("Acciano (Aq)")                   == "Acciano (AQ)"
    assert SmartCap.province_abbreviation_filter("Altino (Ch)")                    == "Altino (CH)"
    assert SmartCap.province_abbreviation_filter("Corvara (Pe)")                   == "Corvara (PE)"
    assert SmartCap.province_abbreviation_filter("Aliano (Mt)")                    == "Aliano (MT)"
    assert SmartCap.province_abbreviation_filter("Rionero in Vulture (Pz)")        == "Rionero in Vulture (PZ)"
    assert SmartCap.province_abbreviation_filter("Laino Borgo (Cs)")               == "Laino Borgo (CS)"
    assert SmartCap.province_abbreviation_filter("Santo Stefano di Rogliano (Cs)") == "Santo Stefano di Rogliano (CS)"


def test_roman_number_filter():
    assert SmartCap.roman_number_filter("di questo xx")                                        == "di questo XX"
    assert SmartCap.roman_number_filter("a noi vii focacce")                                   == "a noi VII focacce"
    assert SmartCap.roman_number_filter("venuti da cupertino xii")                             == "venuti da cupertino XII"
    assert SmartCap.roman_number_filter("in sella alla motoslitta l")                          == "in sella alla motoslitta L"
    assert SmartCap.roman_number_filter("i,ii,iii,iv,v,vi,vii,viii,ix,x")                      == "I,II,III,IV,V,vi,VII,VIII,IX,X"
    assert SmartCap.roman_number_filter("xi,xii,xiii,xiv,xv,xvi,xvii,xviii,xix,xx")            == "XI,XII,XIII,XIV,XV,XVI,XVII,XVIII,XIX,XX"
    assert SmartCap.roman_number_filter("xxi,xxii,xxiii,xxiv,xxv,xxvi,xxvii,xxviii,xxix,xxx")  == "XXI,XXII,XXIII,XXIV,XXV,XXVI,XXVII,XXVIII,XXIX,XXX"
    assert SmartCap.roman_number_filter("... xl,")                                             == "... XL,"
    assert SmartCap.roman_number_filter("xli,xlii,xliii,xliv,xlv,xlvi,xlvii,xlviii,xlix,l")    == "XLI,XLII,XLIII,XLIV,XLV,XLVI,XLVII,XLVIII,XLIX,L"
    assert SmartCap.roman_number_filter("xc,xci,xcii,xciii,xciv,xcv,xcvi,xcvii,xcviii,xcix,c") == "XC,XCI,XCII,XCIII,XCIV,XCV,XCVI,XCVII,XCVIII,XCIX,C"
    assert SmartCap.roman_number_filter("ci,cii")                                              == "ci,CII"
    assert SmartCap.roman_number_filter("mi,di,ci,li,vi")                                      == "mi,di,ci,li,vi"
    assert SmartCap.roman_number_filter("Mi,Di,Ci,Li,Vi")                                      == "Mi,Di,Ci,Li,Vi"


def test_simple_conjunction_filter():
    assert SmartCap.simple_conjunction_filter("HANSEL E GRETEL")             == "HANSEL e GRETEL"
    assert SmartCap.simple_conjunction_filter("O MANGIAMO O ANDIAMO A CASA") == "O MANGIAMO o ANDIAMO A CASA"


def test_address_smart_cap():
    assert SmartCap.address_smart_cap("ARLETTI,DR. FLAVIO")                                          == "Arletti, Dr. Flavio"
    assert SmartCap.address_smart_cap("ATRES,S.R.L.")                                                == "Atres, S.r.l."
    assert SmartCap.address_smart_cap(",AUTOFFICINA L.R. MOTORSPORT,")                               == ", Autofficina L.R. Motorsport,"
    assert SmartCap.address_smart_cap("SPECIALISTA IN OSTETRICIA,GINECOLOGIA ED ENDOCRINOLOGIA")     == "Specialista in Ostetricia, Ginecologia ed Endocrinologia"
    assert SmartCap.address_smart_cap("VIA BOITO ARRIGO,41")                                         == "Via Boito Arrigo, 41"
    assert SmartCap.address_smart_cap("NUOVA CARROZZERIA,F.LLI MASCHIO DI MASCHIO MASSIMO & C. SNC") == "Nuova Carrozzeria, F.lli Maschio di Maschio Massimo & C. Snc"
    assert SmartCap.address_smart_cap("SANTHIA'")                                                    == 'Santhià'


def test_town_apostrophe2accent_filter():
    assert SmartCap.town_apostrophe2accent_filter("santhia'") == 'Santhià'
    assert SmartCap.town_apostrophe2accent_filter("cuorgne'") == 'Cuorgnè'
    assert SmartCap.town_apostrophe2accent_filter("forli'")   == 'Forlì'
    assert SmartCap.town_apostrophe2accent_filter("vigano'")  == 'Viganò'
    assert SmartCap.town_apostrophe2accent_filter("cefalu'")  == 'Cefalù'


def test_conditional_smart_cap():
    assert SmartCap.conditional_smart_cap("ARLETTI DR. FLAVIO", 0.95) == "Arletti Dr. Flavio"
    assert SmartCap.conditional_smart_cap("ATRES S.R.L.", 0.95) == "Atres S.r.l."
    assert SmartCap.conditional_smart_cap("Macelleria Di Gioia", 0.95) == "Macelleria Di Gioia"
    assert SmartCap.conditional_smart_cap("MaceLleRia Di Gioia", 0.95) == "Macelleria di Gioia"
    assert SmartCap.conditional_smart_cap("G come Di Gioia", 0.85) == "G come Di Gioia"
    assert SmartCap.conditional_smart_cap("G come Di Gioia", 0.95) == "G Come di Gioia"
    assert SmartCap.conditional_smart_cap("Macelleria di Biase", 0.95) == "Macelleria di Biase"
    assert SmartCap.conditional_smart_cap("CMTmotor - Centro Moto Ticino Bergamo", 0.90) == "CMTmotor - Centro Moto Ticino Bergamo"


def test_smart_cap():
    assert SmartCap.smart_cap("ARLETTI DR. FLAVIO")                                                            == "Arletti Dr. Flavio"
    assert SmartCap.smart_cap("ATRES S.R.L.")                                                                  == "Atres S.r.l."
    assert SmartCap.smart_cap("AUTOFFICINA L.R. MOTORSPORT")                                                   == "Autofficina L.R. Motorsport"
    assert SmartCap.smart_cap("AUTOSTYLE S.N.C.")                                                              == "Autostyle S.n.c."
    assert SmartCap.smart_cap("AVV. CRISTINA SCOTTI")                                                          == "Avv. Cristina Scotti"
    assert SmartCap.smart_cap("AZALEA S.A.S. DI AZZALE FRANCO E PIETRO & C.")                                  == "Azalea S.a.s. di Azzale Franco e Pietro & C."
    assert SmartCap.smart_cap("BAR SPORT S.A.S. DI WANG WEIQIN E C.")                                          == "Bar Sport S.a.s. di Wang Weiqin e C."
    assert SmartCap.smart_cap("BAR SPRINT S.N.C. DI MOCCIA CLAUDIO")                                           == "Bar Sprint S.n.c. di Moccia Claudio"
    assert SmartCap.smart_cap("BASE S.P.A.")                                                                   == "Base S.p.a."
    assert SmartCap.smart_cap("BERARDI AVV. FILIPPO MARIA")                                                    == "Berardi Avv. Filippo Maria"
    assert SmartCap.smart_cap("BRUGNATO HEAT & DRINK SNC")                                                     == "Brugnato Heat & Drink Snc"
    assert SmartCap.smart_cap("CAFFE' PAGLIA DI BANI EGLANTINA")                                               == "Caffe' Paglia di Bani Eglantina"
    assert SmartCap.smart_cap("CANNAVO' GAETANO SRL")                                                          == "Cannavo' Gaetano Srl"
    assert SmartCap.smart_cap("CANNAVO' GAETANO S.R.L.")                                                       == "Cannavo' Gaetano S.r.l."
    assert SmartCap.smart_cap("CARAIBI 2 S.N.C DI MICHELA FALCO & C.")                                         == "Caraibi 2 S.n.c di Michela Falco & C."
    assert SmartCap.smart_cap("CENTRO ESTETICO GOCCE D'AMBRA")                                                 == "Centro Estetico Gocce D'Ambra"
    assert SmartCap.smart_cap("CHIRIATTI EDILIZIA S.A.S. DI CHIRIATTI FLAVIO & C.")                            == "Chiriatti Edilizia S.a.s. di Chiriatti Flavio & C."
    assert SmartCap.smart_cap("CONTI CAV. COLOMBO COSTRUZIONI EDILI E RESTAURI DI CONTI RANDOLFO & C. S.N.C.") == "Conti Cav. Colombo Costruzioni Edili e Restauri di Conti Randolfo & C. S.n.c."
    assert SmartCap.smart_cap("D'ALOISIO AVV. CLAUDIA STUDIO LEGALE")                                          == "D'Aloisio Avv. Claudia Studio Legale"
    assert SmartCap.smart_cap("D.A.I. S.R.L.")                                                                 == "D.A.I. S.r.l."
    assert SmartCap.smart_cap("SOCIETÀ XX SETTEMBRE")                                                          == "Società XX Settembre"
    assert SmartCap.smart_cap("EDIL DBN S.A.S. DI DI BENEDETTO NICOLA E C.")                                   == "Edil Dbn S.a.s. di di Benedetto Nicola e C."
    assert SmartCap.smart_cap("EFFELLE SISTEMI S.R.L.")                                                        == "Effelle Sistemi S.r.l."
    assert SmartCap.smart_cap("ESPANA S.A.S. DI MONTELLA MARIANO & C.")                                        == "Espana S.a.s. di Montella Mariano & C."
    assert SmartCap.smart_cap("F.A.M.I.P.")                                                                    == "F.A.M.I.P."
    assert SmartCap.smart_cap("FIORDIROCCIA S.A.S. DI SCALET MARINO & C.")                                     == "Fiordiroccia S.a.s. di Scalet Marino & C."
    assert SmartCap.smart_cap("FIORIN F.LLI")                                                                  == "Fiorin F.lli"
    assert SmartCap.smart_cap("FREE SLIM DI TIBET S.A.S.")                                                     == "Free Slim di Tibet S.a.s."
    assert SmartCap.smart_cap("G.M.G. S.A.S. DI COPPOLA GIULIO E C.")                                          == "G.M.G. S.a.s. di Coppola Giulio e C."
    assert SmartCap.smart_cap("GARNÌ STELLA ALPINA")                                                           == "Garnì Stella Alpina"
    assert SmartCap.smart_cap("GE.MI.SO. DI LOPES GIUSEPPE MARCELLO")                                          == "Ge.Mi.So. di Lopes Giuseppe Marcello"
    assert SmartCap.smart_cap("GUARESCHI DR. SANDRA")                                                          == "Guareschi Dr. Sandra"
    assert SmartCap.smart_cap("HOTEL CAVALLINO - S' RÃSSL")                                                == "Hotel Cavallino - S' RãSsl"
    assert SmartCap.smart_cap("HOTEL LA GINESTRA S.R.L.")                                                      == "Hotel La Ginestra S.r.l."
    assert SmartCap.smart_cap("I.B.S. SRL")                                                                    == "I.B.S. Srl"
    assert SmartCap.smart_cap("I.T.I.D. DI PARENTI O. E PERI R. E C. SAS")                                     == "I.T.I.D. di Parenti O. e Peri R. e C. Sas"
    assert SmartCap.smart_cap("IMPIANTI ZERBO DI ZERBO ANDREA A.")                                             == "Impianti Zerbo di Zerbo Andrea A."
    assert SmartCap.smart_cap("IMPRESA C.F. GENTA 1848 S.R.L.")                                                == "Impresa C.F. Genta 1848 S.r.l."
    assert SmartCap.smart_cap("IMPRESA FORESTI - costruzioni edili dal 1972")                                  == "Impresa Foresti - Costruzioni Edili dal 1972"
    assert SmartCap.smart_cap("ING. CAIONE COSTRUZIONI S.R.L.")                                                == "Ing. Caione Costruzioni S.r.l."
    assert SmartCap.smart_cap("INVIDIA CAFE' DI ROVERSI GIANLUCA & C. SAS")                                    == "Invidia Cafe' di Roversi Gianluca & C. Sas"
    assert SmartCap.smart_cap("IPPOLITO A.S.STUDIO ODONTOIATRICO ASSOCIATO")                                   == "Ippolito A.S.Studio Odontoiatrico Associato"
    assert SmartCap.smart_cap("ISTITUTO DI BELLEZZA' DONATELLA'")                                              == "Istituto di Bellezza' Donatella'"
    assert SmartCap.smart_cap("LA MAISON DE LA BEAUTE' S.A.S. DI FIORITO CONCETTA")                            == "La Maison De La Beaute' S.a.s. di Fiorito Concetta"
    assert SmartCap.smart_cap("LA MARIC S.A.S. DI RICCIO GAETANO")                                             == "La Maric S.a.s. di Riccio Gaetano"
    assert SmartCap.smart_cap("LA PIOLA D'LE 2 SURELE")                                                        == "La Piola D'Le 2 Surele"
    assert SmartCap.smart_cap("LATTERIA#21")                                                                   == "Latteria#21"
    assert SmartCap.smart_cap("LE NINFEE ESTETICA & BENESSERE")                                                == "Le Ninfee Estetica & Benessere"
    assert SmartCap.smart_cap("LERARIO AVV. NICOLA")                                                           == "Lerario Avv. Nicola"
    assert SmartCap.smart_cap("LISA AVV. SANTI")                                                               == "Lisa Avv. Santi"
    assert SmartCap.smart_cap("LUALDI S.P.A.")                                                                 == "Lualdi S.p.a."
    assert SmartCap.smart_cap("M.S. CREM DI SABRINA MANFRONI")                                                 == "M.S. Crem di Sabrina Manfroni"
    assert SmartCap.smart_cap("MARA MEO S.R.L.")                                                               == "Mara Meo S.r.l."
    assert SmartCap.smart_cap("MARGAGLIOTTI PORTE & FINESTRE")                                                 == "Margagliotti Porte & Finestre"
    assert SmartCap.smart_cap("MASE' EZIO")                                                                    == "Mase' Ezio"
    assert SmartCap.smart_cap("MILK S.A.S. DI LUCIFORA SALVATORE & C.")                                        == "Milk S.a.s. di Lucifora Salvatore & C."
    assert SmartCap.smart_cap("MILLENNIUM SNC DI RICCIARDI FABIO ROCCO & C.")                                  == "Millennium Snc di Ricciardi Fabio Rocco & C."
    assert SmartCap.smart_cap("ML IMPIANTI S.R.L.")                                                            == "ML Impianti S.r.l."
    assert SmartCap.smart_cap("NEW BODY ESTETICA & BENESSERE")                                                 == "New Body Estetica & Benessere"
    assert SmartCap.smart_cap("NSQ SOCIETA' COOPERATIVA")                                                      == "Nsq Societa' Cooperativa"
    assert SmartCap.smart_cap("NUOVA CARROZZERIA F.LLI MASCHIO DI MASCHIO MASSIMO & C. SNC")                   == "Nuova Carrozzeria F.lli Maschio di Maschio Massimo & C. Snc"
    assert SmartCap.smart_cap("NUOVA PROGRESS S.R.L.")                                                         == "Nuova Progress S.r.l."
    assert SmartCap.smart_cap("O.VAL SRL")                                                                     == "O.Val Srl"
    assert SmartCap.smart_cap("OLIMPIA FOOD S.R.L.")                                                           == "Olimpia Food S.r.l."
    assert SmartCap.smart_cap("ONORANZE FUNEBRI MAIOLINI ALBINO DIR. TEC. PIERINO BETELLI")                    == "Onoranze Funebri Maiolini Albino Dir. Tec. Pierino Betelli"
    assert SmartCap.smart_cap("ONORANZE FUNEBRI S. BARBARA")                                                   == "Onoranze Funebri S. Barbara"
    assert SmartCap.smart_cap("PEREGO AVV. DANIELA")                                                           == "Perego Avv. Daniela"
    assert SmartCap.smart_cap("PERIANO S.C.R.L.")                                                              == "Periano S.c.r.l."
    assert SmartCap.smart_cap("PIZZA PARTY SNC DI MONTANA MICHELE & VILLARASPI")                               == "Pizza Party Snc di Montana Michele & Villaraspi"
    assert SmartCap.smart_cap("PIZZERIA-FRIGGITORIA \"MADE IN SALVO\"")                                        == "Pizzeria-Friggitoria \"Made in Salvo\""
    assert SmartCap.smart_cap("POLITERMICA INDUSTRIALE S.P.A")                                                 == "Politermica Industriale S.p.a"
    assert SmartCap.smart_cap("POLIZIANI DR. GIOVANNI")                                                        == "Poliziani Dr. Giovanni"
    assert SmartCap.smart_cap("PRESTIGE S.R.L.")                                                               == "Prestige S.r.l."
    assert SmartCap.smart_cap("PROFUMERIA ACADEMIE BEAUTE - CENTRO ESTETICO")                                  == "Profumeria Academie Beaute - Centro Estetico"
    assert SmartCap.smart_cap("RISTORANTE LA TARTANA DA MARIO L'OSTRICARO sas")                                == "Ristorante La Tartana da Mario L'Ostricaro Sas"
    assert SmartCap.smart_cap("RIZZO AVV. GABRIELE")                                                           == "Rizzo Avv. Gabriele"
    assert SmartCap.smart_cap("S.C.I. SOCIETA' COSTRUZIONI INDUSTRIALI SRL")                                   == "S.C.I. Societa' Costruzioni Industriali Srl"
    assert SmartCap.smart_cap("SANDONA' GOMME - CENTRO PNEUMATICI")                                            == "Sandona' Gomme - Centro Pneumatici"
    assert SmartCap.smart_cap("SAVIO TECNOIMPIANTI - IMPIANTI TERMOIDRAULICI")                                 == "Savio Tecnoimpianti - Impianti Termoidraulici"
    assert SmartCap.smart_cap("SERRAMENTI ARREDAMENTI G.F.")                                                   == "Serramenti Arredamenti G.F."
    assert SmartCap.smart_cap("SETTIMO DENTAL SNC DI TROTTA PASQUALE E C.")                                    == "Settimo Dental Snc di Trotta Pasquale e C."
    assert SmartCap.smart_cap("SEVEN ZEE DI ZONTA LUIGI & C. SNC")                                             == "Seven Zee di Zonta Luigi & C. Snc"
    assert SmartCap.smart_cap("SOCIETA' ACCARDO MARINI SRL")                                                   == "Societa' Accardo Marini Srl"
    assert SmartCap.smart_cap("SOCIETA' PACIFIC DI FORST ROSEMARIE SIGRID E C. SNC")                           == "Societa' Pacific di Forst Rosemarie Sigrid e C. Snc"
    assert SmartCap.smart_cap("SOPPELSA TERMOIDRAULICA S.N.C. DI SOPPELSA FULVIO & F.LLI")                     == "Soppelsa Termoidraulica S.n.c. di Soppelsa Fulvio & F.lli"
    assert SmartCap.smart_cap("SPINETTO DR ROBERTO E DR.SSA GIULIA STUDIO DENTISTICO ASSOCIATO")               == "Spinetto Dr Roberto e Dr.ssa Giulia Studio Dentistico Associato"
    assert SmartCap.smart_cap("STN CONSULTING S.A.S. DI GIANLUCA NUNNARI E C. SERVIZI DI INGEGNERIA")          == "Stn Consulting S.a.s. di Gianluca Nunnari e C. Servizi di Ingegneria"
    assert SmartCap.smart_cap("STRATO S.R.L.")                                                                 == "Strato S.r.l."
    assert SmartCap.smart_cap("STUDIO DENTISTICO ASS.TO DR. F. BEVILACQUA, G. PIANCA, V. PIANCA")              == "Studio Dentistico Ass.to Dr. F. Bevilacqua, G. Pianca, V. Pianca"
    assert SmartCap.smart_cap("STUDIO DENTISTICO IACONO DOTT.SSA LIVIA")                                       == "Studio Dentistico Iacono Dott.ssa Livia"
    assert SmartCap.smart_cap("STUDIO DENTISTICO MARESCHI DR. PAOLO E BASSUTTI DR. FABIO")                     == "Studio Dentistico Mareschi Dr. Paolo e Bassutti Dr. Fabio"
    assert SmartCap.smart_cap("STYLCAR CARROZZERIA S.N.C. DI SANDRI GRAZIANO")                                 == "Stylcar Carrozzeria S.n.c. di Sandri Graziano"
    assert SmartCap.smart_cap("T.S.TERMOIDRAULICA")                                                            == "T.S.Termoidraulica"
    assert SmartCap.smart_cap("TECNOIMPIANTI PERSALI S.R.L.")                                                  == "Tecnoimpianti Persali S.r.l."
    assert SmartCap.smart_cap("TECNOVERDE DEL DOTT. FRANCESCO VATTERONI AGRONOMO PAESAGGISTA")                 == "Tecnoverde del Dott. Francesco Vatteroni Agronomo Paesaggista"
    assert SmartCap.smart_cap("TERMOIDRAULICA DUE ZETA SNC - DI ZOBBI E. & ZANNONI R.")                        == "Termoidraulica Due Zeta Snc - di Zobbi E. & Zannoni R."
    assert SmartCap.smart_cap("TRATTORIA SAN PIETRO SNC DI TOSATTO GIOVANNI & C.")                             == "Trattoria San Pietro Snc di Tosatto Giovanni & C."
    assert SmartCap.smart_cap("VERDE AMBIENTE PICC. SOC. COOP. A R.L.")                                        == "Verde Ambiente Picc. Soc. Coop. a R.L."
    assert SmartCap.smart_cap("VERDE VAN PIK S.N.C. DI CHINELLATO MICHELE E MIGOTTO MAURIZIO")                 == "Verde Van Pik S.n.c. di Chinellato Michele e Migotto Maurizio"
    assert SmartCap.smart_cap("VIRGINIA CINQUE STELLE S.R.L.")                                                 == "Virginia Cinque Stelle S.r.l."
    assert SmartCap.smart_cap("DI FARIELLO PASQUALE")                                                          == "Di Fariello Pasquale"
    assert SmartCap.smart_cap("SPECIALISTA IN OSTETRICIA, GINECOLOGIA ED ENDOCRINOLOGIA")                      == "Specialista in Ostetricia, Ginecologia ed Endocrinologia"
    assert SmartCap.smart_cap("SARTORIS D.SSA LAURA")                                                          == "Sartoris D.ssa Laura"
    assert SmartCap.smart_cap("REBOLINI GIORGIO_ASSISTENZA RIELLO")                                            == "Rebolini Giorgio_Assistenza Riello"
    assert SmartCap.smart_cap("GRAZIOLI CLIMASERVICE S.R.L._AGENZIA E ASSISTENZA RIELLO")                      == "Grazioli Climaservice S.r.l._Agenzia e Assistenza Riello"
    assert SmartCap.smart_cap("ROMANO D'EZZELLINO")                                                            == "Romano D'Ezzellino"
