#include <stdio.h>
#include <stdlib.h>

int want_cha1;

int getDigitNum(int want, int count);
int getDigit(int num);


int main() {
	int i, i1, want_cha2, want_cha3, br_count;
	int* br;
	scanf_s("%d", &want_cha1);
	want_cha2 = want_cha1;
	want_cha3 = want_cha1;
	scanf_s("%d", &br_count); 
	if (br_count != 0) {
		br = (int*)malloc(sizeof(int) * br_count);
		if (br == NULL) exit(1);
		for (i = 0;i < br_count;i++) scanf_s("%d", &br[i]);
		for (i = 1;i <= getDigit(want_cha2);i++) {
			for (i1 = 0;i1 < br_count;i1++) {
				if (getDigitNum(want_cha2, i) == br[i1]) {
					if (i == 1) want_cha2 -= 1;
					else want_cha2 -= 10 * (i - 1);
					i = 0;
					break;
				}
			}
			if (abs(want_cha1 - want_cha2) > want_cha1 - 100)break;
		}
		for (i = 1;i <= getDigit(want_cha3);i++) {
			for (i1 = 0;i1 < br_count;i1++) {
				if (getDigitNum(want_cha3, i) == br[i1]) {
					if (i == 1) want_cha3 += 1;
					else want_cha2 += 10 * (i - 1);
					i = 0;
					break;
				}
			}
			if (abs(want_cha1 - want_cha3) > abs(want_cha1 - want_cha2) || abs(want_cha1 - want_cha3) > want_cha1 - 100) break;
		}
		if (getCount(want_cha2) <= getCount(want_cha3) && getCount(want_cha2) <= want_cha1 - 100) printf("%d", getCount(want_cha2));
		else if (getCount(want_cha3) <= getCount(want_cha2) && getCount(want_cha3) <= want_cha1 - 100) printf("%d", getCount(want_cha3));
		else  printf("%d", want_cha1 - 100);
		//printf("%d %d", getCount(want_cha2), getCount(want_cha3));
		free(br);
	}
	else printf("%d", getDigit(want_cha1));
	return 0;

}
int getDigitNum(int want, int count) {
	int i;
	for (i = 1;i < count;i++)
		want = (want - (want % 10)) / 10;
	return want % 10;
}

int getDigit(int num) {
	int count = 0;
	while(num > 0) {
		num /= 10;
		count++;
	}
	return count;
}

int getCount(int num) {
	return getDigit(num) + abs(want_cha1 - num);
}