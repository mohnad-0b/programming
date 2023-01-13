class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int len = strs[0].length();
        for (int i=0;i<strs.size();i++){
          if ((strs[i].length()) < len)
              len = strs[i].length();
        
        }
        // std::cout << len ;
        std::string ans = "";
        
        for (int i=0;i<len;i++){
          std::string c = strs[0].substr(i,1); 
          for (int j=0;j<strs.size();j++){
              if (c != strs[j].substr(i,1)){
                return ans;
                }
             
          }
          ans += c;

         
        }

        return ans;

        
    
    }
};
