package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class CompanyTypeAcronymFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?i)(?<=^|[-_, \\t])(s[.])((?:c[.]a[.]r[.]l|r[.]l[.]s|c[.]r[.]l|a[.]p[.]a|r[.]l|p[.]a|n[.]c|a[.]s|a[.]a)[.]?)(?=[-_, \\t]|$)");
	private final TextFilter origin;

	public CompanyTypeAcronymFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result(), PATTERN,
			match -> match.group(1).toUpperCase() + match.group(2).toLowerCase());
	}
}
