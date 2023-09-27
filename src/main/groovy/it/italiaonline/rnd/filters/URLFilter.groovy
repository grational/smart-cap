package it.italiaonline.rnd.filters

import java.util.regex.Pattern

class URLFilter implements TextFilter {

	private final TextFilter origin
	private final Pattern pattern = ~$/(?i)(?:(?:ht|f)tps?://)?(?:[a-z0-9-]{3,}[.])+[a-z]{2,}(?::[1-9][0-9]{0,4})?(?:/.*)?/$

	URLFilter(TextFilter orig) {
		this.origin = orig
	}

	@Override
	String result() {
		origin.result().replaceAll(pattern) { all ->
			return all.toLowerCase()
		}
	}
}
