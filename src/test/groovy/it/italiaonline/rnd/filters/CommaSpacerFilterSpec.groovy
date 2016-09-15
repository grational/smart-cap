package it.italiaonline.rnd.filters

import spock.lang.Specification

class CommaSpacerFilterSpec extends Specification {

	def "Should add a single space after each comma"() {

		expect:
			output == new CommaSpacerFilter(
			            new TextFilter.NoNullFilter(input)
			          ).result()

		where:
			input                                 | output
			'virgola,senza spazio'                | 'virgola, senza spazio'
			'virgola alla fine,'                  | 'virgola alla fine,'
			',virgola iniziale e finale,'         | ', virgola iniziale e finale,'
			'virgola con tab,	e senza,dopo'       | 'virgola con tab,	e senza, dopo'
			'  ,   virgola con tab,	e senza,dopo' | '  ,   virgola con tab,	e senza, dopo'
	}
}
