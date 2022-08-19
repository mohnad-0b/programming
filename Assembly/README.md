



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
  
  6-copy the following string to another string starting from first space
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
