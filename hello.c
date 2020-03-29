#include <stdio.h>
#include <string.h>

int printMsg(char *msg, int len) {
    int maxLen = 13;
    char out[maxLen + 1];
    if ( len > maxLen )
        return 1;
    strncpy(out, msg, len);
    out[len] = '\0';
    printf("%s\n", out);
    return 0;
}
