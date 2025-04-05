	.text
	.file	"output.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$1, 4(%rsp)
	xorl	%eax, %eax
	testb	%al, %al
	jne	.LBB0_1
# %bb.3:                                # %else.0
	movl	$fmt.5, %edi
	movl	$str.4, %esi
	jmp	.LBB0_2
.LBB0_1:                                # %then.0
	movl	$fmt.3, %edi
	movl	$str.2, %esi
.LBB0_2:                                # %ifcont
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	str.2,@object                   # @str.2
	.section	.rodata,"a",@progbits
str.2:
	.asciz	"Nose"
	.size	str.2, 5

	.type	fmt.3,@object                   # @fmt.3
fmt.3:
	.asciz	"%s\n"
	.size	fmt.3, 4

	.type	str.4,@object                   # @str.4
str.4:
	.asciz	"si se"
	.size	str.4, 6

	.type	fmt.5,@object                   # @fmt.5
fmt.5:
	.asciz	"%s\n"
	.size	fmt.5, 4

	.section	".note.GNU-stack","",@progbits
