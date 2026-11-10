package it.italiaonline.rnd.filters;

import java.util.function.Function;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** Literal, computed replacements using the Java 8 regular expression API. */
final class RegexReplacement {
	private RegexReplacement() {
	}

	static String replaceAll(String input, Pattern pattern, Function<Matcher, String> replacement) {
		Matcher matcher = pattern.matcher(input);
		StringBuffer result = new StringBuffer();
		while (matcher.find()) {
			matcher.appendReplacement(result, Matcher.quoteReplacement(replacement.apply(matcher)));
		}
		return matcher.appendTail(result).toString();
	}
}
