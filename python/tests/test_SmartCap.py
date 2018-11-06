# -*- coding: utf-8 -*-
from TextFilter import SmartCap


def test_abbreviation_filter():
    assert SmartCap.abbreviation_filter(u"F.LLI SASSO")               == u"F.lli SASSO"
    assert SmartCap.abbreviation_filter(u"FR.LLI SASSO")              == u"FR.LLI SASSO"
    assert SmartCap.abbreviation_filter(u"DOTT.SSA CRISTINA D'AVENA") == u"Dott.ssa CRISTINA D'AVENA"
    assert SmartCap.abbreviation_filter(u"D.SSA MARIA PIA")           == u"D.ssa MARIA PIA"
    assert SmartCap.abbreviation_filter(u"DOT.SSA NINA")              == u"DOT.SSA NINA"


def test_capitalize_filter():
    assert SmartCap.capitalize_filter(u"DI QUESTO")                   == u"Di Questo"
    assert SmartCap.capitalize_filter(u"A NOI")                       == u"A Noi"
    assert SmartCap.capitalize_filter(u"VENUTI DA CUPERTINO")         == u"Venuti Da Cupertino"
    assert SmartCap.capitalize_filter(u"IN SELLA ALLA MOTOSLITTA")    == u"In Sella Alla Motoslitta"
    assert SmartCap.capitalize_filter(u"CON TANTA CAPARBIETÀ")        == u"Con Tanta Caparbietà"
    assert SmartCap.capitalize_filter(u"SU PER LA MONTAGNA")          == u"Su Per La Montagna"
    assert SmartCap.capitalize_filter(u"TRA FIERI STAMBECCHI")        == u"Tra Fieri Stambecchi"
    assert SmartCap.capitalize_filter(u"FRA CESPUGLI ODOROSI")        == u"Fra Cespugli Odorosi"
    assert SmartCap.capitalize_filter(u"NON INTERESSA")               == u"Non Interessa"
    assert SmartCap.capitalize_filter(u"AD OGNI PIE' SOSPESO")        == u"Ad Ogni Pie' Sospeso"
    assert SmartCap.capitalize_filter(u"AL SOSPIRO DEL VENTO")        == u"Al Sospiro Del Vento"
    assert SmartCap.capitalize_filter(u"ALLO SCALPICCIO DEI CAVALLI") == u"Allo Scalpiccio Dei Cavalli"
    assert SmartCap.capitalize_filter(u"TE-ST")                       == u"Te-St"


def test_company_type_acronym_filter():
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ s.p.a.-RICCA") == u"SoCiEtÀ S.p.a.-RICCA"
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ s.p.a-RICCA")  == u"SoCiEtÀ S.p.a-RICCA"
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ s.r.l.")       == u"SoCiEtÀ S.r.l."
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ s.r.l.s.")     == u"SoCiEtÀ S.r.l.s."
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ S.N.C.")       == u"SoCiEtÀ S.n.c."
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ S.c.A.r.L.")   == u"SoCiEtÀ S.c.a.r.l."
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ s.C.r.L.")     == u"SoCiEtÀ S.c.r.l."
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ s.A.s")        == u"SoCiEtÀ S.a.s"
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ S.A.A.")       == u"SoCiEtÀ S.a.a."
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ S.A.p.A.")     == u"SoCiEtÀ S.a.p.a."
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ S.R.l.A.")     == u"SoCiEtÀ S.R.l.A."
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ S.P.C.")       == u"SoCiEtÀ S.P.C."
    assert SmartCap.company_type_acronym_filter(u"SoCiEtÀ S.P.A.S.")     == u"SoCiEtÀ S.P.A.S."


