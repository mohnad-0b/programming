



 1- Procedure to find number of odd words in the array
   
 ```Assembly
        org 100h
    
    mov cx,10
    mov si,offset X
    L:
    mov ax , [si]
    rcr ax , 1
    jc n
    c: 
    inc si
    inc si 
    loop L
    
    hlt
    
    X dw 9,10,12,56,43,2,5,13,43,44
    
    odd db 0   
    n:
     inc odd
     jmp c
 ```
 
 ---
 
 2- Procedure to find the maximum word in the array
 ```Assembly
        org 100h
    
    mov cx,10
    mov si , offset X
    mov ax , [si]
    mov max , ax
    add si , 2
    L: 
    mov ax,[si]
    cmp ax,max
    jg m
    c: add si,2
    loop L
    
    hlt
    X dw 250,10,12,32767,43,2,5,13,43,99
    max dw ? 
    m: 
    mov max ,ax
    jmp c
 ```
 
 ---
 
 3- Procedure to find number of 1's in the maximum word
 ```Assembly
    org 100h
    
    mov cx,10
    mov si , offset X
    mov ax , [si]
    mov max , ax
    add si , 2
    L: 
    mov ax,[si]
    cmp ax,max
    jg m
    c: add si,2
    loop L
    mov cx,16
    mov ax,max
    L2:
    rcr ax,1
    jc O
    c2:
    loop L2
    
    hlt
    X dw 250,10,12,32767,43,2,5,13,43,99
    max dw ?
    one db 0 
    m: 
    mov max ,ax
    jmp c   
    O:
    inc one
    jmp c2
```

---

4- write a program to store 'y' in the variable same if the two strings X and Y are same else store 'N' in the variable same if the two stringsX and Yare not same
   
   X db 'abcdaefgak'
   Y db 'abcdlefgak'
   Same db ?
 ```Assembly
    org 100h
            mov di,offset x
            mov si,offset y
            mov cx , 10
            L:
               cmpsb
               jnz n
            loop L 
            mov Same,"Y"
    
    hlt 
      X db 'abcdaefgak'
      Y db 'abcdaefgak'
      Same db ?  
      
    n:
     mov Same,"N"
     hlt
```

---


5- input number and print "*" in center secren  
```Assembly
    org 100h
    
    mov dh,12
    mov dl,39
    mov ah,02h
    int 10h
    
    mov ah,01h
    int 21h 
    sub al,48
    mov cl,al
    
    L:
    
     
      mov ah,02h
      mov dl , msg
      int 21h
    loop L      
    
    hlt
    
    msg db "*"
```

---

6- if input "A" print 
  
  A   A   A   A
  A     A     A
  A       A       A
  
  if "B" print
  
  B
  BB
  BBB
  BBBB
  ```Assembly
          org 100h
        
        mov ah,01h
        int 21h
        cmp al,"A"
        jZ print_A
        cmp al,"B"
        jZ print_B
        
        hlt
        
        msg_A db        9,"A",9,"A",9,"A",0ah,0dh,"A",9,9,"A",9,9,"A",0ah   ,0dh,"A",9    ,9,9,"A",9,9,9,"A"
        msg_B db        0ah,0dh,"B","B",0ah,0dh,"B","B","B",0ah,0dh,"B","B","B","B"
        print_A:
        mov cx , 28
        mov si , offset msg_A
        mov ah,02h
        L1:
        mov dl ,[si]
        int 21h
        inc si
        loop L1
        hlt    
        print_B:
        mov cx , 15
        mov si , offset msg_B
        mov ah,02h
        L2:
        mov dl ,[si]
        int 21h
        inc si
        loop L2
        hlt
  ```
 
---
 
7-copy the following string to another string starting from first space
x db 'This is my program'
y db 20 dup(?)

