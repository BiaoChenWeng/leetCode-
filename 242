class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        else {
            vector<int>letrasS(27, 0);
            vector<int>letrasT(27, 0);
            for (int i = 0; i < s.size(); i++) {
                letrasS[s[i] - 'a']++;
                letrasT[t[i] - 'a']++;
            }
            for (int i = 0; i < letrasS.size();i++) {
                if (letrasS[i] != letrasT[i])
                    return false;
            }
            return true;
        }
    }
};
