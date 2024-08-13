#include <math.h>

// Função para calcular uma expressão quadrática: ax^2 + bx + c
void quadratic_values(double a, double b, double c, double start, double end, double step, double *values, int *count) {
    int i = 0;
    for (double x = start; x <= end; x += step) {
        values[i] = (a * x * x) + (b * x) + c;
        i++;
    }
    *count = i;
}