#### Flag Register :
|flag|0|1|
|-|-|-|
|Zero (ZF)|None zero Result|zero Result|
|Sign (SF)|Positive (+)|Negative (-)|
|Direction (DF)|From left to right|From right to left|
|Parity (PF)|odd|even|
|Auxiliary (AF)|no carry affter add bit 4|carry affter add bit 4|
|Carry (CF)|no carry|carry|
|Overflow "unsigned"|output $\leq$ 255| output $\gt$ 255 |
|Overflow "signed"|output $\leq$ 127| output $\gt$ 127 |

---
---
#### Instruction :
**MOV**
```assmbly
mov Dest Src
```

> Dest = Reg or Mem
> Src = Reg or Mem or immediate

*errors*
- mov AL , BX 
- mov IP , 5H or mov Cs , 10H
- mov x , y
- mov 3 , x or mov 3 , Al
- mov Ds , Es

**xchg**
```assmbly
xchg Dest , Src
```

> Dest = Reg or Mem
> Src = Reg or Mem 

Dest = Src 
Src = Dest
```assmbly
mov AL , Dest
mov BL , Src
mov CL , AL
mov AL , BL
mov BL , CL
```

**LEA**

```assmbly
LEA Dest Src
```

```assmbly
mov Dest , offset Src
```

**Stack Instruction**
![[Pasted image ٢٠٢٢٠١٣٠١٢١٦٠٣.png]]

**push**
```assmbly
push Src 
```
 >Src => imm 16 bit or Reg 16 bit or mem 16 bit 

**pop**
```assmbly
pop Src
```
>Src => Reg 16 bit or mem 16 bit 

**ADD**

```add
add Dest Src
```

Dest = Dest + Src

>Dest = Reg or mem
>Src = Reg or mem or imm

**ADC**

```add
adc Dest Src
```

Dest = Dest + Src + CF

>Dest = Reg or mem
>Src = Reg or mem or imm

**SUB**

```add
sub Dest Src
```

Dest = Dest - Src

>Dest = Reg or mem
>Src = Reg or mem or imm


**SBB**

```add
sbb Dest Src
```

Dest = Dest - Src - CF

>Dest = Reg or mem
>Src = Reg or mem or imm


**INC**

```assmbly
Inc Dest
```

```assmbly
add Dest , 1
```

>Dest = Reg or mem


**DEC**

```assmbly
Dec Dest
```

```assmbly
sub Dest , 1
```

>Dest = Reg or mem

**CMP**

```
cmp Dest , Src
```
>Dest = Reg or mem
>Src = Reg or mem or imm

---
SF --> 0 Dest $\geq$ Src
SF --> 1 Dest $\leq$ Src
ZF --> 0 Dest $\geq$ Src
ZF --> 1 Dest $\leq$ Src

---

#### MUL  
-*Unsigned multiplying*
-*The general format for MUL*
```assmbly
MUL source
```

MUL BL => Ax = BL * AL        source = 8bit
MUL BX => Dx.Ax => Ax\*Bx    source = 16bit

- -> Dx = high
- -> Ax = Low

Al operand

>Note : IMUL the same MUL but used for **signed numbers**

>if the result siz greater the operand size OF=CF=1 otherwise OF=CF=0 , **other flags unchanged**

---
**DIV**

-*Unsigned multiplying*
-*The general format for MUL*
```assmbly
DIV source
```

DIV BL => Ax = Ax /BL        source = 8bit

>AL = result , AH = reminder

DIV BX => Dx.Ax = DxAx/bX    source = 16bit

- -> Dx = high
- -> Ax = Low




>Note : IMUL the same MUL but used for **signed numbers**
>
|+/+ | result + |reminder +|
|-|-|-|
|**+/-**  | **result -** |**reminder +**|
|**-/+**|**result -**|**reminder -**|
|**-/-**|**result +**|**reminder -**|
   
**CTI** *Control Transfer Instruction*

|unconditional|
|-|
|call|
|jmp|
|int|
|ret|

