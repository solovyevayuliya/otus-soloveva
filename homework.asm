;Задача 1: самая длинная последовательность

%include 'library.asm'

section .data
arr dd  0, 0, 1, 0, 1, 1, 1, 0
n   dd  8

section .text
global _start

_start:
mov eax, 0     ; maxCount
mov ebx, 0     ; curentCount
mov edx, 0     ; prevEl
mov ecx, [n]   ; n
mov esi, arr   ; array
cmp ecx, 0
je done

loop_start:
cmp byte[esi], 0
je skip_zero
cmp  edx, [esi]  			; сравниваем prevEl и arr[i]
je increase_curent_count    ; если arr[i] == prevEl, то увеличиваем curentCount
jne reset_curent_count		; если arr[i] != prevEl, то сбрасываем curentCount

skip_zero:
mov ebx, 0				        ; currentCount = 0
mov edx, 0						; сбрасываем prevEl
jmp continue_loop

increase_curent_count:
inc ebx							 ; curentCount++
jmp check_max_count_and_continue

reset_curent_count:
mov ebx, 1						; currentCount = 1
jmp check_max_count_and_continue

check_max_count_and_continue:
mov edx, [esi]					; prevEl = arr[i]
cmp ebx, eax					; сравниваем currentCount и maxCount
jle continue_loop			    ; если currentCount < maxCount то продолжаем цикл
mov eax, ebx					; иначе maxCount = currentCount
jmp continue_loop

continue_loop:
add esi, 4 						; двигаем массив на следующий элемент
dec ecx							; уменьшаем n
jnz loop_start				    ; если n != 0 то продолжаем цикл. Иначе ниже в done

done:
call print_number
call exit