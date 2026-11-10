package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class URLFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?i)(?:(?:ht|f)tps?://)?(?:[a-z0-9-]{3,}[.])+[a-z]{2,}(?::[1-9][0-9]{0,4})?(?:/.*)?");
	private final TextFilter origin;

	public URLFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result(), PATTERN,
			match -> match.group().toLowerCase());
	}
}
