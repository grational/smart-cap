package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class RomanNumberFilter implements TextFilter {

  private final TextFilter origin
  private final Pattern pattern = ~/(?i)(?<=^|[ \t]|[\p{P}&&[^.]])(?=[MDCLXVI])M*(?:C[MD]|D?C{0,3})(?:X[CL]|L?X{0,3})(?:I[XV]|V?I{0,3})(?=[\p{P}&&[^.]]|[ \t]|$)/
  private final Pattern exclude = ~/(?i)^[MDCLV]I$/

  RomanNumberFilter(TextFilter orig) {
    this.origin = orig
  }

  @Override
  String result() {
    origin.result().replaceAll(pattern) {
      if (it =~ exclude ) {
        it
      } else {
        it.toUpperCase()
      }
    }
  }
}
