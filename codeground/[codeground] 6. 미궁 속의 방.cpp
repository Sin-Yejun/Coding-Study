// https://myprivatestudy.tistory.com/5
#include <iostream>
using namespace std;

int main(int argc, char** argv)
{
	int i, T, test_case;
	cin >> T;

	for (test_case = 0; test_case < T; test_case++)
	{
		int n, k;
		cin >> n >> k;
		char tmp[300000]; // direction 저장용
		cin >> tmp;
		int x = 0, y = 0; //초기 위치
		int rd = -1, base = 0; // ud : 아래나 오른쪽으로 이동할 때 1, 위나 왼쪽으로 이동할 때 0
		long long Answer = 1; //초기 위치 1번은 무조건 포함된다.
		for (i = 0; i < k; i++) {
			switch (tmp[i]) {
			case 'U':
				x--;
				rd = 0;
				break;

			case 'D':
				x++;
				rd = 1;
				break;

			case 'L':
				y--;
				rd = 0;
				break;

			case 'R':
				y++;
				rd = 1;
				break;
			}
			int pointSum = x + y; //udlr : 현재 위치가 왼쪽 아래에서 오른쪽 위로 가는 대각선들 중 몇 번째인지를 확인한다.
			if (pointSum < n) { //위쪽 삼각형
				if (rd) base += pointSum; //base : 구하는 대각선 윗부분의 방 번호 중 최댓값
				else base -= pointSum + 1;
				if (pointSum % 2 == 0) Answer += base + y + 1;
				else Answer += base + x + 1;
			}
		
			else { //아래쪽 삼각형
				if (rd) base += 2 * n - pointSum;
				else base -= 2 * n - (pointSum + 1);
				if (pointSum % 2 == 0) Answer += base + n - x;
				else Answer += base + n - y;
			}
		}
		cout << "Case #" << test_case + 1 << endl;
		cout << Answer << endl;
	}
	return 0;//Your program should return 0 on normal termination.
}