```Assembly
org 100h

mov di,offset x
mov si,offset y
mov al," "
mov cx , 20

L: 
 scasb
 je FindSpace
 inc si
 loop L 
           
HLT

x db 'This is my program'
y db 20 dup(?)

FindSpace:  
  mov al,[di]
  mov [si],al
  inc si
  inc di
  loop FindSpace
 HLT 

```

---

8- replace the character 'a' in the follwing string to '\*' string 
db 'abcdefaghiak'

```Assembly
org 100h

mov di,offset x
mov al, 'a'
mov cx,12
L: 
 scasb
 je findA
 loop L 
END: hlt

x db "abcdefaghiak"
findA:
 mov [di-1],"*"
 cmp cx,0
 je END
 jmp L
```

---

9- write a progran that find the max and min number in the following array arr[] = {1,-5,0,7,9,-8,13,-12,4,-2}

```Assembly
;write a progran that find the max and min number in the following array
;arr[] = {1,-5,0,7,9,-8,13,-12,4,-2}

org 100h

mov si, offset arr
mov cx,10
mov al , [si]
mov min , al
mov max , al


L: 
    mov al,[si]
    
    ;L_for_find_min:
        cmp al,min
        jl find_min
    
    L_for_find_max:
        cmp al,max
        jg find_max
    
    inc si 
loop L

hlt

arr db 1,-5,0,7,9,-8,13,-12,4,-2
min db 0
max db 0


find_min:
    mov min,al
    cmp cx,0
    jne L_for_find_max 
    hlt 
    
find_max:
    mov max,al
    inc si   
    dec cx
    cmp cx,0
    jne L
    hlt  
 ```
 
 ---
 
10- Write a program in assembly language to read the following matrix x db 1,5,4,3,6 

&nbsp;&thinsp;odd numbers counter \
&nbsp;&thinsp;even numbers counter \
&nbsp;&thinsp;odd numbers sum  \
&nbsp;&thinsp;even numbers sum 
  
```Assembly
org 100h

mov si, offset arr
mov cx,5   
mov bl,2
; div x => ax = al/x
L:  
    mov al,[si]  
    div bl
    cmp ah,0
    je find_even
    jmp find_odd    


hlt
 
arr db 01h,05h,04h,03h,06h

num_odd db 0
num_even db 0
sum_of_odd db 0 
sum_of_even db 0


find_even:
    inc num_even
    mov al,[si]
    add sum_of_even,al
    inc si
    dec cx
    cmp cx,0
    jne L
    hlt
    
find_odd:
    inc num_odd
    mov al,[si]
    add sum_of_odd,al
    inc si
    dec cx
    cmp cx,0
    jne L
```

use for loop 

```Assembly
org 100h

mov si, offset arr
mov cx,5   
mov bl,2
; div x => ax = al/x
L:  
    mov al,[si]  
    div bl
    cmp ah,0
    je find_even
    jmp find_odd 
    C:
loop L   


hlt
 
arr db 01h,05h,04h,03h,06h

num_odd db 0
num_even db 0
sum_of_odd db 0 
sum_of_even db 0


find_even:
    inc num_even
    mov al,[si]
    add sum_of_even,al
    inc si
    jmp C
  
    
find_odd:
    inc num_odd
    mov al,[si]
    add sum_of_odd,al 
    inc si
    jmp C
```

--- 

11 - Write an assembly code to set bit#3 and reset bit#4 in each element in array Z.
Z DB 66H,78H,33H

```Assembly
org 100h

mov cx,3
mov si,offset ZZ

L:
and [si],247
or [si],4
inc si
loop L 

hlt

ZZ DB 66H,78H,33H
```

---

12 - convert the capital letters to small letters and the small to capital in string str
str db ‘ABcdEFgh’

```Assembly
org 100h

mov cx,8
mov si,offset str

L:
mov al,[si]
and al,32
cmp al,0
je s_to_c 
and [si],223
inc si
loop L 

hlt


str db 'ABcdEFgh'

s_to_c:
      or [si],32
      inc si
      dec cx
      jmp L
```
