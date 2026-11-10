package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class RomanNumberFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?i)(?<=^|[ \\t]|[\\p{P}&&[^.]])(?=[MDCLXVI])M*(?:C[MD]|D?C{0,3})(?:X[CL]|L?X{0,3})(?:I[XV]|V?I{0,3})(?=[\\p{P}&&[^.]]|[ \\t]|$)");
	private static final Pattern EXCLUDE = Pattern.compile("(?i)^[MDCLV]I$");
	private final TextFilter origin;

	public RomanNumberFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result(), PATTERN,
			match -> EXCLUDE.matcher(match.group()).find() ? match.group() : match.group().toUpperCase());
	}
}
