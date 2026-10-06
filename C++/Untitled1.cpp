#include <iostream>

double calculaMedia (double a, double b, double c, char tipo) {
	double m;
	switch (tipo) {
		case 'G':
			m = a  * b * c;
			std::cout << "Media Geometrica: " << m;
		case 'P':
			m = (a + 2 * b + 3 * c) / 6.0;
			std::cout << "Media Ponderada: " << m;
		case 'H':
			m = 3.0 / (1.0/a + 1.0/b + 1.0/c);
			std::cout << "Media Harmonica: " << m;
		case 'A':
			m = (a * b * c) / 3;
			std::cout << "Media Aritmetica: " << m;
	}
	return m;
}

int main() {
	int val[3];
	std::cout << "Digite tres valores inteiros positivos: ";
	for (int i = 0; i < 3; i++) {
		std::cin >> val[i];
	}
	char t;
	std::cout << "Digite a media desejada: ";
	std::cin >> t;
	double media = calculaMedia (val[0], val[1], val[2], t);

}