|conditional Flag|
|-|
|JZ   -> ZF = 1|
|JNZ -> ZF = 0|
|JC   -> CF = 1|
|JNC -> CF = 0|
|JS    -> SF = 1|
|JNS -> SF = 0|
|JO -> OF = 1|
|JNO -> OF = 0|
|JP -> PF = 1|
|JNP -> PF = 0|


*Logica instruction*
**AND**
```assmbly
and Dest , Src
```
>Dest = Reg or mem
>Src = Reg or mem or imm
>Dest = Dest and Src

**OR**
```assmbly
or Dest , Src
```
>Dest = Reg or mem
>Src = Reg or mem or imm
>Dest = Dest or Src

**XOR**
```assmbly
xor Dest , Src
```

>Dest = Dest xor Src

1 xor 0 => 1
0 xor 1 => 1
1 xor 1 => 0
0 xor 0 => 0

>Dest = Reg or mem
>Src = Reg or mem or imm

**NOT**
```assmbly
not Dest
```
Dest = !Dest

**NEG**
```assmbly
neg Dest
```
2nd Comp of Dest

**TEST**
```assmbly
test Dest , Src
```

> Dest and Src ; test Dest == Src


**Shift :**

**SHR**
```assmbly
shr Dest , # shift
```

![[Pasted image ٢٠٢٢٠١٣٠١٣٢٤٣٣.png]]

> if CF = 1 then odd else even


**SHL**
```assmbly
shl Dest , # shift
```
![[Pasted image ٢٠٢٢٠١٣٠١٣٣٠٠٦.png]]
**SAR**
```assmbly
sar Dest , # shift
```


![[Pasted image ٢٠٢٢٠١٣٠١٥٢٨٣٢.png]]

![[Pasted image ٢٠٢٢٠١٣٠١٥٢٩٠٧.png]]

**SAL**
```assmbly
sal Dest , # shift
```

![[Pasted image ٢٠٢٢٠١٣٠١٥٣٥١٢.png]]

![[Pasted image ٢٠٢٢٠١٣٠١٥٣٥٢٦.png]]
**Rotate :**

**ROR**
```asmmbly
ror Dest, # rol
```

![[Pasted image ٢٠٢٢٠١٣٠١٥٤٢٥١.png]]

**ROL**
```asmmbly
rol Dest, # rol
```
![[Pasted image ٢٠٢٢٠١٣٠١٥٤٣٢٦.png]]

**RCR**
```asmmbly
rcr Dest, # rol
```

![[Pasted image ٢٠٢٢٠١٣٠١٥٥١٠٥.png]]
**RCL**
```asmmbly
rcl Dest, # rol
```

![[Pasted image ٢٠٢٢٠١٣٠١٥٤٨٢٠.png]]

***Loop***
>Cx = Cx - 1
> if Cx $\neq$ 0 
> Jump label

***LoopE => LoopZ***
>Cx = Cx - 1
> if Cx $\neq$ 0 & if Zf = 1
> Jump label

***LoopNE=> LoopNZ***
>Cx = Cx - 1
> if Cx $\neq$ 0 & if Zf = 0
> Jump label



---
#### *string*
**movs** Si --> Di
 `movSB`  copy byte from byte  
 `movWB` copy words from words

```assembly 
mov Al , [si]
mov [di], Al
inc si
inc di
```

>Direction Flag (DF)
>STD ==> DF = 1 ;  **the processing is done forward**
>CLD ==> DF = 0 ;  **the processing is done backward**

***
**LODS** 
`LODSB` lood byte at *si* --> *Al*
if DF = 0

```assembly
mov Al,Si
INC Si
```
f DF = 1

```assembly
mov Al,Si
DEC Si
```

`LODSW` lood byte at *si* --> *Ax*

if DF = 0

```assembly
mov Al,Si
add Si,2
```
f DF = 1

```assembly
mov Al,Si
sub Si,2
```
***

**REP**

