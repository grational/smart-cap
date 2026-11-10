package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class AbbreviationFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?i)\\b(?:prof[.]ssa|dott[.]ssa|stim[.]mo|preg[.]mo|gent[.]mo|gent[.]mi|gent[.]me|gent[.]ma|chia[.]mo|dr[.]ssa|sig[.]ra|sig[.]na|ill[.]mo|ass[.]to|egr[.]ia|d[.]ssa|f[.]lli|egr[.]i|v[.]le|p[.]za|c[.]so)\\b");
	private final TextFilter origin;

	public AbbreviationFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result(), PATTERN,
			match -> match.group().substring(0, 1).toUpperCase() + match.group().substring(1).toLowerCase());
	}
}
