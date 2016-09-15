package it.italiaonline.rnd.filters

import spock.lang.Specification

class CutPrepositionFilterSpec extends Specification {

  def "Should make prepositions in lowercase"() {

    expect:
      output == new CutPrepositionFilter(
                  new TextFilter.NoNullFilter(input)
                ).result()

    where:
      input                         | output
      "PER POCO SULL'ACQUA"         | "PER POCO sull'ACQUA"
      "ANCHE NELL'ANCORA BUIO VELO" | "ANCHE nell'ANCORA BUIO VELO"
      "DELLA SERA DELL'EST"         | "DELLA SERA dell'EST"
      "DAL BASSO E DALL'ALTO"       | "DAL BASSO E dall'ALTO"
      "ARRIVAVANO ALL'ALTIPIANO"    | "ARRIVAVANO all'ALTIPIANO"

  }
  //sull
  //nell
  //dell
  //dall
  //all
}
