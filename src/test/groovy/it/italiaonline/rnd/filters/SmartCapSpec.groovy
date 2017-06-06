package it.italiaonline.rnd.filters
/*
 *                       _oo0oo_
 *                      o8888888o
 *                      88" . "88
 *                      (| -_- |)
 *                      0\  =  /0
 *                    ___/`---'\___
 *                  .' \\|     |// '.
 *                 / \\|||  :  |||// \
 *                / _||||| -:- |||||- \
 *               |   | \\\  -  /// |   |
 *               | \_|  ''\---/''  |_/ |
 *               \  .-\__  '-'  ___/-. /
 *             ___'. .'  /--.--\  `. .'___
 *          ."" '<  `.___\_<|>_/___.' >' "".
 *         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *         \  \ `_.   \_ __\ /__ _/   .-` /  /
 *     =====`-.____`.___ \_____/___.-`___.-'=====
 *                       `=---='
 *
 * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 *   Buddha bless this code to make it (almost) bug-free
 */
import spock.lang.Specification

class SmartCapSpec extends Specification {

	/**
	 * The test should throw an exception if a null argument is provided
	 */
	def "should throw exception when the required String is null"()
	throws IllegalArgumentException {
		when:
			//new TextFilter.NoNullFilter(null).result()
			new TextFilter.SmartCap().result()

		then:
			final IllegalArgumentException exception = thrown()
			// Alternate syntax: def exception = thrown(ArticleNotFoundException)
			exception.message == "Input is NULL: can't go ahead."
	}

