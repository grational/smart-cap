package it.italiaonline.rnd.filters

import spock.lang.Specification

class ProvinceAbbreviationFilterSpec extends Specification {

	def "Should make province abbreviation in uppercase"() {

    expect:
			output == new ProvinceAbbreviationFilter(
			            new TextFilter.NoNullFilter(input)
			          ).result()

    where:
      input                            | output
			"Città del Vaticano (cv)"        | "Città del Vaticano (CV)"
			"Acciano (Aq)"                   | "Acciano (AQ)"
			"Altino (Ch)"                    | "Altino (CH)"
			"Corvara (Pe)"                   | "Corvara (PE)"
			"Aliano (Mt)"                    | "Aliano (MT)"
			"Rionero in Vulture (Pz)"        | "Rionero in Vulture (PZ)"
			"Laino Borgo (Cs)"               | "Laino Borgo (CS)"
			"Santo Stefano di Rogliano (Cs)" | "Santo Stefano di Rogliano (CS)"

	}
}
