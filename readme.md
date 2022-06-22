# LZ78 demo

## Examples

```bash
$ python lz78encode.py "красная краска"
'к'     <0, 'к'>        1
'р'     <0, 'р'>        2
'а'     <0, 'а'>        3
'с'     <0, 'с'>        4
'н'     <0, 'н'>        5
'ая'    <3, 'я'>        6
' '     <0, ' '>        7
'кр'    <1, 'р'>        8
'ас'    <3, 'с'>        9
'ка'    <1, 'а'>        10
len(ret)=10
<0, 'к'> <0, 'р'> <0, 'а'> <0, 'с'> <0, 'н'> <3, 'я'> <0, ' '> <1, 'р'> <3, 'с'> <1, 'а'>
decoded: 'красная краска'

$ python lz78encode.py "11000000110111100110"
'1'     <0, '1'>        1
'10'    <1, '0'>        2
'0'     <0, '0'>        3
'00'    <3, '0'>        4
'001'   <4, '1'>        5
'101'   <2, '1'>        6
'11'    <1, '1'>        7
'100'   <2, '0'>        8
'110'   <7, '0'>        9
len(ret)=9
<0, '1'> <1, '0'> <0, '0'> <3, '0'> <4, '1'> <2, '1'> <1, '1'> <2, '0'> <7, '0'>
decoded: '11000000110111100110'
```
