package it.italiaonline.rnd.filters;

import java.util.HashMap;
import java.util.Map;

/** Executes against production dependencies only, without Groovy or a test framework. */
public final class JavaCompatibilityCheck {
	public static void main(String[] args) throws Exception {
		try {
			Class.forName("groovy.lang.GroovyObject");
			throw new AssertionError("Groovy must not be a production dependency");
		} catch (ClassNotFoundException expected) {
			// A Java consumer must not need Groovy on its class path.
		}
		equals("Atres S.r.l.", new TextFilter.SmartCap("ATRES S.R.L.").result());
		equals("Via Boito Arrigo, 41", new TextFilter.AddressSmartCap("VIA BOITO ARRIGO,41").result());
		equals("Santhià", new TextFilter.AddressSmartCap("SANTHIA'").result());
		equals("G come Di Gioia", new TextFilter.ConditionalSmartCap("G come Di Gioia", 0.85d).result());
		equals("ATRES S.R.L.", new TextFilter.ConditionalSmartCap("ATRES S.R.L.", 0.0d).result());
		equals("Iis Service", new TextFilter.ConditionalSmartCap("IIS Service", 1.0d).result());
		equals("", new TextFilter.SmartCap("").result());
		equals("Text", new CapitalizeFilter(() -> "TEXT").result());
		equals("https://example.it/$1\\folder", new URLFilter(() -> "HTTPS://EXAMPLE.IT/$1\\FOLDER").result());

		TownApostrophe2AccentFilter towns = new TownApostrophe2AccentFilter(() -> "TESTA'");
		Map<String, String> accents = new HashMap<>();
		accents.put("testa", "Testà");
		towns.setAccented_towns(accents);
		equals("Testà", towns.result());
		towns.getAccented_towns().put("testa", "");
		equals("TESTA'", towns.result());

		try {
			new TextFilter.SmartCap(null).result();
			throw new AssertionError("Null input must be rejected");
		} catch (IllegalArgumentException expected) {
			equals("Input is NULL: can't go ahead.", expected.getMessage());
		}
		System.out.println("Java compatibility checks passed without Groovy");
	}

	private static void equals(String expected, String actual) {
		if (!expected.equals(actual)) {
			throw new AssertionError("Expected <" + expected + "> but got <" + actual + ">");
		}
	}
}