def test_cut_preposition_filter():
    assert SmartCap.cut_preposition_filter(u"PER POCO SULL'ACQUA")         == u"PER POCO sull'ACQUA"
    assert SmartCap.cut_preposition_filter(u"ANCHE NELL'ANCORA BUIO VELO") == u"ANCHE nell'ANCORA BUIO VELO"
    assert SmartCap.cut_preposition_filter(u"DELLA SERA DELL'EST")         == u"DELLA SERA dell'EST"
    assert SmartCap.cut_preposition_filter(u"DAL BASSO E DALL'ALTO")       == u"DAL BASSO E dall'ALTO"
    assert SmartCap.cut_preposition_filter(u"ARRIVAVANO ALL'ALTIPIANO")    == u"ARRIVAVANO all'ALTIPIANO"

def test_preposition_filter():
    assert SmartCap.preposition_filter(u"PERCIÒ DI QUESTO")              == u"PERCIÒ di QUESTO"
    assert SmartCap.preposition_filter(u"A NOI, PROPRIO A NOI")          == u"A NOI, PROPRIO a NOI"
    assert SmartCap.preposition_filter(u"VENUTI DA CUPERTINO")           == u"VENUTI da CUPERTINO"
    assert SmartCap.preposition_filter(u"IN SELLA ALLA MOTOSLITTA")      == u"IN SELLA alla MOTOSLITTA"
    assert SmartCap.preposition_filter(u"PURE CON TANTA CAPARBIETÀ")     == u"PURE con TANTA CAPARBIETÀ"
    assert SmartCap.preposition_filter(u"FIN SU PER LA MONTAGNA")        == u"FIN su per LA MONTAGNA"
    assert SmartCap.preposition_filter(u"SALENDO TRA FIERI STAMBECCHI")  == u"SALENDO tra FIERI STAMBECCHI"
    assert SmartCap.preposition_filter(u"E FRA CESPUGLI ODOROSI")        == u"E fra CESPUGLI ODOROSI"
    assert SmartCap.preposition_filter(u"NON INTERESSA.")                == u"NON INTERESSA."
    assert SmartCap.preposition_filter(u"ODE AD OGNI PIE' SOSPESO")      == u"ODE ad OGNI PIE' SOSPESO"
    assert SmartCap.preposition_filter(u"E AL SOSPIRO DEL VENTO")        == u"E al SOSPIRO del VENTO"
    assert SmartCap.preposition_filter(u"E ALLO SCALPICCIO DEI CAVALLI") == u"E allo SCALPICCIO dei CAVALLI"


def test_roman_number_filter():
    assert SmartCap.roman_number_filter(u"di questo xx")                                        == u"di questo XX"
    assert SmartCap.roman_number_filter(u"a noi vii focacce")                                   == u"a noi VII focacce"
    assert SmartCap.roman_number_filter(u"venuti da cupertino xii")                             == u"venuti da cupertino XII"
    assert SmartCap.roman_number_filter(u"in sella alla motoslitta l")                          == u"in sella alla motoslitta L"
    assert SmartCap.roman_number_filter(u"i,ii,iii,iv,v,vi,vii,viii,ix,x")                      == u"I,II,III,IV,V,vi,VII,VIII,IX,X"
    assert SmartCap.roman_number_filter(u"xi,xii,xiii,xiv,xv,xvi,xvii,xviii,xix,xx")            == u"XI,XII,XIII,XIV,XV,XVI,XVII,XVIII,XIX,XX"
    assert SmartCap.roman_number_filter(u"xxi,xxii,xxiii,xxiv,xxv,xxvi,xxvii,xxviii,xxix,xxx")  == u"XXI,XXII,XXIII,XXIV,XXV,XXVI,XXVII,XXVIII,XXIX,XXX"
    assert SmartCap.roman_number_filter(u"... xl,")                                             == u"... XL,"
    assert SmartCap.roman_number_filter(u"xli,xlii,xliii,xliv,xlv,xlvi,xlvii,xlviii,xlix,l")    == u"XLI,XLII,XLIII,XLIV,XLV,XLVI,XLVII,XLVIII,XLIX,L"
    assert SmartCap.roman_number_filter(u"xc,xci,xcii,xciii,xciv,xcv,xcvi,xcvii,xcviii,xcix,c") == u"XC,XCI,XCII,XCIII,XCIV,XCV,XCVI,XCVII,XCVIII,XCIX,C"
    assert SmartCap.roman_number_filter(u"ci,cii")                                              == u"ci,CII"
    assert SmartCap.roman_number_filter(u"mi,di,ci,li,vi")                                      == u"mi,di,ci,li,vi"
    assert SmartCap.roman_number_filter(u"Mi,Di,Ci,Li,Vi")                                      == u"Mi,Di,Ci,Li,Vi"


