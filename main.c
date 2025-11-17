#include <stdio.h>
#include <string.h>

int main()
{
    // date
    char date[50] = "";
    // description
    char desc[100] = "";
    // money payed
    char payed[20] = "";

    // date
    printf("Date of purchase (e.g DD/MM/YYYY):\n");
    fgets(date, sizeof(date), stdin);
    date[strcspn(date, "\n")] = '\0';
    
    // desc
    printf("Description:\n");
    fgets(desc, sizeof(desc), stdin);
    desc[strcspn(desc, "\n")] = '\0';
    // money payed
    printf("Amount payed and currency:\n");
    fgets(payed, sizeof(payed), stdin);
    payed[strcspn(payed, "\n")] = '\0';;

    FILE *file = fopen("expenses.txt", "a");
    fprintf(file, "%s %s %s\n", date, desc, payed);
    fclose(file);
}