# PolyWord
Identifies all possible words from poly words puzzle published in the 
[Daily Telegraph](https://puzzles.telegraph.co.uk/)

### Poly Word Rules
  1. All words created must include the key central letter
  2. No Capitalized words
  3. No plurals

At the moment words that don't fit the rule #2 of Poly Word are only marked with a 
**possible invalid** tag. As of 19.04.2021, there is no current implementation to remove plurals 

I intend have two modes where you can just quickly see the nine-letter word or
have an output of all identified words within the 9 letters available.

## Future Plans
  * Implement image recognition to identify the Ploy Word octagons and the text within them
  * Output identified words in to tables and store in AWS
  * Create UI (or potential website) to drag and drop Poly Word images for analysis
  * Update the dictionary used for word identification (Currently: [words.txt](words.txt))
  * Update the disallowed words to check dictionary definition. If only Proper 
    noun in definition section (maybe keyword such as city, country, name, etc)
    exclude word from final table