def test_simple_conjunction_filter():
    assert SmartCap.simple_conjunction_filter(u'HANSEL E GRETEL')             == u'HANSEL e GRETEL'
    assert SmartCap.simple_conjunction_filter(u'O MANGIAMO O ANDIAMO A CASA') == u'O MANGIAMO o ANDIAMO A CASA'


def test_smart_cap():
    assert SmartCap.smart_cap(u"ARLETTI DR. FLAVIO")                                                            == u"Arletti Dr. Flavio"
    assert SmartCap.smart_cap(u"ATRES S.R.L.")                                                                  == u"Atres S.r.l."
    assert SmartCap.smart_cap(u"AUTOFFICINA L.R. MOTORSPORT")                                                   == u"Autofficina L.R. Motorsport"
    assert SmartCap.smart_cap(u"AUTOSTYLE S.N.C.")                                                              == u"Autostyle S.n.c."
    assert SmartCap.smart_cap(u"AVV. CRISTINA SCOTTI")                                                          == u"Avv. Cristina Scotti"
    assert SmartCap.smart_cap(u"AZALEA S.A.S. DI AZZALE FRANCO E PIETRO & C.")                                  == u"Azalea S.a.s. di Azzale Franco e Pietro & C."
    assert SmartCap.smart_cap(u"BAR SPORT S.A.S. DI WANG WEIQIN E C.")                                          == u"Bar Sport S.a.s. di Wang Weiqin e C."
    assert SmartCap.smart_cap(u"BAR SPRINT S.N.C. DI MOCCIA CLAUDIO")                                           == u"Bar Sprint S.n.c. di Moccia Claudio"
    assert SmartCap.smart_cap(u"BASE S.P.A.")                                                                   == u"Base S.p.a."
    assert SmartCap.smart_cap(u"BERARDI AVV. FILIPPO MARIA")                                                    == u"Berardi Avv. Filippo Maria"
    assert SmartCap.smart_cap(u"BRUGNATO HEAT & DRINK SNC")                                                     == u"Brugnato Heat & Drink Snc"
    assert SmartCap.smart_cap(u"CAFFE' PAGLIA DI BANI EGLANTINA")                                               == u"Caffe' Paglia di Bani Eglantina"
    assert SmartCap.smart_cap(u"CANNAVO' GAETANO SRL")                                                          == u"Cannavo' Gaetano Srl"
    assert SmartCap.smart_cap(u"CANNAVO' GAETANO S.R.L.")                                                       == u"Cannavo' Gaetano S.r.l."
    assert SmartCap.smart_cap(u"CARAIBI 2 S.N.C DI MICHELA FALCO & C.")                                         == u"Caraibi 2 S.n.c di Michela Falco & C."
    assert SmartCap.smart_cap(u"CENTRO ESTETICO GOCCE D'AMBRA")                                                 == u"Centro Estetico Gocce D'Ambra"
    assert SmartCap.smart_cap(u"CHIRIATTI EDILIZIA S.A.S. DI CHIRIATTI FLAVIO & C.")                            == u"Chiriatti Edilizia S.a.s. di Chiriatti Flavio & C."
    assert SmartCap.smart_cap(u"CONTI CAV. COLOMBO COSTRUZIONI EDILI E RESTAURI DI CONTI RANDOLFO & C. S.N.C.") == u"Conti Cav. Colombo Costruzioni Edili e Restauri di Conti Randolfo & C. S.n.c."
    assert SmartCap.smart_cap(u"D'ALOISIO AVV. CLAUDIA STUDIO LEGALE")                                          == u"D'Aloisio Avv. Claudia Studio Legale"
    assert SmartCap.smart_cap(u"D.A.I. S.R.L.")                                                                 == u"D.A.I. S.r.l."
    assert SmartCap.smart_cap(u"SOCIETÀ XX SETTEMBRE")                                                          == u"Società XX Settembre"
    assert SmartCap.smart_cap(u"EDIL DBN S.A.S. DI DI BENEDETTO NICOLA E C.")                                   == u"Edil Dbn S.a.s. di di Benedetto Nicola e C."
    assert SmartCap.smart_cap(u"EFFELLE SISTEMI S.R.L.")                                                        == u"Effelle Sistemi S.r.l."
    assert SmartCap.smart_cap(u"ESPANA S.A.S. DI MONTELLA MARIANO & C.")                                        == u"Espana S.a.s. di Montella Mariano & C."
    assert SmartCap.smart_cap(u"F.A.M.I.P.")                                                                    == u"F.A.M.I.P."
    assert SmartCap.smart_cap(u"FIORDIROCCIA S.A.S. DI SCALET MARINO & C.")                                     == u"Fiordiroccia S.a.s. di Scalet Marino & C."
    assert SmartCap.smart_cap(u"FIORIN F.LLI")                                                                  == u"Fiorin F.lli"
    assert SmartCap.smart_cap(u"FREE SLIM DI TIBET S.A.S.")                                                     == u"Free Slim di Tibet S.a.s."
    assert SmartCap.smart_cap(u"G.M.G. S.A.S. DI COPPOLA GIULIO E C.")                                          == u"G.M.G. S.a.s. di Coppola Giulio e C."
    assert SmartCap.smart_cap(u"GARNÌ STELLA ALPINA")                                                           == u"Garnì Stella Alpina"
    assert SmartCap.smart_cap(u"GE.MI.SO. DI LOPES GIUSEPPE MARCELLO")                                          == u"Ge.Mi.So. di Lopes Giuseppe Marcello"
    assert SmartCap.smart_cap(u"GUARESCHI DR. SANDRA")                                                          == u"Guareschi Dr. Sandra"
    assert SmartCap.smart_cap(u"HOTEL CAVALLINO - S' RÃSSL")                                                == u"Hotel Cavallino - S' RãSsl"
    assert SmartCap.smart_cap(u"HOTEL LA GINESTRA S.R.L.")                                                      == u"Hotel La Ginestra S.r.l."
    assert SmartCap.smart_cap(u"I.B.S. SRL")                                                                    == u"I.B.S. Srl"
    assert SmartCap.smart_cap(u"I.T.I.D. DI PARENTI O. E PERI R. E C. SAS")                                     == u"I.T.I.D. di Parenti O. e Peri R. e C. Sas"
    assert SmartCap.smart_cap(u"IMPIANTI ZERBO DI ZERBO ANDREA A.")                                             == u"Impianti Zerbo di Zerbo Andrea A."
    assert SmartCap.smart_cap(u"IMPRESA C.F. GENTA 1848 S.R.L.")                                                == u"Impresa C.F. Genta 1848 S.r.l."
    assert SmartCap.smart_cap(u"IMPRESA FORESTI - costruzioni edili dal 1972")                                  == u"Impresa Foresti - Costruzioni Edili dal 1972"
    assert SmartCap.smart_cap(u"ING. CAIONE COSTRUZIONI S.R.L.")                                                == u"Ing. Caione Costruzioni S.r.l."
    assert SmartCap.smart_cap(u"INVIDIA CAFE' DI ROVERSI GIANLUCA & C. SAS")                                    == u"Invidia Cafe' di Roversi Gianluca & C. Sas"
    assert SmartCap.smart_cap(u"IPPOLITO A.S.STUDIO ODONTOIATRICO ASSOCIATO")                                   == u"Ippolito A.S.Studio Odontoiatrico Associato"
    assert SmartCap.smart_cap(u"ISTITUTO DI BELLEZZA' DONATELLA'")                                              == u"Istituto di Bellezza' Donatella'"
    assert SmartCap.smart_cap(u"LA MAISON DE LA BEAUTE' S.A.S. DI FIORITO CONCETTA")                            == u"La Maison De La Beaute' S.a.s. di Fiorito Concetta"
    assert SmartCap.smart_cap(u"LA MARIC S.A.S. DI RICCIO GAETANO")                                             == u"La Maric S.a.s. di Riccio Gaetano"
    assert SmartCap.smart_cap(u"LA PIOLA D'LE 2 SURELE")                                                        == u"La Piola D'Le 2 Surele"
    assert SmartCap.smart_cap(u"LATTERIA#21")                                                                   == u"Latteria#21"
    assert SmartCap.smart_cap(u"LE NINFEE ESTETICA & BENESSERE")                                                == u"Le Ninfee Estetica & Benessere"
    assert SmartCap.smart_cap(u"LERARIO AVV. NICOLA")                                                           == u"Lerario Avv. Nicola"
    assert SmartCap.smart_cap(u"LISA AVV. SANTI")                                                               == u"Lisa Avv. Santi"
    assert SmartCap.smart_cap(u"LUALDI S.P.A.")                                                                 == u"Lualdi S.p.a."
    assert SmartCap.smart_cap(u"M.S. CREM DI SABRINA MANFRONI")                                                 == u"M.S. Crem di Sabrina Manfroni"
    assert SmartCap.smart_cap(u"MARA MEO S.R.L.")                                                               == u"Mara Meo S.r.l."
    assert SmartCap.smart_cap(u"MARGAGLIOTTI PORTE & FINESTRE")                                                 == u"Margagliotti Porte & Finestre"
    assert SmartCap.smart_cap(u"MASE' EZIO")                                                                    == u"Mase' Ezio"
    assert SmartCap.smart_cap(u"MILK S.A.S. DI LUCIFORA SALVATORE & C.")                                        == u"Milk S.a.s. di Lucifora Salvatore & C."
    assert SmartCap.smart_cap(u"MILLENNIUM SNC DI RICCIARDI FABIO ROCCO & C.")                                  == u"Millennium Snc di Ricciardi Fabio Rocco & C."
    assert SmartCap.smart_cap(u"ML IMPIANTI S.R.L.")                                                            == u"ML Impianti S.r.l."
    assert SmartCap.smart_cap(u"NEW BODY ESTETICA & BENESSERE")                                                 == u"New Body Estetica & Benessere"
    assert SmartCap.smart_cap(u"NSQ SOCIETA' COOPERATIVA")                                                      == u"Nsq Societa' Cooperativa"
    assert SmartCap.smart_cap(u"NUOVA CARROZZERIA F.LLI MASCHIO DI MASCHIO MASSIMO & C. SNC")                   == u"Nuova Carrozzeria F.lli Maschio di Maschio Massimo & C. Snc"
    assert SmartCap.smart_cap(u"NUOVA PROGRESS S.R.L.")                                                         == u"Nuova Progress S.r.l."
    assert SmartCap.smart_cap(u"O.VAL SRL")                                                                     == u"O.Val Srl"
    assert SmartCap.smart_cap(u"OLIMPIA FOOD S.R.L.")                                                           == u"Olimpia Food S.r.l."
    assert SmartCap.smart_cap(u"ONORANZE FUNEBRI MAIOLINI ALBINO DIR. TEC. PIERINO BETELLI")                    == u"Onoranze Funebri Maiolini Albino Dir. Tec. Pierino Betelli"
    assert SmartCap.smart_cap(u"ONORANZE FUNEBRI S. BARBARA")                                                   == u"Onoranze Funebri S. Barbara"
    assert SmartCap.smart_cap(u"PEREGO AVV. DANIELA")                                                           == u"Perego Avv. Daniela"
    assert SmartCap.smart_cap(u"PERIANO S.C.R.L.")                                                              == u"Periano S.c.r.l."
    assert SmartCap.smart_cap(u"PIZZA PARTY SNC DI MONTANA MICHELE & VILLARASPI")                               == u"Pizza Party Snc di Montana Michele & Villaraspi"
    assert SmartCap.smart_cap(u"PIZZERIA-FRIGGITORIA \"MADE IN SALVO\"")                                        == u"Pizzeria-Friggitoria \"Made in Salvo\""
    assert SmartCap.smart_cap(u"POLITERMICA INDUSTRIALE S.P.A")                                                 == u"Politermica Industriale S.p.a"
    assert SmartCap.smart_cap(u"POLIZIANI DR. GIOVANNI")                                                        == u"Poliziani Dr. Giovanni"
    assert SmartCap.smart_cap(u"PRESTIGE S.R.L.")                                                               == u"Prestige S.r.l."
    assert SmartCap.smart_cap(u"PROFUMERIA ACADEMIE BEAUTE - CENTRO ESTETICO")                                  == u"Profumeria Academie Beaute - Centro Estetico"
    assert SmartCap.smart_cap(u"RISTORANTE LA TARTANA DA MARIO L'OSTRICARO sas")                                == u"Ristorante La Tartana da Mario L'Ostricaro Sas"
    assert SmartCap.smart_cap(u"RIZZO AVV. GABRIELE")                                                           == u"Rizzo Avv. Gabriele"
    assert SmartCap.smart_cap(u"S.C.I. SOCIETA' COSTRUZIONI INDUSTRIALI SRL")                                   == u"S.C.I. Societa' Costruzioni Industriali Srl"
    assert SmartCap.smart_cap(u"SANDONA' GOMME - CENTRO PNEUMATICI")                                            == u"Sandona' Gomme - Centro Pneumatici"
    assert SmartCap.smart_cap(u"SAVIO TECNOIMPIANTI - IMPIANTI TERMOIDRAULICI")                                 == u"Savio Tecnoimpianti - Impianti Termoidraulici"
    assert SmartCap.smart_cap(u"SERRAMENTI ARREDAMENTI G.F.")                                                   == u"Serramenti Arredamenti G.F."
    assert SmartCap.smart_cap(u"SETTIMO DENTAL SNC DI TROTTA PASQUALE E C.")                                    == u"Settimo Dental Snc di Trotta Pasquale e C."
    assert SmartCap.smart_cap(u"SEVEN ZEE DI ZONTA LUIGI & C. SNC")                                             == u"Seven Zee di Zonta Luigi & C. Snc"
    assert SmartCap.smart_cap(u"SOCIETA' ACCARDO MARINI SRL")                                                   == u"Societa' Accardo Marini Srl"
    assert SmartCap.smart_cap(u"SOCIETA' PACIFIC DI FORST ROSEMARIE SIGRID E C. SNC")                           == u"Societa' Pacific di Forst Rosemarie Sigrid e C. Snc"
    assert SmartCap.smart_cap(u"SOPPELSA TERMOIDRAULICA S.N.C. DI SOPPELSA FULVIO & F.LLI")                     == u"Soppelsa Termoidraulica S.n.c. di Soppelsa Fulvio & F.lli"
    assert SmartCap.smart_cap(u"SPINETTO DR ROBERTO E DR.SSA GIULIA STUDIO DENTISTICO ASSOCIATO")               == u"Spinetto Dr Roberto e Dr.ssa Giulia Studio Dentistico Associato"
    assert SmartCap.smart_cap(u"STN CONSULTING S.A.S. DI GIANLUCA NUNNARI E C. SERVIZI DI INGEGNERIA")          == u"Stn Consulting S.a.s. di Gianluca Nunnari e C. Servizi di Ingegneria"
    assert SmartCap.smart_cap(u"STRATO S.R.L.")                                                                 == u"Strato S.r.l."
    assert SmartCap.smart_cap(u"STUDIO DENTISTICO ASS.TO DR. F. BEVILACQUA, G. PIANCA, V. PIANCA")              == u"Studio Dentistico Ass.to Dr. F. Bevilacqua, G. Pianca, V. Pianca"
    assert SmartCap.smart_cap(u"STUDIO DENTISTICO IACONO DOTT.SSA LIVIA")                                       == u"Studio Dentistico Iacono Dott.ssa Livia"
    assert SmartCap.smart_cap(u"STUDIO DENTISTICO MARESCHI DR. PAOLO E BASSUTTI DR. FABIO")                     == u"Studio Dentistico Mareschi Dr. Paolo e Bassutti Dr. Fabio"
    assert SmartCap.smart_cap(u"STYLCAR CARROZZERIA S.N.C. DI SANDRI GRAZIANO")                                 == u"Stylcar Carrozzeria S.n.c. di Sandri Graziano"
    assert SmartCap.smart_cap(u"T.S.TERMOIDRAULICA")                                                            == u"T.S.Termoidraulica"
    assert SmartCap.smart_cap(u"TECNOIMPIANTI PERSALI S.R.L.")                                                  == u"Tecnoimpianti Persali S.r.l."
    assert SmartCap.smart_cap(u"TECNOVERDE DEL DOTT. FRANCESCO VATTERONI AGRONOMO PAESAGGISTA")                 == u"Tecnoverde del Dott. Francesco Vatteroni Agronomo Paesaggista"
    assert SmartCap.smart_cap(u"TERMOIDRAULICA DUE ZETA SNC - DI ZOBBI E. & ZANNONI R.")                        == u"Termoidraulica Due Zeta Snc - di Zobbi E. & Zannoni R."
    assert SmartCap.smart_cap(u"TRATTORIA SAN PIETRO SNC DI TOSATTO GIOVANNI & C.")                             == u"Trattoria San Pietro Snc di Tosatto Giovanni & C."
    assert SmartCap.smart_cap(u"VERDE AMBIENTE PICC. SOC. COOP. A R.L.")                                        == u"Verde Ambiente Picc. Soc. Coop. a R.L."
    assert SmartCap.smart_cap(u"VERDE VAN PIK S.N.C. DI CHINELLATO MICHELE E MIGOTTO MAURIZIO")                 == u"Verde Van Pik S.n.c. di Chinellato Michele e Migotto Maurizio"
    assert SmartCap.smart_cap(u"VIRGINIA CINQUE STELLE S.R.L.")                                                 == u"Virginia Cinque Stelle S.r.l."
    assert SmartCap.smart_cap(u"DI FARIELLO PASQUALE")                                                          == u"Di Fariello Pasquale"
    assert SmartCap.smart_cap(u"SPECIALISTA IN OSTETRICIA, GINECOLOGIA ED ENDOCRINOLOGIA")                      == u"Specialista in Ostetricia, Ginecologia ed Endocrinologia"
    assert SmartCap.smart_cap(u"SARTORIS D.SSA LAURA")                                                          == u"Sartoris D.ssa Laura"
    assert SmartCap.smart_cap(u"REBOLINI GIORGIO_ASSISTENZA RIELLO")                                            == u"Rebolini Giorgio_Assistenza Riello"
    assert SmartCap.smart_cap(u"GRAZIOLI CLIMASERVICE S.R.L._AGENZIA E ASSISTENZA RIELLO")                      == u"Grazioli Climaservice S.r.l._Agenzia e Assistenza Riello"
