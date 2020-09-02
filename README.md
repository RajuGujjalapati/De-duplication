# Flask_Deduplication_backend
This repository mainly consists of API's which helps us to add data to database and fetch user details and prints the matching percentages according to input.<br>

The four fuzzywuzzy methods call difflib.ratio on different combinations of the input strings.
<br>
<b>fuzz.ratio</b>
Simple. Just calls difflib.ratio on the two input strings (code).
<br>
fuzz.ratio("NEW YORK METS", "NEW YORK MEATS")<br>
96<br>
<b>fuzz.partial_ratio</b>
Attempts to account for partial string matches better. Calls ratio using the shortest string (length n) against all n-length substrings of the larger string and returns the highest score (code).<br>

Notice here that "YANKEES" is the shortest string (length 7), and we run the ratio with "YANKEES" against all substrings of length 7 of "NEW YORK YANKEES" (which would include checking against "YANKEES", a 100% match):<br>

fuzz.ratio("YANKEES", "NEW YORK YANKEES")<br>
60<br>
fuzz.partial_ratio("YANKEES", "NEW YORK YANKEES")<br>
100<br>
fuzz.token_sort_ratio<br>
Attempts to account for similar strings out of order. Calls ratio on both strings after sorting the tokens in each string (code). Notice here fuzz.ratio and fuzz.partial_ratio both fail, but once you sort the tokens it's a 100% match:<br>

fuzz.ratio("New York Mets vs Atlanta Braves", "Atlanta Braves vs New York Mets")<br>
45<br>
fuzz.partial_ratio("New York Mets vs Atlanta Braves", "Atlanta Braves vs New York Mets")<br>
45<br>
fuzz.token_sort_ratio("New York Mets vs Atlanta Braves", "Atlanta Braves vs New York Mets")<br>
100<br>
<b>fuzz.token_set_ratio</b><br>
Attempts to rule out differences in the strings. Calls ratio on three particular substring sets and returns the max (code):<br>

intersection-only and the intersection with remainder of string one<br>
intersection-only and the intersection with remainder of string two<br>
intersection with remainder of one and intersection with remainder of two<br>
Notice that by splitting up the intersection and remainders of the two strings, we're accounting for both how similar and different the two strings are:<br>

fuzz.ratio("mariners vs angels", "los angeles angels of anaheim at seattle mariners")<br>
36<br>
fuzz.partial_ratio("mariners vs angels", "los angeles angels of anaheim at seattle mariners")<br>
61<br>
fuzz.token_sort_ratio("mariners vs angels", "los angeles angels of anaheim at seattle mariners")<br>
51<br>
fuzz.token_set_ratio("mariners vs angels", "los angeles angels of anaheim at seattle mariners")<br>
91<br>
<b>Application</b><br>
This is where the magic happens. At SeatGeek, essentially we create a vector score with each ratio for each data point (venue, event name, etc) and use that to inform programatic decisions of similarity that are specific to our problem domain.<br>

That being said, truth by told it doesn't sound like FuzzyWuzzy is useful for your use case. It will be tremendiously bad at determining if two addresses are similar.<br> Consider two possible addresses for SeatGeek HQ: "235 Park Ave Floor 12" and "235 Park Ave S. Floor 12":<br>

fuzz.ratio("235 Park Ave Floor 12", "235 Park Ave S. Floor 12")<br>
93<br>
fuzz.partial_ratio("235 Park Ave Floor 12", "235 Park Ave S. Floor 12")<br>
85<br>
fuzz.token_sort_ratio("235 Park Ave Floor 12", "235 Park Ave S. Floor 12")<br>
95<br>
fuzz.token_set_ratio("235 Park Ave Floor 12", "235 Park Ave S. Floor 12")<br>
100<br>
