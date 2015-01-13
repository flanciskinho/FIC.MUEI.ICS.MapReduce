#include <stdio.h>
#include <stdlib.h>

#include <stdbool.h>
#include <string.h>

#include <libxml/xmlmemory.h>
#include <libxml/parser.h>

#define SIZE_LIST 10000
char *list[SIZE_LIST];
int pos;


void add(char *str) {
	list[pos] = strdup(str);
	pos++;
}

bool find(char *str) {
	for (int cnt = 0; cnt < pos; cnt++) {
		if (!strcmp(list[cnt], str))
			return true;
	}

	return false;
}

void exit_msg(char *s1, char *s2) {
	printf("%s: %s\n", s1, s2);
}

int main (int argc, char *argv[]) {
	char url[] = "http://ics-mei-udc.s3-us-west-2.amazonaws.com/";

	xmlDocPtr doc = xmlParseFile(argv[1]);
    if (doc == NULL) {
        exit_msg("main","Document not parsed successfully");
    }
    xmlNodePtr  cur = xmlDocGetRootElement(doc);
    if (cur == NULL) {
        exit_msg("main","empty document");
    }


    if (xmlStrcmp(cur->name, (const xmlChar *) "ListBucketResult")) {
        exit_msg("main","document of the wrong type, root node != ListBucketResult");
    }

    char *str, *tmp;
    int filesize;
    for (xmlNodePtr node = cur->xmlChildrenNode; node != NULL; node = node->next) {
    	if ((!xmlStrcmp(node->name, (const xmlChar *) "Contents"))) {
    		for (xmlNodePtr aux = node->xmlChildrenNode; aux != NULL; aux = aux->next) {
				if ((!xmlStrcmp(aux->name, (const xmlChar *)"Key"))) {
					str = (char *) xmlNodeGetContent(aux);
					if (str+strlen(str)-1 == rindex(str, '/')) {
						//printf("echo 'Create dir %s'\n", str);
						printf("mkdir -p \"%s\"\n", str);
						add(str);
					} else {
						for (xmlNodePtr searchSize = aux; searchSize != NULL; searchSize = searchSize->next) {
							if ((!xmlStrcmp(searchSize->name, (const xmlChar *) "Size"))) {
								filesize=atoi((char *) xmlNodeGetContent(searchSize));
								//printf("echo '%6d %s'\n", filesize, str);
								break;
							}
						}

						if (filesize != 0) {
							printf("echo 'Download %s'\n", str);
							//printf("echo \"curl -o %s %s%s\"\n", str, url, str);
							printf("curl -O \"%s%s\"\n", url, str);
						}
						tmp = rindex(str, '/');
						*tmp = '\0';
						if (filesize == 0) {
							printf("touch \"%s\"\n", tmp+1);
						}
						if (!find(str)) {
							printf("mkdir -p \"%s\"\n", str);
							add(str);
						}
						printf("mv \"%s\" \"%s\"\n", (tmp+1), str);
                	}
                }
    		}// buscando el key
    	}// si tiene contents
    }// buscar los nodos

}