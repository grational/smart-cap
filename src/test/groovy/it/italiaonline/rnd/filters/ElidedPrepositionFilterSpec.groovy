package it.italiaonline.rnd.filters

import spock.lang.Specification

class ElidedPrepositionFilterSpec extends Specification {

  def "Should make prepositions in lowercase"() {

    expect:
      output == new ElidedPrepositionFilter(
                  new TextFilter.NoNullFilter(input)
                ).result()

    where:
      input                         | output
      "PER POCO SULL'ACQUA"         | "PER POCO sull'ACQUA"
      "ANCHE NELL'ANCORA BUIO VELO" | "ANCHE nell'ANCORA BUIO VELO"
      "DELLA SERA DELL'EST"         | "DELLA SERA dell'EST"
      "DAL BASSO E DALL'ALTO"       | "DAL BASSO E dall'ALTO"
      "ARRIVAVANO ALL'ALTIPIANO"    | "ARRIVAVANO all'ALTIPIANO"
      "ROMANO D'EZZELLINO"          | "ROMANO D'EZZELLINO"

  }
  //sull
  //nell
  //dell
  //dall
  //all
}
