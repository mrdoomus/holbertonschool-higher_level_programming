#include "lists.h"

int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *tmp = list;

	while (tmp->next != NULL && i <= 100)
	{
		tmp = tmp->next;
		i++;
	}

	if (i >= 100)
		return (1);
return (0);
}
