package it.italiaonline.rnd.filters

import spock.lang.Specification

class TownApostrophe2AccentFilterSpec extends Specification {

	def "Should switch towns' terminal vowel plus apostrophe into accented vowel"() {

		expect:
			output == new TownApostrophe2AccentFilter(
			            new TextFilter.NoNullFilter(input)
			          ).result()

		where:
			input      | output
			"santhia'" | 'Santhià'
			"cuorgne'" | 'Cuorgnè'
			"forli'"   | 'Forlì'
			"vigano'"  | 'Viganò'
			"cefalu'"  | 'Cefalù'
	}
}
