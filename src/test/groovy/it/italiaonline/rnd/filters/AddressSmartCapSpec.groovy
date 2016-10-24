package it.italiaonline.rnd.filters

import spock.lang.Specification

class AddressSmartCapSpec extends Specification {

	/**
	 * Behavioral test made against a list provided by Italia On Line.
	 * 100 real cases mixed between 'customers' and 'inseriti'
	 */
	def "All filters together should correctly match these tests"() {
		expect:
			filtered == new TextFilter.AddressSmartCap(
			              businessName
			            ).result()

		where:
			businessName                                                  | filtered
			"ARLETTI,DR. FLAVIO"                                          | "Arletti, Dr. Flavio"
			"ATRES,S.R.L."                                                | "Atres, S.r.l."
			",AUTOFFICINA L.R. MOTORSPORT,"                               | ", Autofficina L.R. Motorsport,"
			"SPECIALISTA IN OSTETRICIA,GINECOLOGIA ED ENDOCRINOLOGIA"     | "Specialista in Ostetricia, Ginecologia ed Endocrinologia"
			"VIA BOITO ARRIGO,41"                                         | "Via Boito Arrigo, 41"
			"NUOVA CARROZZERIA,F.LLI MASCHIO DI MASCHIO MASSIMO & C. SNC" | "Nuova Carrozzeria, F.lli Maschio di Maschio Massimo & C. Snc"
			"SANTHIA'"                                                    | "Santhià"
	}
}
