nclude<iostream>
using namespace std;
int main() {
    string s;
    bool t = true;
    cin >> s;
    if (islower(s[0])) {

        for (int i = 1; i <= s.length();i++) {
            if (toupper(s[i]) != s[i]) {
                cout << s;
                t = false;
                break;
            }
        }
        if (t) {
            cout << char(toupper(s[0]));
            for (int i = 1; i <= s.length(); i++) {
                cout << char(tolower(s[i]));
            }
        }
    }
    else {
        for (int i = 1; i <= s.length(); i++) {
            if (toupper(s[i]) != s[i]) {
                cout << s;
                t = false;
                break;
            }
        }
        if (t) {
            cout << char(tolower(s[0]));
            for (int i = 1; i <= s.length(); i++) {
                cout << char(tolower(s[i]));
            }
        }
    }
}
