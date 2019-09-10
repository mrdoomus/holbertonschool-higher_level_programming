#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: Pointer to head
 * Return: 1 if it has a cycle, 0 if it doesn't
**/
int check_cycle(listint_t *list)
{
	listint_t *one, *two;
	one = list;
	two = list;

	while (two != NULL && two->next != NULL)
	{
		one = one->next;
		two = two->next->next;
		if (one == two)
			return (1);
	}
return (0);
}
