#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <windows.h>
#include <math.h>
#include <iostream>
using namespace std;


// ���������������� ������������� ����������       ������� 5 (1) - �����

/*
int main()
{
	SetConsoleOutputCP(1251);
	double a, b, c;
	printf("������� a - ");
	scanf("%lf", &a);
	printf("������� b - ");
	scanf("%lf", &b);
	printf("������� c - ");
	scanf("%lf", &c);

	if (a + b > c & b + c > a & a + c > b)
		if ((a == b) & (b == c))
			printf("����������� � ������� ��������� �������� ��������������");
		else if ((a == b & a != c) || (b == c & b != a) || (a == c & a != b))
			printf("����������� � ������� ��������� �������� ��������������");
		else printf("����������� � ������� ��������� �������� ��������������");

	else printf("������������ � ������� ��������� �� ����������");
}
*/



// 20.09.24       ���������������� ����������� ����������             ������� ����� 6, 10, 15, 24, 30, 35   - �����

//������� 6 - ����������

/*
int main()
{
	SetConsoleOutputCP(1251);
	int N, kol, nenul = 0, sum2 = 0;
	cout << "������� ���-�� ��������� - ";
	cin >> N;

	for (kol = 1; kol <= N; kol++)
	{
		int x;
		cout << "������� ���������� - ";
		cin >> x;

		if (x != 0)
			nenul++;

		if (x < 2)
			sum2 = sum2 + x;
	}
	cout << "���-�� ��������� ��������� - " << nenul << endl;
	cout << "����� ���������, ������� ������ ������ - " << sum2;
}
*/

//������� 10 - ����������

/*
int main()
{
	SetConsoleOutputCP(1251);
	int N, k, x, flag = 0;
	cout << "������� ���-�� ��������� - ";
	cin >> N;

	for (k = 1; k <= N; k++)
	{
		cout << "������� ���������� - ";
		cin >> x;

		if (x == 0)
		{
			cout << "������ ���� � ������������������ ����� ����� - " << k;
			break;
		}
			flag = 1;

	}
	if (flag == 0)
		cout << "���� �����������";

}
*/

//������� 15 - ����������

/*
int main()
{
	SetConsoleOutputCP(1251);
	int N, k, posl = 1, umn = 1;
	cout << "������� ���-�� ������ ������������������ - ";
	cin >> N;

	for (k = 2; k <= N + 1; k++)
	{
		umn = umn * posl;
		posl = posl + k;
	}
	cout << "������������ ������ ������������������ ������� ���� = " << umn;
}
*/

//������� 24 - ����������

/*
int main()
{
	SetConsoleOutputCP(1251);
	srand(time(0));

	int N, i, a, proizv5 = 1;
	cout << "������� ���-�� ������ �������������� ��������� - ";
	cin >> N;

	int smin = 1, smax = 10;
	int a1 = rand() % (smax - smin + 1) + smin;               // ������ ��������� ���������� �� ���������
	int d = rand() % (smax - smin + 1) + smin;

	a = a1;
	if (a > 5)
		proizv5 *= a;

	cout << a1 << endl;
	for (i = 0; i < N-1; i++)                      // for (��������� ���������� = 0 ; ������� ; ��������� ����������)
	{
		a += d;
		cout << a << endl;
		if (a > 5)
			proizv5 *= a;
	}

	cout << "������������ ���� ���������, ������� 5 = " << proizv5;
}

*/

//������� 30 - ����������

/*
int main()
{
	SetConsoleOutputCP(1251);
	int i, x, k=0,sum=0;
	for (i = 0; i < 15; i++)
	{
		cout << "������� ����� �� 0 �� 10  - ";
		cin >> x;
		if (x == 4)
		{
		k++;
		sum += x;
		}
	}

	cout << "���-�� �����, ������� 5, �� ������� 3  = " << k << endl;
	cout << "����� �����, ������� 5, �� ������� 3  = " << sum << endl;

}
*/

//������� 35 - ����������

/*
int main()
{
	SetConsoleOutputCP(1251);
	int x, y, z;
	bool find = false;
	for (x = 1; x <= 9; x++)
		for (y = 0; y <= 9; y++)
			for (z = 0; z <= 9; z++)
				if ((x * x * x) + (y * y * y) + (z * z * z) == 730 && !find)
				{
					cout << x << " " << y << " " << z << endl;
					find = true;
					break;
				}

}
*/



//25.10.24 ������, ������, ��������� - �����

/*
#define _CRT_SECURE_NO_WARNINGS
#define PI 3.14159
#include <stdio.h>
#include <windows.h>
#define N 11
#include <math.h>
#include <iostream>
using namespace std;

int main()
{
#if N==1
	SetConsoleOutputCP(1251);

	int* ptrInt;
	double* ptrDouble;
	char* ptrChar;

	cout << "������ ��������� �� int: " << sizeof(ptrInt) << " ����" << endl;
	cout << "������ ��������� �� double: " << sizeof(ptrDouble) << " ����" << endl;
	cout << "������ ��������� �� char: " << sizeof(ptrChar) << " ����" << endl;

	return 0;

#elif N==3
	SetConsoleOutputCP(1251);

	double* num1 = new double;
	double* num2 = new double;

	cout << "������� ������ �����: ";
	cin >> *num1;

	cout << "������� ������ �����: ";
	cin >> *num2;

	double sum = *num1 + *num2;
	double difference = *num1 - *num2;

	cout << "�����: " << sum << endl;
	cout << "��������: " << difference << endl;

	delete num1;
	delete num2;

	return 0;

#elif N==5
	SetConsoleOutputCP(1251);

	int number = 10;
	int& refNumber = number;

	cout << "�������� �������� number: " << number << endl;

	refNumber = 20;

	cout << "����� �������� number (����� ������): " << refNumber << endl;

	return 0;

#elif N==7
	SetConsoleOutputCP(1251);

	double number = 5.0;
	double* ptrNumber = &number;

	cout << "�������� �������� number: " << number << endl;

	*ptrNumber *= 2;

	cout << "����� �������� number: " << number << endl;

	return 0;

#elif N==9
	SetConsoleOutputCP(1251);

	int num1, num2, num3;
	int& refNum1 = num1;
	int& refNum2 = num2;
	int& refNum3 = num3;

	cout << "������� ������ �����: ";
	cin >> refNum1;

	cout << "������� ������ �����: ";
	cin >> refNum2;

	refNum3 = 2 * (refNum1 * refNum1 - refNum2 * refNum2);

	cout << "����� �3 = " << num3 << endl;

	return 0;

#elif N==11
	SetConsoleOutputCP(1251);

	const double value = 3.14;

	const double* const ptrValue = &value;
	const double* const* ptrPtrValue = &ptrValue;

	cout << "�������� ������������ ���������: " << **ptrPtrValue << endl;

	return 0;
#endif

} */



//01.11.24 ��������������� ��������
