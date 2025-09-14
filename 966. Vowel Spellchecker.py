class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")
        
        def devowel(word: str) -> str:
            return ''.join('_' if ch in vowels else ch for ch in word.lower())
        
        original_wordlist = wordlist[:]  # preserve capitalization
        
        # Preprocess wordlist
        wordlist_lower = [w.lower() for w in wordlist]
        wordlist_devowel = [devowel(w) for w in wordlist]
        
        output = []
        for query in queries:
            q_lower = query.lower()
            q_devowel = devowel(query)
            match_found = ""
            
            # Step 1: exact match
            for word in original_wordlist:
                if query == word:
                    match_found = word
                    break
            
            # Step 2: case-insensitive match
            if not match_found:
                for idx, w_lower in enumerate(wordlist_lower):
                    if q_lower == w_lower:
                        match_found = original_wordlist[idx]
                        break
            
            # Step 3: vowel match
            if not match_found:
                for idx, w_devowel in enumerate(wordlist_devowel):
                    if q_devowel == w_devowel:
                        match_found = original_wordlist[idx]
                        break
            
            output.append(match_found)
        
        return output
