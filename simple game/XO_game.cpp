#include <iostream>
#include <string.h>
using namespace std;

class XO_game {

public:

	void ShowGame() {
		int n = 0;
		cout << "\n  -------------\n ";
		for (int i = 0; i < 3; i++) {
			cout << " | ";
			for (int j = 0; j < 3; j++) {
				cout << G[i][j] << " | ";
			}
			cout << "\n  -------------\n ";
		}
	}

	void GenGame() {
		int n = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				G[i][j] = ++n + char('0');
			}
		}
	}

	void cheakWiner() {
		if ((G[0][0] == G[0][1] && G[0][1] == G[0][2]) && (G[0][0] == 'X' || G[0][0] == 'O') || (G[1][0] == G[1][1] && G[1][1] == G[1][2]) && (G[1][2] == 'X' || G[0][2] == 'O') || (G[2][0] == G[2][1] && G[2][1] == G[2][2]) && (G[2][2] == 'X' || G[2][2] == 'O') || (G[0][0] == G[1][0] && G[1][0] == G[2][0]) && (G[2][0] == 'X' || G[2][0] == 'O') || (G[0][1] == G[1][1] && G[2][1] == G[0][1]) && (G[0][1] == 'X' || G[0][1] == 'O') || (G[0][2] == G[1][2] && G[1][2] == G[2][2]) && (G[2][2] == 'X' || G[2][2] == 'O') || (G[0][0] == G[1][1] && G[1][1] == G[2][2]) && (G[2][2] == 'X' || G[2][2] == 'O') || (G[0][2] == G[1][1] && G[1][1] == G[2][0]) && (G[2][0] == 'X' || G[2][0] == 'O'))
		{
			cout << "----------\n| " << chr << " WINs |  \n ---------- \n";
			win = true;
		}

	}

	void StarGame() {

		string input;
		int index;


		while (true)
		{
			c += 1;
			if (c == 10) {
				cout << "------\n| Draw |  \n ------ \n";
				break;
			}
			cout << "\n [ " << chr << " ] choose a number: ";
			cin >> input;

			if (input != "") {
				if (input >= "1" && input <= "9") {
					index = (int)input[0] - (int('0') + 1);
					if (G[index / 3][index % 3] != 'O' && G[index / 3][index % 3] != 'X')
					{

						G[index / 3][index % 3] = chr;
						ShowGame();
						cheakWiner();
						if (chr == 'X') {
							chr = 'O';
						}
						else {
							chr = 'X';
						}

						if (win) { break; }
					}
					else {
						c -= 1;
						puts("\n This place is used");
					}
				}
				else {
					puts("Enter number in range [1..9]\n");
				}
			}
			else {
				puts("Please print something :)");
			}
		}
	}
	XO_game();
private:
	char G[3][3];
	bool win = false;
	char chr = 'X';
	int c = 0;
};

XO_game::XO_game() {
	GenGame();
	ShowGame();
}
int main(int argc, char* argv[]) {

	XO_game G;
	G.StarGame();

}
