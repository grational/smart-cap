package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class SimpleConjunctionFilter implements TextFilter {

  private final TextFilter origin
  private final Pattern pattern =
    ~/(?i)(?<=[ \t])(?:ed|e|o)(?=[ \t])/
    //e, né, o, inoltre, ma, però, dunque, anzi, che

  SimpleConjunctionFilter(TextFilter orig) {
    this.origin = orig
  }

  @Override
  String result() {
    origin.result().replaceAll(pattern) {
      it.toLowerCase()
    }
  }
}
