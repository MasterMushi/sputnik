
/*******************************************************************************
 * File:    dgoControl.cpp
 * Created: by configurator asd
 * Date:    Sunday, 08 July 2018 13:49
*******************************************************************************/

#include "AISPar.h"
#include "Externs.h"
#include "UDT_system.h"

void outputControl(void) {
    if(!GlobalData.Test_ON) {
    // Отключение разрешений кнопок тестирования дискр. вых.
	prm.dgo1_ON = false; 	prm.dgo1_OF = false;
	prm.dgo2_ON = false; 	prm.dgo2_OF = false;

    }
    else {
    // Выдача разрешений кнопок тестирования дискр. вых.
	prm.dgo1_ON = !dgo.alg_name1;	prm.dgo1_OF = dgo.alg_name1;
	prm.dgo2_ON = !dgo.alg_name2;	prm.dgo2_OF = dgo.alg_name2;

    // Выдача команд на включение/отключение дискр. вых.
	dgo.alg_name1 = (btn.dgo1_ON || dgo.alg_name1) && !btn.dgo1_OF;
	dgo.alg_name2 = (btn.dgo2_ON || dgo.alg_name2) && !btn.dgo2_OF;

    }
}
    