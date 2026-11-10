package it.italiaonline.rnd.filters;

import java.util.regex.Pattern;

public class ProvinceAbbreviationFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?i)(?<=[(])(?:AG|AL|AN|AO|AP|AQ|AR|AT|AV|BA|BG|BI|BL|BN|BO|BR|BS|BT|BZ|CA|CB|CE|CH|CI|CL|CN|CO|CR|CS|CT|CV|CZ|EN|FC|FE|FG|FI|FM|FR|GE|GO|GR|IM|IS|KR|LC|LE|LI|LO|LT|LU|MB|MC|ME|MI|MN|MO|MS|MT|NA|NO|NU|OG|OR|OT|PA|PC|PD|PE|PG|PI|PN|PO|PR|PT|PU|PV|PZ|RA|RC|RE|RG|RI|RM|RN|RO|SA|SI|SM|SO|SP|SR|SS|SV|TA|TE|TN|TO|TP|TR|TS|TV|UD|VA|VB|VC|VE|VI|VR|VS|VT|VV)(?=[)])");
	private final TextFilter origin;

	public ProvinceAbbreviationFilter(TextFilter origin) {
		this.origin = origin;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result(), PATTERN,
			match -> match.group().toUpperCase());
	}
}