`REP` => `Loop`
`REPE` => `LoopE`
`REPNE` => `LoopNE`
***
**STOS**
`STOSB` store byte at *Al* --> *Di*
if DF = 0

```assembly
mov Di, Al
INC Di
```
f DF = 1

```assembly
mov Di, Al
DEC Di
```

`STOSW` store wored at *Ax* --> *Di*
if DF = 0

```assembly
mov Ax,Di
add Di,2
```
f DF = 1

```assembly
mov Ax,Di
sub Di,2
```
***
**Scas**
`ScasB` 
if DF = 0
```assembly
cmp Al,[Di]
CLD
INC Di
```
if DF = 1
```assembly
cmp Al,[Di]
STD
DEC Di
```
`ScasW`
if DF = 0
```assembly
cmp Ax,[Di]
CLD
add Di,2
```
if DF= 1
```assembly
cmp Ax,[Di]
STD
sub Di,2
```
***

***cmps***
`cmpsb` compre byte *Di* --> *Si*
if DF = 0

```assembly
cmp [Di],[Si]
INC Di
INC Si
```
f DF = 1

```assembly
cmp [Di],[Si]
DEC Di
DEC Si
```

`cmpsw` compre word *Di* --> *Si*
if DF = 1

```assembly
cmp [Di],[Si]
sub Si,2
sub Di,2
```
f DF = 0

```assembly
cmp Di,Si
add Si,2
add Di,2
```


***

**Interrupts**
int 0 -> 255
in each int 0 -> 255 fun 
use *Reg **AH** * to select function in Interrupt 

```assmbly
int # of Interrupts
```

Interrupt vectors = (# of Interrupt)\*4

---
**INT 10H**
the screen 
=> 25 row 0->24
=> 80 colums 0->79

---

**FUN 02H**
```assmbly
mov DH , # row
mov DL , # column
mov BH , # page
mov AH , 02h ; # fun
int 10h
```

>setting the cursor
>*BH* => page number (0 ... 7) 
>*DH* => row
>*DL* => colum 


**FUN 06H/07H**
```assmbly
mov AL , # of line
mov CX , starting row:column
mov DX , ending row:column
mov BH , attribute
mov AH , 06h or 07h ; # fun
int 10h
```


>handles screen clearing or scroling
>*BH* => attribute value (color,reverse video,blinking)
>
>|background (4 bit)|forground (4 bit)|
>|-|-|
>
>AL => number of lines to scroll , pr 00H for the full screen
>CX => starting row:column
>*DX* => ending row:column
>06H => scroll up window
>07H => scroll down window


---
**INT 21H**
Using control characters in a screen display

---

|Control character |Decimal|Hex|Effect on cusor|
|-|-|-|-|
|Carriage return|13|0Dh|Rest to left position of screen|
|Line feed|10|0Ah|Advance to next line|
|Tab|09|09h|Advance to next tab stop|


**FUN 02H**
```assmbly
mov AH , 2
mov DL , Msg
Int 21h
```

>print DL

**FUN 01H**
```assmbly
mov AH , 1h
Int 21h
```

>input in AL


**FUN 09H**

```assmbly
mov AH , 09h 
mov DX , Offset msg ; LEA DX , Offset
int 21h
```

>print string end $ or 24h

**FUN 0A**

```assmbly
buffer DB 20;maxmim size
Accl DB ?;# of bit input
Data DB buffer*dup(''); locations to save chr entered from keyboard
mov AH , 0Ah
mov DX , Offset buffer
int 21h
```

 >input string
 
#### *port instruction*

**IN instruction** : Read form port 

```assmbly
IN REGISTR , PORT
```

- REGISTER : input form port into **AL** or **Ax**

if port number less 255 can be used *Immediate value* the port number over 255 
should be use **DX** register 

**OUT instruction** : Write to port
```assmbly
OUT PORT,REGISTER
```

- REGISTER : input form port into **AL** or **Ax**

if port number less 255 can be used *Immediate value* the port number over 255 
should be use **DX** register

