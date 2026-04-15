class Solution {
  public:
    string URLify(string &s) {
        string res = "";
        
        for(char ch : s) {
            if(ch == ' ')
                res += "%20";
            else
                res += ch;
        }
        
        return res;
    }
};