#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>

typedef double complex comp;
const double pi = 3.1415926535897932384;

int poweroftwo(int n)
{
    if (n == 1)
        return 1;
    if (n % 2)
        return 0;
    return poweroftwo(n / 2);
}

comp *transform(comp input[], int n, int inv) 
{
    if (n < 1 || !poweroftwo(n))
    {
        fprintf(stderr, "Input length must be a power of two, exiting...\n");
        exit(EXIT_FAILURE);
    }
    if (n <= 1)
        return input;

    comp *even = (comp *)malloc((n / 2) * sizeof(comp));
    comp *odd = (comp *)malloc((n / 2) * sizeof(comp));
    comp *output = (comp *)malloc(n * sizeof(comp));

    for (int i = 0; i < n; i++)
        (i % 2 ? odd : even)[i / 2] = input[i];

    even = transform(even, n / 2, inv);
    odd = transform(odd, n / 2, inv);

    for (int i = 0; i < n / 2; i++)
    {
        comp expo = cos(2 * (inv ? pi : -pi) * i / n) + (I * sin(2 * (inv ? pi : -pi) * i / n));
        output[i] = (even[i] + expo * odd[i]) / (inv ? 2 : 1);
        output[i + n / 2] = (even[i] - expo * odd[i]) / (inv ? 2 : 1);
    }
    free(even);
    free(odd);
    return output;
}

void write_to_file(comp *c, char *filename, int n)
{
    FILE *f;
    f = fopen(filename, "w");
    for (int i = 0; i < n; i++)
    {
        fprintf(f, "%lf\n %lf\n", creal(c[i]), cimag(c[i]));
    }
    fclose(f);
}

void print(comp *c, int n)
{
    for (int i = 0; i < n; i++)
        printf("%f %f\n", creal(c[i]), cimag(c[i]));
}

int main()
{
    int n = 8;
    comp x[] = {0, 9, 1, 1, 2, 0, 0, 1};

    comp *Y = transform(x, n, 0);
    printf("%s\n", "fft");
    print(Y, n);
    write_to_file(Y, "../data/dft.dat", n);

    comp *xhat = transform(Y, n, 1);
    printf("%s\n", "ifft");
    print(xhat, n);
    write_to_file(xhat, "../data/idft.dat", n);

    return 0;
}