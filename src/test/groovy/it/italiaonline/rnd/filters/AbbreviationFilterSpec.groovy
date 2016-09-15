package it.italiaonline.rnd.filters

import spock.lang.Specification

class AbbreviationFilterSpec extends Specification {

  def "Should make abbreviation first letter uppercase and then lowercase"() {

    expect:
      output == new AbbreviationFilter(
                  new TextFilter.NoNullFilter(input)
                ).result()

    where:
      input                       | output
      "F.LLI SASSO"               | "F.lli SASSO"
      "FR.LLI SASSO"              | "FR.LLI SASSO"
      "DOTT.SSA CRISTINA D'AVENA" | "Dott.ssa CRISTINA D'AVENA"
      "D.SSA MARIA PIA"           | "D.ssa MARIA PIA"
      "DOT.SSA NINA"              | "DOT.SSA NINA"

  }

}
