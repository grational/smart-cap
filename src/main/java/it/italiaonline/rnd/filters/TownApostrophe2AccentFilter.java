package it.italiaonline.rnd.filters;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.regex.Pattern;

public class TownApostrophe2AccentFilter implements TextFilter {
	private static final Pattern PATTERN = Pattern.compile("(?i)(\\w+[aeiou])'(?=[\\p{P}&&[^.]]|[ \\t]|$)");
	private final TextFilter origin;
	private Map<String, String> accentedTowns = defaultAccentedTowns();

	public TownApostrophe2AccentFilter(TextFilter origin) {
		this.origin = origin;
	}

	public Map<String, String> getAccented_towns() {
		return accentedTowns;
	}

	public void setAccented_towns(Map<String, String> accentedTowns) {
		this.accentedTowns = accentedTowns;
	}

	@Override
	public String result() {
		return RegexReplacement.replaceAll(origin.result(), PATTERN, match -> {
			String town = accentedTowns.get(match.group(1).toLowerCase());
			return town == null || town.isEmpty() ? match.group() : town;
		});
	}

	private static Map<String, String> defaultAccentedTowns() {
		Map<String, String> towns = new LinkedHashMap<>();
		towns.put("aglie", "Agliè");
		towns.put("alluvioni cambio", "Alluvioni Cambiò");
		towns.put("alme", "Almè");
		towns.put("ali", "Alì");
		towns.put("antey-saint-andre", "Antey-Saint-André");
		towns.put("arsie", "Arsiè");
		towns.put("barzano", "Barzanò");
		towns.put("bascape", "Bascapè");
		towns.put("baselga di pine", "Baselga di Pinè");
		towns.put("basico", "Basicò");
		towns.put("bastia mondovi", "Bastia Mondovì");
		towns.put("belvi", "Belvì");
		towns.put("bianze", "Bianzè");
		towns.put("bidoni", "Bidonì");
		towns.put("budduso", "Buddusò");
		towns.put("cagno", "Cagnò");
		towns.put("canicatti", "Canicattì");
		towns.put("cantu", "Cantù");
		towns.put("carde", "Cardè");
		towns.put("carre", "Carrè");
		towns.put("carru", "Carrù");
		towns.put("castel san niccolo", "Castel San Niccolò");
		towns.put("castelfranco piandisco", "Castelfranco Piandiscò");
		towns.put("cavaglia", "Cavaglià");
		towns.put("cefalu", "Cefalù");
		towns.put("centa san nicolo", "Centa San Nicolò");
		towns.put("cesaro", "Cesarò");
		towns.put("ciglie", "Cigliè");
		towns.put("cimina", "Ciminà");
		towns.put("cirie", "Ciriè");
		towns.put("ciro", "Cirò");
		towns.put("codogne", "Codognè");
		towns.put("condro", "Condrò");
		towns.put("cuorgne", "Cuorgnè");
		towns.put("dare", "Darè");
		towns.put("dasa", "Dasà");
		towns.put("dolce", "Dolcè");
		towns.put("erbe", "Erbè");
		towns.put("fenegro", "Fenegrò");
		towns.put("fiave", "Fiavè");
		towns.put("forli", "Forlì");
		towns.put("forza d'agro", "Forza d'Agrò");
		towns.put("fosso", "Fossò");
		towns.put("frazzano", "Frazzanò");
		towns.put("galtelli", "Galtellì");
		towns.put("gambolo", "Gambolò");
		towns.put("gonnosno", "Gonnosnò");
		towns.put("gressoney-la-trinite", "Gressoney-la-Trinité");
		towns.put("gualtieri sicamino", "Gualtieri Sicaminò");
		towns.put("leini", "Leinì");
		towns.put("lode", "Lodè");
		towns.put("loranze", "Loranzè");
		towns.put("lusiglie", "Lusigliè");
		towns.put("maiera", "Maierà");
		towns.put("male", "Malè");
		towns.put("mansue", "Mansuè");
		towns.put("mazze", "Mazzè");
		towns.put("melicucca", "Melicuccà");
		towns.put("meri", "Merì");
		towns.put("mondovi", "Mondovì");
		towns.put("montaldo di mondovi", "Montaldo di Mondovì");
		towns.put("monta", "Montà");
		towns.put("muggio", "Muggiò");
		towns.put("nardo", "Nardò");
		towns.put("nughedu san nicolo", "Nughedu San Nicolò");
		towns.put("onani", "Onanì");
		towns.put("palu", "Palù");
		towns.put("panchia", "Panchià");
		towns.put("paterno", "Paternò");
		towns.put("patu", "Patù");
		towns.put("petrona", "Petronà");
		towns.put("plati", "Platì");
		towns.put("ponte san nicolo", "Ponte San Nicolò");
		towns.put("portobuffole", "Portobuffolè");
		towns.put("prela", "Prelà");
		towns.put("revo", "Revò");
		towns.put("rocca ciglie", "Rocca Cigliè");
		towns.put("roccaforte mondovi", "Roccaforte Mondovì");
		towns.put("ronca", "Roncà");
		towns.put("rora", "Rorà");
		towns.put("rosa", "Rosà");
		towns.put("roveredo di gua", "Roveredo di Guà");
		towns.put("salo", "Salò");
		towns.put("san michele mondovi", "San Michele Mondovì");
		towns.put("san pietro di carida", "San Pietro di Caridà");
		towns.put("sanfre", "Sanfrè");
		towns.put("santa maria hoe", "Santa Maria Hoè");
		towns.put("santa maria la carita", "Santa Maria la Carità");
		towns.put("santhia", "Santhià");
		towns.put("scorze", "Scorzè");
		towns.put("secli", "Seclì");
		towns.put("senorbi", "Senorbì");
		towns.put("serra ricco", "Serra Riccò");
		towns.put("soddi", "Soddì");
		towns.put("sorga", "Sorgà");
		towns.put("staletti", "Stalettì");
		towns.put("temu", "Temù");
		towns.put("torpe", "Torpè");
		towns.put("torre mondovi", "Torre Mondovì");
		towns.put("tortoli", "Tortolì");
		towns.put("trinita", "Trinità");
		towns.put("vestigne", "Vestignè");
		towns.put("vialfre", "Vialfrè");
		towns.put("vigano", "Viganò");
		towns.put("viggiu", "Viggiù");
		towns.put("villa d'alme", "Villa d'Almè");
		towns.put("villanova mondovi", "Villanova Mondovì");
		towns.put("viu", "Viù");
		towns.put("zane", "Zanè");
		towns.put("zerbolo", "Zerbolò");
		return towns;
	}
}
