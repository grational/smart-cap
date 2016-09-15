package it.italiaonline.rnd.filters

import spock.lang.Specification

class SimpleConjunctionFilterSpec extends Specification {

	def "Should make conjunctions all lowercase"() {

		expect:
			output == new SimpleConjunctionFilter(
			            new TextFilter.NoNullFilter(input)
			          ).result()

		where:
			input                         | output
			'HANSEL E GRETEL'             | 'HANSEL e GRETEL'
			'O MANGIAMO O ANDIAMO A CASA' | 'O MANGIAMO o ANDIAMO A CASA'
	}

}
