package it.italiaonline.rnd.filters

import spock.lang.Specification

class NoNullFilterSpec extends Specification {

  def "should throw exception when the required String is null"()
  throws IllegalArgumentException {
    when:
      //new TextFilter.NoNullFilter(null).result()
      new TextFilter.NoNullFilter().result()

    then:
      final IllegalArgumentException exception = thrown()
      // Alternate syntax: def exception = thrown(ArticleNotFoundException)
      exception.message == "Input is NULL: can't go ahead."
  }

  def "Should not throw an exception where the required String is provided"() {
    when:
      new TextFilter.NoNullFilter("a simple string").result()

    then:
      final IllegalArgumentException exception = notThrown()
  }

}
