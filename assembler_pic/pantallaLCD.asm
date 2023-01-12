#include "p18f4550.inc"
#include "config.inc"
#define		RS		0
#define		E		1
#define		dato		LATB
#define		control		LATD
#define		lcd_dato	TRISB
#define		lcd_control	TRISD

;codigo principal

	org		0x0000
	goto	SETUP
	org		0x0020

SETUP:
	movlw	0x62
	movwf	OSCCON
	movlw	0x0f
	movwf	ADCON1
	;rutina para inicializar lcd
	call	lcd_begin
	;rutina para mover el cursor en la fila 0
	movlw	.0
	call	lcd_fila0
	;rutina para imprimir una cadena en lcd
	movlw 	.0
	call	lcd_print
	;rutina para mover el cursor en la fila 1
	movlw	.0
	call	lcd_fila1
	;rutina para imprimir una cadena en el LCD
	movlw	.12
	call 	lcd_print
LOOP:
	goto	LOOP

;mensajes
mensajes:	;ptr
	data	"hola UMAKER"
	data	"PIC en ASM"
	
;subrutinas LCD en 8bits
	cblock
		ptr_pos
		ptr_count
	endc
	
;inicializar la pantalla LCD
lcd_begin:
	clrf	lcd_dato	
	bcf		lcd_control,RS
	bcf		lcd_control,E
	call	retardo_15ms
	movlw	0x38
	call	lcd_comando
	movlw	0x01
	call 	lcd_comando
	movlw	0x0c
	call	lcd_comando
	movlw	0x06
	call	lcd_comando	
	return
	
;limpiar pantalla lcd
lcd_clear:
	movlw	0x01
	call 	lcd_comando
	return
	
;imprimir un caracter
lcd_char:
	movwf	dato
	bsf		control,RS
	bsf		control,E
	call	retardo_1ms
	bcf		control_E
	call	retardo_1ms
	return
	
;imprimir una cadena de caracteres
lcd_print:
	movwf	ptr_pos
	movlw	UPPER	mensajes
	movwf 	TBLPTRU
	movlw	HIGH	mensajes
	movwf	TBLPTRH
	movlw	LOW	mensajes
	movwf	TBLPTRL
	movf	ptr_pos,W
	addwf	TBLPTRL,F
	clrf	WREG
	addwfc	TBLPTRH,F
	addwfc	TBLPTRU,F
	
leer:
	TBLRD*+
	
verificar:
	movlw	0x00
	cpfseq	TABLAT
	goto	print
	return
	
print:
	movf	TABLAT,W
	call	lcd_char
	goto	leer
	
lcd_fila0:
	andlw	0x0f
	iorlw	0x80
	call	lcd_comando
	return
	
lcd_fila1:
	andlw	0x0f
	iorlw	0xc0
	call	lcd_comando
	return
	
lcd_comando:
	movwf	dato
	bcf		control,RS
	bsf		control,E
	call	retardo_1ms
	bcf		control,E
	call	retardo_1ms
	return
	
#include"retardo.inc"

	end
