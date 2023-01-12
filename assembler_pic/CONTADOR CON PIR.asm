;CONTADOR DE PERSONAS CON SENSOR PIR

#include "p18f4550.inc"
#include "config.inc"

;variables en memoria

CBLOCK	0X010
	S_PIR
	i	
END
		
	ORG		0X0000
	GOTO	SETUP
	ORG		0X0020
	
SETUP:
	MOVLW	0X62
	MOVWF	OSCCON
	MOVLW	0X0F
	MOVWF	ADCON1
	CLRF	TRISD
	BSF		TRISA,0
	CLRF	S_PIR
	MOVF	S_PIR,W
	CALL	deco7seg
	MOVWF	LATD

LOOP:
	BTFSS	PORTA,0
	GOTO	LOOP
	INCF	S_PIR
	CALL	deco7seg
	MOVWF	LATD
	MOVLW	OX0A
	CPFSEQ	S_PIR,W
	GOTO	VERIFICAR
	GOTO	CERO

VERIFICAR:
	BTFSS	PORTA,0
	GOTO	LOOP
	GOTO	VERIFICAR
	
CERO:
	CLRF	S_PIR
	MOVF	S_PIR,W
	CALL	deco7seg
	MOVWF	LATD
	GOTO	VERIFICAR
	
;DISPLAY DE 7 SEG DE CATODO COMUN
BCD7SEG:	DB	0X3F,0X06,0X5B,0X4F,0X66,0X6D,0X7D,0X07,0X7F,0X67

deco7seg:
	MOVWF	i
	MOVLW	UPPER	BCD7SEG
	MOVWF	TBLPTRU
	MOVLW	HIGH	BCD7SEG
	MOVWF	TBLPTRH
	MOVLW	LOW		BCD7SEG
	MOVWF	TBLPTRL
	MOVF	i,W
	ADDWF	TBLPTRL,F
	TBLRD*
	MOVF	TABLAT,W
	RETURN
	
#include "retardos.inc"

	END