	/**
	 * Behavioral test made against a list provided by Italia On Line.
	 * 100 real cases mixed between 'customers' and 'inseriti'
	 */
	def "All filters together should correctly match these tests"() {
		expect:
			filtered == new TextFilter.SmartCap(
			              businessName
			            ).result()

		where:
			businessName                                                                    | filtered
			"ARLETTI DR. FLAVIO"                                                            | "Arletti Dr. Flavio"
			"ATRES S.R.L."                                                                  | "Atres S.r.l."
			"AUTOFFICINA L.R. MOTORSPORT"                                                   | "Autofficina L.R. Motorsport"
			"AUTOSTYLE S.N.C."                                                              | "Autostyle S.n.c."
			"AVV. CRISTINA SCOTTI"                                                          | "Avv. Cristina Scotti"
			"AZALEA S.A.S. DI AZZALE FRANCO E PIETRO & C."                                  | "Azalea S.a.s. di Azzale Franco e Pietro & C."
			"BAR SPORT S.A.S. DI WANG WEIQIN E C."                                          | "Bar Sport S.a.s. di Wang Weiqin e C."
			"BAR SPRINT S.N.C. DI MOCCIA CLAUDIO"                                           | "Bar Sprint S.n.c. di Moccia Claudio"
			"BASE S.P.A."                                                                   | "Base S.p.a."
			"BERARDI AVV. FILIPPO MARIA"                                                    | "Berardi Avv. Filippo Maria"
			"BRUGNATO HEAT & DRINK SNC"                                                     | "Brugnato Heat & Drink Snc"
			"CAFFE' PAGLIA DI BANI EGLANTINA"                                               | "Caffe' Paglia di Bani Eglantina"
			"CANNAVO' GAETANO SRL"                                                          | "Cannavo' Gaetano Srl"
			"CANNAVO' GAETANO S.R.L."                                                       | "Cannavo' Gaetano S.r.l."
			"CARAIBI 2 S.N.C DI MICHELA FALCO & C."                                         | "Caraibi 2 S.n.c di Michela Falco & C."
			"CENTRO ESTETICO GOCCE D'AMBRA"                                                 | "Centro Estetico Gocce D'Ambra"
			"CHIRIATTI EDILIZIA S.A.S. DI CHIRIATTI FLAVIO & C."                            | "Chiriatti Edilizia S.a.s. di Chiriatti Flavio & C."
			"CONTI CAV. COLOMBO COSTRUZIONI EDILI E RESTAURI DI CONTI RANDOLFO & C. S.N.C." | "Conti Cav. Colombo Costruzioni Edili e Restauri di Conti Randolfo & C. S.n.c."
			"D'ALOISIO AVV. CLAUDIA STUDIO LEGALE"                                          | "D'Aloisio Avv. Claudia Studio Legale"
			"D.A.I. S.R.L."                                                                 | "D.A.I. S.r.l."
			"SOCIETÀ XX SETTEMBRE"                                                          | "Società XX Settembre"
			"EDIL DBN S.A.S. DI DI BENEDETTO NICOLA E C."                                   | "Edil Dbn S.a.s. di di Benedetto Nicola e C."
			"EFFELLE SISTEMI S.R.L."                                                        | "Effelle Sistemi S.r.l."
			"ESPANA S.A.S. DI MONTELLA MARIANO & C."                                        | "Espana S.a.s. di Montella Mariano & C."
			"F.A.M.I.P."                                                                    | "F.A.M.I.P."
			"FIORDIROCCIA S.A.S. DI SCALET MARINO & C."                                     | "Fiordiroccia S.a.s. di Scalet Marino & C."
			"FIORIN F.LLI"                                                                  | "Fiorin F.lli"
			"FREE SLIM DI TIBET S.A.S."                                                     | "Free Slim di Tibet S.a.s."
			"G.M.G. S.A.S. DI COPPOLA GIULIO E C."                                          | "G.M.G. S.a.s. di Coppola Giulio e C."
			"GARNÌ STELLA ALPINA"                                                           | "Garnì Stella Alpina"
			"GE.MI.SO. DI LOPES GIUSEPPE MARCELLO"                                          | "Ge.Mi.So. di Lopes Giuseppe Marcello"
			"GUARESCHI DR. SANDRA"                                                          | "Guareschi Dr. Sandra"
			"HOTEL CAVALLINO - S' RÃSSL"                                                | "Hotel Cavallino - S' RãSsl"
			"HOTEL LA GINESTRA S.R.L."                                                      | "Hotel La Ginestra S.r.l."
			"I.B.S. SRL"                                                                    | "I.B.S. Srl"
			"I.T.I.D. DI PARENTI O. E PERI R. E C. SAS"                                     | "I.T.I.D. di Parenti O. e Peri R. e C. Sas"
			"IMPIANTI ZERBO DI ZERBO ANDREA A."                                             | "Impianti Zerbo di Zerbo Andrea A."
			"IMPRESA C.F. GENTA 1848 S.R.L."                                                | "Impresa C.F. Genta 1848 S.r.l."
			"IMPRESA FORESTI - costruzioni edili dal 1972"                                  | "Impresa Foresti - Costruzioni Edili dal 1972"
			"ING. CAIONE COSTRUZIONI S.R.L."                                                | "Ing. Caione Costruzioni S.r.l."
			"INVIDIA CAFE' DI ROVERSI GIANLUCA & C. SAS"                                    | "Invidia Cafe' di Roversi Gianluca & C. Sas"
			"IPPOLITO A.S.STUDIO ODONTOIATRICO ASSOCIATO"                                   | "Ippolito A.S.Studio Odontoiatrico Associato"
			"ISTITUTO DI BELLEZZA' DONATELLA'"                                              | "Istituto di Bellezza' Donatella'"
			"LA MAISON DE LA BEAUTE' S.A.S. DI FIORITO CONCETTA"                            | "La Maison De La Beaute' S.a.s. di Fiorito Concetta"
			"LA MARIC S.A.S. DI RICCIO GAETANO"                                             | "La Maric S.a.s. di Riccio Gaetano"
			"LA PIOLA D'LE 2 SURELE"                                                        | "La Piola D'Le 2 Surele"
			"LATTERIA#21"                                                                   | "Latteria#21"
			"LE NINFEE ESTETICA & BENESSERE"                                                | "Le Ninfee Estetica & Benessere"
			"LERARIO AVV. NICOLA"                                                           | "Lerario Avv. Nicola"
			"LISA AVV. SANTI"                                                               | "Lisa Avv. Santi"
			"LUALDI S.P.A."                                                                 | "Lualdi S.p.a."
			"M.S. CREM DI SABRINA MANFRONI"                                                 | "M.S. Crem di Sabrina Manfroni"
			"MARA MEO S.R.L."                                                               | "Mara Meo S.r.l."
			"MARGAGLIOTTI PORTE & FINESTRE"                                                 | "Margagliotti Porte & Finestre"
			"MASE' EZIO"                                                                    | "Mase' Ezio"
			"MILK S.A.S. DI LUCIFORA SALVATORE & C."                                        | "Milk S.a.s. di Lucifora Salvatore & C."
			"MILLENNIUM SNC DI RICCIARDI FABIO ROCCO & C."                                  | "Millennium Snc di Ricciardi Fabio Rocco & C."
			"ML IMPIANTI S.R.L."                                                            | "ML Impianti S.r.l."
			"NEW BODY ESTETICA & BENESSERE"                                                 | "New Body Estetica & Benessere"
			"NSQ SOCIETA' COOPERATIVA"                                                      | "Nsq Societa' Cooperativa"
			"NUOVA CARROZZERIA F.LLI MASCHIO DI MASCHIO MASSIMO & C. SNC"                   | "Nuova Carrozzeria F.lli Maschio di Maschio Massimo & C. Snc"
			"NUOVA PROGRESS S.R.L."                                                         | "Nuova Progress S.r.l."
			"O.VAL SRL"                                                                     | "O.Val Srl"
			"OLIMPIA FOOD S.R.L."                                                           | "Olimpia Food S.r.l."
			"ONORANZE FUNEBRI MAIOLINI ALBINO DIR. TEC. PIERINO BETELLI"                    | "Onoranze Funebri Maiolini Albino Dir. Tec. Pierino Betelli"
			"ONORANZE FUNEBRI S. BARBARA"                                                   | "Onoranze Funebri S. Barbara"
			"PEREGO AVV. DANIELA"                                                           | "Perego Avv. Daniela"
			"PERIANO S.C.R.L."                                                              | "Periano S.c.r.l."
			"PIZZA PARTY SNC DI MONTANA MICHELE & VILLARASPI"                               | "Pizza Party Snc di Montana Michele & Villaraspi"
			"PIZZERIA-FRIGGITORIA \"MADE IN SALVO\""                                        | "Pizzeria-Friggitoria \"Made in Salvo\""
			"POLITERMICA INDUSTRIALE S.P.A"                                                 | "Politermica Industriale S.p.a"
			"POLIZIANI DR. GIOVANNI"                                                        | "Poliziani Dr. Giovanni"
			"PRESTIGE S.R.L."                                                               | "Prestige S.r.l."
			"PROFUMERIA ACADEMIE BEAUTE - CENTRO ESTETICO"                                  | "Profumeria Academie Beaute - Centro Estetico"
			"RISTORANTE LA TARTANA DA MARIO L'OSTRICARO sas"                                | "Ristorante La Tartana da Mario L'Ostricaro Sas"
			"RIZZO AVV. GABRIELE"                                                           | "Rizzo Avv. Gabriele"
			"S.C.I. SOCIETA' COSTRUZIONI INDUSTRIALI SRL"                                   | "S.C.I. Societa' Costruzioni Industriali Srl"
			"SANDONA' GOMME - CENTRO PNEUMATICI"                                            | "Sandona' Gomme - Centro Pneumatici"
			"SAVIO TECNOIMPIANTI - IMPIANTI TERMOIDRAULICI"                                 | "Savio Tecnoimpianti - Impianti Termoidraulici"
			"SERRAMENTI ARREDAMENTI G.F."                                                   | "Serramenti Arredamenti G.F."
			"SETTIMO DENTAL SNC DI TROTTA PASQUALE E C."                                    | "Settimo Dental Snc di Trotta Pasquale e C."
			"SEVEN ZEE DI ZONTA LUIGI & C. SNC"                                             | "Seven Zee di Zonta Luigi & C. Snc"
			"SOCIETA' ACCARDO MARINI SRL"                                                   | "Societa' Accardo Marini Srl"
			"SOCIETA' PACIFIC DI FORST ROSEMARIE SIGRID E C. SNC"                           | "Societa' Pacific di Forst Rosemarie Sigrid e C. Snc"
			"SOPPELSA TERMOIDRAULICA S.N.C. DI SOPPELSA FULVIO & F.LLI"                     | "Soppelsa Termoidraulica S.n.c. di Soppelsa Fulvio & F.lli"
			"SPINETTO DR ROBERTO E DR.SSA GIULIA STUDIO DENTISTICO ASSOCIATO"               | "Spinetto Dr Roberto e Dr.ssa Giulia Studio Dentistico Associato"
			"STN CONSULTING S.A.S. DI GIANLUCA NUNNARI E C. SERVIZI DI INGEGNERIA"          | "Stn Consulting S.a.s. di Gianluca Nunnari e C. Servizi di Ingegneria"
			"STRATO S.R.L."                                                                 | "Strato S.r.l."
			"STUDIO DENTISTICO ASS.TO DR. F. BEVILACQUA, G. PIANCA, V. PIANCA"              | "Studio Dentistico Ass.to Dr. F. Bevilacqua, G. Pianca, V. Pianca"
			"STUDIO DENTISTICO IACONO DOTT.SSA LIVIA"                                       | "Studio Dentistico Iacono Dott.ssa Livia"
			"STUDIO DENTISTICO MARESCHI DR. PAOLO E BASSUTTI DR. FABIO"                     | "Studio Dentistico Mareschi Dr. Paolo e Bassutti Dr. Fabio"
			"STYLCAR CARROZZERIA S.N.C. DI SANDRI GRAZIANO"                                 | "Stylcar Carrozzeria S.n.c. di Sandri Graziano"
			"T.S.TERMOIDRAULICA"                                                            | "T.S.Termoidraulica"
			"TECNOIMPIANTI PERSALI S.R.L."                                                  | "Tecnoimpianti Persali S.r.l."
			"TECNOVERDE DEL DOTT. FRANCESCO VATTERONI AGRONOMO PAESAGGISTA"                 | "Tecnoverde del Dott. Francesco Vatteroni Agronomo Paesaggista"
			"TERMOIDRAULICA DUE ZETA SNC - DI ZOBBI E. & ZANNONI R."                        | "Termoidraulica Due Zeta Snc - di Zobbi E. & Zannoni R."
			"TRATTORIA SAN PIETRO SNC DI TOSATTO GIOVANNI & C."                             | "Trattoria San Pietro Snc di Tosatto Giovanni & C."
			"VERDE AMBIENTE PICC. SOC. COOP. A R.L."                                        | "Verde Ambiente Picc. Soc. Coop. a R.L."
			"VERDE VAN PIK S.N.C. DI CHINELLATO MICHELE E MIGOTTO MAURIZIO"                 | "Verde Van Pik S.n.c. di Chinellato Michele e Migotto Maurizio"
			"VIRGINIA CINQUE STELLE S.R.L."                                                 | "Virginia Cinque Stelle S.r.l."
			"DI FARIELLO PASQUALE"                                                          | "Di Fariello Pasquale"
			"SPECIALISTA IN OSTETRICIA, GINECOLOGIA ED ENDOCRINOLOGIA"                      | "Specialista in Ostetricia, Ginecologia ed Endocrinologia"
			"SARTORIS D.SSA LAURA"                                                          | "Sartoris D.ssa Laura"
			"REBOLINI GIORGIO_ASSISTENZA RIELLO"                                            | "Rebolini Giorgio_Assistenza Riello"
			"GRAZIOLI CLIMASERVICE S.R.L._AGENZIA E ASSISTENZA RIELLO"                      | "Grazioli Climaservice S.r.l._Agenzia e Assistenza Riello"
			"ROMANO D'EZZELLINO"                                                            | "Romano D'Ezzellino"

	}
}
