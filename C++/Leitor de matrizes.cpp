#include <iostream>

int main()
{
    int m, n;
    int mat[50][50];
    std::cout << "Entre com m e n: ";
    std::cin >> m >> n;
    std::cout << "Entre com a matriz: ";
    for (int i = 0; i < m; i++) {
        for (int j = 1; j <= n; j++)  {
            std::cin >> mat[i][j];
        }
    }
    int lnula = 0;
    bool nula = true;
    for (int i = 0; i < m; i++) {
        for (int j = 1; j <= n; j++){
            if (mat[i][j] != 0) {
                nula = false;
            }
        }
        if (nula == true) {
            lnula = lnula + 1;
        }
        nula = true;
    }
    int cnula = 0;
    nula = true;
    for (int i = 0; i < m; i++) {
        for (int j = 1; j <= n; j++){
            if (mat[j][i] != 0) {
                nula = false;
            }
        }
        if (nula == true) {
            cnula = cnula + 1;
        }
        nula = true;
    }
    std::cout << "Linhas nulas: " << lnula << std::endl << "Colunas nulas: " << cnula;
}
