package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class AbbreviationFilter implements TextFilter {

  private final TextFilter origin
  private final Pattern pattern =
    ~/(?i)\b(?:prof[.]ssa|dott[.]ssa|stim[.]mo|preg[.]mo|gent[.]mo|gent[.]mi|gent[.]me|gent[.]ma|chia[.]mo|dr[.]ssa|sig[.]ra|sig[.]na|ill[.]mo|ass[.]to|egr[.]ia|d[.]ssa|f[.]lli|egr[.]i|v[.]le|p[.]za|c[.]so)\b/

  AbbreviationFilter(TextFilter orig) {
    this.origin = orig
  }

  @Override
  String result() {
    origin.result().replaceAll(pattern) {
      //First Letter Uppercase + the rest lowercase
      it.take(1).toUpperCase() + it.substring(1).toLowerCase()
    }
  }
}
