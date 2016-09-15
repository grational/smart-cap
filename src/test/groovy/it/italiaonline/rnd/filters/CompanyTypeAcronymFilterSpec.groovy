package it.italiaonline.rnd.filters

import spock.lang.Specification

class CompanyTypeAcronymFilterSpec extends Specification {

  def "Should make company's type acronym first letter uppercase and then lowercase"() {

    expect:
      output == new CompanyTypeAcronymFilter(
                  new TextFilter.NoNullFilter(input)
                ).result()

    where:
      input                  | output
      "SoCiEtÀ s.p.a.-RICCA" | "SoCiEtÀ S.p.a.-RICCA"
      "SoCiEtÀ s.p.a-RICCA"  | "SoCiEtÀ S.p.a-RICCA"
      "SoCiEtÀ s.r.l."       | "SoCiEtÀ S.r.l."
      "SoCiEtÀ s.r.l.s."     | "SoCiEtÀ S.r.l.s."
      "SoCiEtÀ S.N.C."       | "SoCiEtÀ S.n.c."
      "SoCiEtÀ S.c.A.r.L."   | "SoCiEtÀ S.c.a.r.l."
      "SoCiEtÀ s.C.r.L."     | "SoCiEtÀ S.c.r.l."
      "SoCiEtÀ s.A.s"        | "SoCiEtÀ S.a.s"
      "SoCiEtÀ S.A.A."       | "SoCiEtÀ S.a.a."
      "SoCiEtÀ S.A.p.A."     | "SoCiEtÀ S.a.p.a."
      "SoCiEtÀ S.R.l.A."     | "SoCiEtÀ S.R.l.A."   //fake
      "SoCiEtÀ S.P.C."       | "SoCiEtÀ S.P.C."     //fake
      "SoCiEtÀ S.P.A.S."     | "SoCiEtÀ S.P.A.S."   //fake

  }
  //S.p.a.       V
  //S.r.l.       V
  //S.r.l.s.     V
  //S.n.c.       V
  //S.c.a.r.l.   V
  //S.c.r.l.     V
  //S.a.p.a.     V
  //S.a.s.       V
  //S.a.a.       V
}
