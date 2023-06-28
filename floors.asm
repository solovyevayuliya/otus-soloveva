%include 'library.asm'

section .data
    arr dd  'u', 'd', 'd', 'u', 'u', 'd', 'd', 'u'
    n   dd  8

section .text
    global _start

_start:
    mov eax, 0     ; result
    mov edx, 0     ; count
    mov ecx, [n]   ; n
	mov esi, arr   ; array
	cmp ecx, 0
		je done

loop_start:
	cmp word [esi], 'u'				;сравниваем эл-т массива с 'u'
	je increase__u					;если эл-ты равны, то переходим в increase__u
	cmp word [esi], 'd'				;сравниваем эл-т массива с 'd'
	je increase__d					;если эл-ты равны, то переходим в increase__d
	jmp continue_loop

increase__u:
	inc edx
	jmp continue_loop


increase__d:
	dec edx
	jmp continue_loop


continue_loop:
    add esi, 4 						; двигаем массив на следующий элемент
    dec ecx							; уменьшаем n
		jnz loop_start				; если n != 0 то продолжаем цикл. Иначе ниже в result

result:
	cmp edx, 0
	je result_one
	jne result_zero


result_one:
	mov eax, 1
	jmp done

result_zero:
	mov eax, 0
	jmp done

done:
    call print_number
    call exit