package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class CompanyTypeAcronymFilter implements TextFilter {

  private final TextFilter origin

  private final Pattern pattern =
    ~/(?i)(?<=^|[-_, \t])(s[.])((?:c[.]a[.]r[.]l|r[.]l[.]s|c[.]r[.]l|a[.]p[.]a|r[.]l|p[.]a|n[.]c|a[.]s|a[.]a)[.]?)(?=[-_, \t]|$)/

  CompanyTypeAcronymFilter(TextFilter orig) {
    this.origin = orig
  }

  @Override
  String result() {
    origin.result().replaceAll(pattern) { all, head, tail ->
      head.toUpperCase() + tail.toLowerCase()
    }
  }
}
