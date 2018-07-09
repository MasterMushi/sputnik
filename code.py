from time import strftime
from os import path


def create(dgo):

    def block1(dgo_quantity):
        _text = ''
        for i in range(0, dgo_quantity):
            _text = (_text +
                     '\tprm.dgo{num}_ON = false;' +
                     ' \tprm.dgo{num}_OF = false;\n').format(num=i + 1)
        return _text

    def block2(dgo):
        _text = ''
        for i in range(0, len(dgo)):
            _text = (_text +
                     '\tprm.dgo{num}_ON = !dgo.{alg};' +
                     '\tprm.dgo{num}_OF = dgo.{alg};' +
                     '\n').format(num=i + 1, alg=dgo[i].algname)
        return _text

    def block3(dgo):
        _text = ''
        for i in range(0, len(dgo)):
            _text = (_text +
                     '\tdgo.{alg} = (btn.dgo{num}_ON || dgo.{alg}) && ' +
                     '!btn.dgo{num}_OF;' +
                     '\n').format(num=i + 1, alg=dgo[i].algname)
        return _text

    template = '''
/*******************************************************************************
 * File:    dgoControl.cpp
 * Created: by configurator {cfg_name}
 * Date:    {dt}
*******************************************************************************/

#include "AISPar.h"
#include "Externs.h"
#include "UDT_system.h"

void outputControl(void) {{
    if(!GlobalData.Test_ON) {{
    // Отключение разрешений кнопок тестирования дискр. вых.
{block1}
    }}
    else {{
    // Выдача разрешений кнопок тестирования дискр. вых.
{block2}
    // Выдача команд на включение/отключение дискр. вых.
{block3}
    }}
}}
    '''

    dt = strftime("%A, %d %B %Y %H:%M")
    cfg_name = 'asd'
    block1 = block1(len(dgo))
    block2 = block2(dgo)
    block3 = block3(dgo)

    dirname = path.dirname(__file__)
    filename = path.join(dirname, 'cpp/dgoСontrol.cpp')
    f = open(filename, 'w')
    f.write(template.format(cfg_name=cfg_name,
                            dt=dt,
                            block1=block1,
                            block2=block2,
                            block3=block3
                            )
            )
    f.close
