#ifndef Demo01_H
#define Demo01_H

#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include "diplomat_runtime.h"


#include "Demo01.d.h"






void Demo01_greeting(DiplomatStringView name, DiplomatWrite* write);


void Demo01_destroy(Demo01* self);





#endif // Demo01_H
