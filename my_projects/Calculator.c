#include <stdio.h>

int main()
{
    double a, b;
    char o;
    printf("Enter the number A for operation: ");
    scanf("%lf", &a);
    printf("Enter the number B for operation: ");
    scanf("%lf", &b);
    printf("Enter the operation (+, -, *, /): ");
    scanf(" %c", &o);

    if (o == '+')
    {
        printf("The sum of two numbers %.2lf and %.2lf is equal to %.2lf\n", a, b, a + b);
    }
    else if (o == '-')
    {
        printf("The difference between %.2lf and %.2lf is equal to %.2lf\n", a, b, a - b);
    }
    else if (o == '*')
    {
        printf("The product of two numbers %.2lf and %.2lf is equal to %.2lf\n", a, b, a * b);
    }
    else if (o == '/')
    {
        if (b != 0)
        {
            printf("The division of %.2lf and %.2lf is equal to %.2lf\n", a, b, a / b);
        }
        else
        {
            printf("Division by zero is not allowed.\n");
        }
    }
    else
    {
        printf("Invalid operation.\n");
    }

    return 0;
}



