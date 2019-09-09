#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: Pointer to head
 * Return: 1 if it has a cycle, 0 if it doesn't
**/
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *tmp;

	if (list == NULL)
		return (0);
	tmp = list;

	while (tmp->next != NULL && i <= 100)
	{
		tmp = tmp->next;
		i++;
	}

	if (i >= 100)
		return (1);
return (0);
}
